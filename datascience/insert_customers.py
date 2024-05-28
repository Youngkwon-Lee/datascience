import sqlite3

con = sqlite3.connect('mymall.db')
cur = con.cursor()

sql = """
INSERT INTO CUSTOMERS (CustID, CustName, CustRating, Reserves, Phone, Address)
VALUES ('magician', '이현우', 'gold', 30000, '01022221234', '서울');
"""
cur.execute( sql )

sql = """
INSERT INTO CUSTOMERS (CustID, CustName, CustRating, Reserves, Phone, Address)
VALUES ('kwon3856', '이영권', 'Platinum', 10000, '01067046556', '부산');
"""
cur.execute( sql )

sql = """
INSERT INTO CUSTOMERS (CustID, CustName, CustRating, Reserves, Phone, Address)
VALUES ('eskim', '김이슬', 'silver', 20000, '01011111111', '부천');
"""
cur.execute( sql )

sql = """
INSERT INTO CUSTOMERS (CustID, CustName, CustRating, Reserves, Phone, Address)
VALUES ('yk', '이승만', 'bronze', 40000, '01022222222', '강릉');
"""
cur.execute( sql )

sql = """
INSERT INTO CUSTOMERS (CustID, CustName, CustRating, Reserves, Phone, Address)
VALUES ('hoho', '박지성', 'gold', 50000, '01055555555', '인천');
"""
cur.execute( sql )



con.commit()
cur.close()
con.close()