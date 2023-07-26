import mysql.connector
import requests
import json

def expireCheck():
    cnx = mysql.connector.connect(
        host='localhost',
        user='id',
        password='pwd@@',
        database='cm'
    )

    # 커서 객체 생성
    cursor = cnx.cursor(dictionary=True)

    # User 테이블에서 데이터 가져오기
    query = "SELECT * FROM TB_GROUP"
    cursor.execute(query)

    # 결과 출력
    rows = cursor.fetchall()
    print(rows)
    for row in rows:
        id = row["ID"]
        email = row["EMAIL"]
        print(str(id) + " " + email)
    # GET 요청 보내기
    response_get = requests.get('http://localhost:8080/main/index.jsp')
    print('GET response:', response_get.text)

    # POST 요청 보내기
    headers = {'Content-Type': 'application/json'}
    data = json.dumps({"key": "value"})  # 여기에 실제 데이터를 넣으세요
    response_post = requests.post('http://localhost:8080/main/index.jsp', headers=headers, data=data)
    print('POST response:', response_post.text)
