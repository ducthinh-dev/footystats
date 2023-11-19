def setup():
    import os
    from dotenv import load_dotenv
    import sqlalchemy as sa
    import mysql.connector
    
    load_dotenv()
    HOST = os.environ.get('HOST')
    DATABASE = os.environ.get('DATABASE')
    DUSERNAME = os.environ.get('DUSERNAME')
    DPASSWORD = os.environ.get('DPASSWORD')

    def getconn():
        conn = mysql.connector.connect(
            host=HOST,
            user=DUSERNAME,
            password=DPASSWORD,
            database=DATABASE
        )
        return conn

    pool = sa.create_engine(
        "mysql+mysqlconnector://",
        creator=getconn,
    )

    with pool.connect() as db_conn:
        results = db_conn.execute(sa.text("SELECT NOW()")).fetchone()
        print("Current time: ", results[0])
    return pool