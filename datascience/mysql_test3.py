class CONFIG:
    pymysql_info_file = './private/pymysql_info.txt'
    db_name = 'sakila'


import pymysql
import pandas as pd
from sqlalchemy import create_engine
pymysql.install_as_MySQLdb()
import MySQLdb
from pprint import pprint

with open(CONFIG.pymysql_info_file, 'r') as memo:
    pymysql_info = memo.readlines()
    memo.close()

print(pymysql_info)

host = pymysql_info[0].strip()
user = pymysql_info[1].strip()
password = pymysql_info[2].strip()

print(host, user, password)


def load_cursor():
    conn = pymysql.connect( host=host,
                        port=3306,
                        user=user,
                        password=password,
                        db=CONFIG.db_name,
                        charset='utf8')
    cur = conn.cursor( pymysql.cursors.DictCursor)
    return conn, cur

conn, cur = load_cursor()

sql = "select * from actor;"
cur.execute( sql)
data= cur.fetchall()

for i, r in enumerate(data):
    if i >2: break
    pprint(r)

execute_df = pd.DataFrame(data)
print(execute_df)
engine = create_engine(f"mysql+mysqldb://{user}:{password}@{host}/{CONFIG.db_name}",
                       echo=True)
conn = engine.connect()
execute_df.to_sql( name='tmp', con=engine, if_exists = 'replace', index=False)

cur.close()
conn.close()
