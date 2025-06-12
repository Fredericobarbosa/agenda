import MySQLdb
from config import *

def get_db_connection():
    return MySQLdb.connect(
        host=DB_HOST, port=int(DB_PORT),
        user=DB_USER, passwd=DB_PASSWORD, db=DB_NAME
    )
