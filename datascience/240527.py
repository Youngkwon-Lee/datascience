

class CONFIG : 
    pymysql_info_file = './private/pymysql_info.txt'
    db_name = 'sakila'

#======================================================
import sqlite3
from sqlalchemy import create_engine
import pymysql
pymysql.install_as_MySQLdb()
import MySQLdb
from pprint import pprint


with open(CONFIG.pymysql_info_file, 'r') as memo :
    pymysql_info = memo.readlines()
memo.close()

host = pymysql_info[0].strip()
user  = pymysql_info[1].strip()
password = pymysql_info[2].strip()

print(host, user, password)

def load_cursor() :
    conn = pymysql.connect(host=host, user=user, password=password, db=CONFIG.db_name, charset='utf8')
    cursor = conn.cursor(pymysql.cursors.DictCursor)
    return conn, cursor

# SELECT * FROM CUSTOMERS

con = sqlite3.connect('mymall.db')
cur = con.cursor()

sql = "select * from actor;"
cur.execute(sql)
data= cur.fetchall()

for r in enumerate(data):
    if i >2: break
    pprint(r)

execute_df = pd.DataFrame(data)
print(execute_df)
engine = create_engine(f"mysql+mysqldb://{user}:{password}@{host}/{CONFIG.db_name}", echo=True)

conn = engine.connect()
execute_df.to_sql( name='tmp', con=engine, if_exists = 'replace', index=False)

cur.close()
conn.close()
