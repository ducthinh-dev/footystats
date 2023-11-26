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

    engine = sa.create_engine(
        "mysql+mysqlconnector://",
        creator=getconn,
    )
    return engine