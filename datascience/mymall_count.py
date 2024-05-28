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

sql = """
SELECT COUNT(OrderDate) 
FROM ORDERS 
WHERE OrderDate > '2018-03-01';
"""

sql = """
SELECT MAX(UnitPrice) 
FROM ORDERS 
WHERE OrderDate > '2018-03-01';
"""

sql = """
SELECT AVG(Quantity) 
FROM ORDERS 
"""

sql = """
UPDATE ORDERS 
SET ProdName='스낵라면'
WHERE ProdName='짜짜로니';
"""

sql = """
SELECT  *
FROM ORDERS;
"""

sql = """
SELECT  ProdName, sum(quantity)
FROM ORDERS
GROUP BY ProdName;
"""

sql = """
SELECT  ProdName, sum(quantity * UnitPrice)
FROM ORDERS
GROUP BY ProdName;
"""

sql = """
SELECT  CUSTOMERS.CustName, CUSTOMERS.Phone, ORDERS.ProdName, ORDERS.OrderDate
FROM ORDERS, CUSTOMERS
WHERE ORDERS.CustID = CUSTOMERS.CustID;
"""

sql = """
SELECT  CUSTOMERS.CustName, CUSTOMERS.Phone, ORDERS.quantity * ORDERS.UnitPrice, ORDERS.OrderDate
FROM ORDERS, CUSTOMERS
WHERE ORDERS.ProdName='스낵라면'
      AND ORDERS.CustID = CUSTOMERS.CustID;
"""

result = cur.execute( sql )
#print( type(result), result)

#cnt=0
#r = result.fetchone()
#print(r)
for r in result:
#    cnt+=1
#    print(cnt, r)

    for i in range(len(r)):
        print(r[i], end=' ')
    else:
        print()


con.commit()
cur.close()
con.close()
