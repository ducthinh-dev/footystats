import pandas as pd
from datetime import datetime, timedelta
from api import static

if __name__ == '__main__':
    today = datetime.now()
    live_status = static()

    #GET LAST CHANGES
    yesterday = today - timedelta(1)
    last_changes = pd.read_excel(
        rf'D:\project\footystats\changes\cost_changes_{yesterday.date()}.xlsx')
    last_changes_code = last_changes['code'].tolist()

    #GET NOW CHANGES
    elements_df = live_status.get_elements_summary()
    cost_columns = ['code', 'web_name', 'cost_change_event', 'cost_change_event_fall', 'cost_change_start',
                    'cost_change_start_fall', 'now_cost']
    now_changes = elements_df.loc[elements_df.cost_change_event !=
                                       0, cost_columns]
    now_changes['now_cost'] = now_changes['now_cost'].apply(lambda x: x*0.1)
    now_changes_code = now_changes['code'].tolist()

    diff = list(set(now_changes_code).difference(set(last_changes_code)))

    now_changes.to_excel(
        rf'D:\project\footystats\changes\cost_changes_{today.date()}.xlsx', index=None)
