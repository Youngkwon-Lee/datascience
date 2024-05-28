import pymysql

# 데이터베이스 연결 설정
conn = pymysql.connect(host='localhost', port=3306, user='root', password='3856', db='sakila')

# 커서 생성
cursor = conn.cursor()

# SQL 쿼리 실행
sql = "SELECT * from actor"`
cursor.execute(sql)

# 쿼리 결과 가져오기
data = cursor.fetchall()

# 결과 출력
for row in data:
    print(row)

# 커서와 연결 닫기
cursor.close()
conn.close()
``