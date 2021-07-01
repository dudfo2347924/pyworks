import sqlite3

def getconn():
    conn = sqlite3.connect("c:/pydb/mydb.db")
    return conn

# mydb.db에 연결하는 함수 - getconn


