import pandas as pd
import datetime
from api import static

if __name__ == '__main__':
    today = datetime.datetime.now()
    live_status = static()
    elements_df = live_status.get_elements_summary()
    cost_columns = ['code', 'web_name', 'cost_change_event', 'cost_change_event_fall', 'cost_change_start',
                    'cost_change_start_fall', 'now_cost']
    now_cost_changes = elements_df.loc[elements_df.cost_change_event != 0, cost_columns]
    now_cost_changes['now_cost'] = now_cost_changes['now_cost'].apply(lambda x: x*0.1)
    now_cost_changes.to_excel(rf'D:\project\footystats\changes\cost_changes_{today.date()}.xlsx',index=None)