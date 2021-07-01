# 자료 수정하기

from libs.db.dbconn import getconn

def update_data():
    conn = getconn()
    cur = conn.cursor()
    sql = "update member set age = '18' where name ='엘사'"
    cur.execute(sql)

    conn.commit()
    conn.close()

if __name__ == "__main__":
    update_data()