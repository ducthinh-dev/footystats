def setup(database,host='localhost',user='root'):
    import sqlalchemy as sa
    import mysql.connector
    import getpass
    
    HOST = host
    USER = user
    DATABASE = database
    PASSWORD = getpass.getpass(prompt='input password: ')

    def getconn():
        conn = mysql.connector.connect(
            host=HOST,
            user=USER,
            password=PASSWORD,
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