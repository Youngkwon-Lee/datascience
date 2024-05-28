import sqlite3
# SELECT * FROM CUSTOMERS

con = sqlite3.connect('mymall.db')
cur = con.cursor()

sql = """
SELECT * 
FROM CUSTOMERS 
WHERE CustID = 'kwon3856';
"""

sql = """
SELECT CustID, CustName 
FROM CUSTOMERS 
WHERE CustID = 'kwon3856';
"""

sql = """
SELECT ProdName, UnitPrice 
FROM ORDERS 
WHERE UnitPrice >= 2000;
"""

sql = """
SELECT CustID, ProdName, OrderDate 
FROM ORDERS 
WHERE Quantity * UnitPrice > 7000;
"""

sql = """
SELECT CustID, ProdName, OrderDate 
FROM ORDERS 
WHERE OrderDate > '2018-03-01';
"""

result = cur.execute( sql )
for r in result:
    for i in range(len(r)):
        print(r[i], end=' ')
    else:
        print()


con.commit()
cur.close()
con.close()
