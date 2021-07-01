# 특정한 회원 검색하기
from libs.db.dbconn import getconn

def select_one(num):
    conn = getconn()
    cur = conn.cursor()
    # 1명 검색 sql
    sql = "select * from member where name='장금이'"
    cur.execute(sql)
    print("이름으로 검색")
    rs = cur.fetchmany()
    '''
    for i in rs:
        print(i)
    '''
    print(rs)
    conn.close()

if __name__ == "__main__" :
    select_one(1)