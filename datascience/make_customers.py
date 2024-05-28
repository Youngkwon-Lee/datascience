import sqlite3
# CUSTOMERS 테이블 스키다 생성

con = sqlite3.connect('mymall.db')
cur = con.cursor()

cur.execute("DROP TABLE IF EXISTS CUSTOMERS ")
sql = """
CREATE TABLE CUSTOMERS (
  CustID VARCHAR(20) NOT NULL,
  CustName  VARCHAR(20) NOT NULL,
  CustRating VARCHAR(10) NOT NULL,
  Reserves INT DEFAULT 0,
  Phone VARCHAR(11) NOT NULL,
  Address VARCHAR(50),
  PRIMARY KEY(CustID)
);
"""
cur.execute( sql )
con.commit()
cur.close()
con.close()
