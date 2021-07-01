
from libs.db.dbconn import getconn

def select_data():
    conn = getconn()
    cur = conn.cursor()
    sql = "select  * from member"
    cur.execute(sql)

    print("데이터 전체 조회")
    rs = cur.fetchall() # 꺼내온 자료
    for i in rs:
        print(i)

        conn.close()

if __name__ == "__main__":
    select_data()
