import pandas as pd
from datetime import datetime, timedelta
from api import static
from setup import setup
import sqlalchemy as sa


def get_last_status(pool):
    query = sa.text("select * from elements_summary;")
    with pool.connect() as conn:
        elements = pd.read_sql(query, con=conn)
    return elements


if __name__ == '__main__':
    today = datetime.now()
    pool = setup()
    last_all = get_last_status(pool)
    last = last_all[['id', 'now_cost']]
    last_all.to_sql(name='test_table_1', con=pool.connect(), if_exists='append', index=False)
    # last_all.to_sql(name='test_table', con=pool, if_exists='replace', index=False)
