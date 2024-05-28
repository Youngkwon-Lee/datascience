import sqlite3
# ORDERS 테이블 스키마 생성

con = sqlite3.connect('mymall.db')
cur = con.cursor()

sql = """
INSERT INTO ORDERS (OrderNumber, CustID, ProdName, Quantity, UnitPrice, OrderDate)
VALUES (2018010101, 'kwon3856', '짜짜로니', 10, 1500, '2018-01-01');
"""
cur.execute( sql )

sql = """
INSERT INTO ORDERS (OrderNumber, CustID, ProdName, Quantity, UnitPrice, OrderDate)
VALUES (2018020102, 'eskim', '우정파이', 2, 3500, '2018-02-01');
"""
cur.execute( sql )

sql = """
INSERT INTO ORDERS (OrderNumber, CustID, ProdName, Quantity, UnitPrice, OrderDate)
VALUES (2018030203, 'wannatwo', '스낵라면', 5, 2500, '2018-03-01');
"""
cur.execute( sql )

sql = """
INSERT INTO ORDERS (OrderNumber, CustID, ProdName, Quantity, UnitPrice, OrderDate)
VALUES (2018041201, 'moonlight', '맛있는덮밥', 3, 2500, '2018-04-12');
"""
cur.execute( sql )

sql = """
INSERT INTO ORDERS (OrderNumber, CustID, ProdName, Quantity, UnitPrice, OrderDate)
VALUES (20180513789, 'magician', '탄산콜라', 3, 2000, '2018-02-05');
"""
cur.execute( sql )


con.commit()
cur.close()
con.close()
