CREATE TABLE CUSTOMERS (
  CustID VARCHAR(20) NOT NULL,
  CustName  VARCHAR(20) NOT NULL,
  CustRating VARCHAR(10) NOT NULL,
  Reserves INT DEFAULT 0,
  Phone VARCHAR(11) NOT NULL,
  Address VARCHAR(50),
  PRIMARY KEY(CustID)
);


INSERT INTO CUSTOMERS (CustID, CustName, CustRating, Reserves, Phone, Address)
VALUES ('magician', 'Lee', 'gold', 30000, '01022221234', 'Seoul');

DROP TABLE IF EXISTS ORDERS;


CREATE TABLE ORDERS (
  OrderNumber INT NOT NULL,
  CustID VARCHAR(20) NOT NULL,
  ProdName  VARCHAR(20) NOT NULL,
  Quantity INT DEFAULT 0,  
  UnitPrice INT NOT NULL, 
  OrderDate DATE,
  PRIMARY KEY(OrderNumber)
);

INSERT INTO ORDERS (OrderNumber, CustID, ProdName, Quantity, UnitPrice, OrderDate )
VALUES (2018010101, 'banganboy', 'BlackRamen', 10, 1500, '2018-01-01');

