import pandas as pd
from datetime import datetime, timedelta
from api import static
from setup import setup
import sqlalchemy as sa


def get_last_status(engine):
    query = sa.text("select * from elements_summary;")
    with engine.begin() as conn:
        elements = pd.read_sql(query, con=conn)
    return elements


def get_live_status():
    live_status = static()
    elements = live_status.get_elements_summary()
    return elements


if __name__ == '__main__':
    today = datetime.now()
    engine_changes = setup()
    engine_live = setup()
    last_all = get_last_status(engine_changes)
    live_all = get_live_status()
    live = live_all.loc[live_all['cost_change_event'] != 0,['id', 'now_cost']]
    last = last_all.loc[last_all['cost_change_event'] != 0,['id', 'now_cost']]

    # GET CHANGES LIST
    last_list = ['-'.join([str(i) for i in e])
                 for e in last.to_numpy()]
    live_list = ['-'.join([str(i) for i in e])
                 for e in live.to_numpy()]
    diff = list(set(live_list).difference(set(last_list)))

    # IF CHANGES AVAILABLE
    # if len(diff) > 0:
    changes_list = [int(e.split('-')[0]) for e in diff]

    # GET DIFFERENCE
    last = last_all.loc[last_all['id'].isin(changes_list), ['id', 'now_cost']]
    live = live.loc[live['id'].isin(changes_list), ['id', 'now_cost']]
    changes = last.join(live.set_index('id'), on='id',
                        how='right', rsuffix='_live', lsuffix='_last')
    changes['cost_difference'] = changes['now_cost_live'] - changes['now_cost_last']
    changes['date_change'] = today.date().isoformat()

    # PUSH TO DB
    changes.to_sql(name='elements_cost_changes', con=engine_changes, if_exists='append', index=False)
    live_all.to_sql(name='elements_summary', con=engine_live, if_exists='replace', index=False)