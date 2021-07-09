
import sqlite3

def getconn():
    conn = sqlite3.connect("c:/pydb/web_db.db")
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

def select_one():
    conn = getconn()
    cur = conn.cursor()

    sql = "SELECT * FROM t_book WHERE book_no=?"
    cur.execute(sql,(3,))

    rs = cur.fetchone()
    print(rs)

    conn.close()

def insert_book():
    conn = getconn()
    cur = conn.cursor()

    sql = "INSERT INTO t_book(title,publisher,page) VALUES (?,?,?)"
    cur.execute(sql, ('천개의 파랑','천선란',300))

    conn.commit()
    conn.close()

def update_book():
    conn = getconn()
    cur = conn.cursor()

    sql = "UPDATE t_book SET page = ? WHERE book_no=?"
    cur.execute(sql, (400,2))

    conn.commit()
    conn.close()

def delete_book():
    conn = getconn()
    cur = conn.cursor()

    sql = "DELETE FROM t_book WHERE book_no=?"
    cur.execute(sql, (4,))

    conn.commit()
    conn.close()

if __name__ == "__main__":
    #delete_book()
    #insert_book()
    #update_book()
    select_one()
    #select_book()