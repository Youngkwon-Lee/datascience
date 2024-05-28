import sqlite3

def Menu():
    while True:
        print("1 = 회원 조회")
        print("2 = 주문 조회")
        print("3 = 회원 검색")
        print("4 = 주문 검색")
        print("0 = Exit program")
        num = input("번호: ")
        if num.isdigit():
            num = int( num )
            if num in range(0,5):
                return num

CustomerSchema="CustomerID CustomerName Rating Reserves PhoneNumber Address"
OrderSchema ="OrderNUmber CustomerName ProductName Quiantity UnitPrice OrderDate"

def printResult(schema, result):
    schema_list = schema.split()
    print("-"*(len(schema)+10))
    print(schema)
    print("-"*(len(schema)+10))

    cnt = 0
    for rec in result:
        cnt += 1
        for j in range(len(rec)):
            print(rec[j], end=" ")
            if len(str(rec[j])) < len(schema_list[j]):
              print(" "*(len(schema_list[j])-len(str(rec[j]))), end="")
        print( )
        
    print("-"*(len(schema)+10))
    return cnt

#온라인 몰 프로그램
con = sqlite3.connect( 'mymall.db')
cur = con.cursor()

while True:
    cmd = Menu()
    if cmd == 0:
        break
    elif cmd == 1:
        sql = """
        SELECT * FROM CUSTOMERS;
        """
        result = cur.execute( sql )
        cnt = printResult(CustomerSchema, result)
        print(f'{cnt} 명의 회원이 있습니다.\n')

    elif cmd == 2:
        sql = """
        SELECT * FROM ORDERS;
        """
        result = cur.execute( sql )
        cnt = printResult(OrderSchema, result)
        print(f'{cnt}건의 주문이 있습니다.\n')
    elif cmd == 3:
        pnum = input('전화번호 끝의 네자리를 입력하세요: ')

        sql ="""
        SELECT * FROM CUSTOMERS
        WHERE Phone like '%"""+ pnum + """';"""

        result = cur.execute( sql )
        cnt = printResult(CustomerSchema, result)
        if cnt:
            print(f'{cnt} 명의 고객이 있습니다.\n')
        else:
            print('고객 정보가 없습니다.\n')

    elif cmd == 4:
        pname = input('상품명을 입력하세요:')

        sql = """
        SELECT * FROM ORDERS
        WHERE ProdName like '"""+ pname + """;"""

        result = cur.execute(sql)
        cnt = printResult(OrderSchema, result)
        if cnt:
            print(f'{cnt} 건의 주문이 있습니다.\n')
        else:
            print('주문 정보가 없습니다.\n')


cur.close()

con.close()