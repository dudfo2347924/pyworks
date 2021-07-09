
import sqlite3

def getconn():
    conn = sqlite3.connect("test.db")
    return conn

def select_book():
    conn = getconn()
    cur = conn.cursor()

    sql = "SELECT * FROM t_book"

    cur.execute(sql)
    rs = cur.fetchall()
    for i in rs:
        print(i)

    conn.close()

def insert_book():
    conn = getconn()
    cur = conn.cursor()

    sql = "INSERT INTO t_book(title,publisher,page) VALUES (?,?,?)"
    cur.execute(sql, ('천개의 파랑','천선란',300))

    conn.commit()
    conn.close()


if __name__ == "__main__":
    insert_book()
    select_book()