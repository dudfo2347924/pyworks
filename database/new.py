from libs.db.dbconn import getconn

def ():
    conn = getconn()
    cur = conn.cursor()

    sql = ""

    cur.execute(sql)

    conn.commit()
    conn.close()


if __name__ == "__main__":
    ()