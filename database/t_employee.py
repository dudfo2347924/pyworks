from libs.db.dbconn import getconn

def select_emp():
    conn = getconn()
    cur = conn.cursor()
    #sql * select
    sql = "select * from employee"

    cur.execute(sql)
    rs = cur.fetchall()
    for i in rs:
        print(i)
    conn.close()

def select_one():
    conn = getconn()
    cur = conn.cursor()
    sql = "select * from employee where emp_id=?"
    cur.execute(sql, ('e101',))
    rs = cur.fetchone()
    print(rs)
    conn.commit()

def insert_emp():
    conn = getconn()
    cur = conn.cursor()
    sql = "insert into employee(emp_id, name, age, salary) values (?,?,?,?)"
    cur.execute(sql, ('e104','강산', 22, 5000))
    conn.commit()
    conn.close()

def insert_update():
    conn = getconn()
    cur = conn.cursor()
    sql = "update employee set salary=? where emp_id=?"
    cur.execute(sql,(25000, 'e102'))
    conn.commit()
    conn.close()

def insert_delete():
    conn = getconn()
    cur = conn.cursor()
    sql = "delete from employee where emp_id=?"
    cur.execute(sql,('e104',))
    conn.commit()
    conn.close()

insert_delete()
#insert_update()
#insert_emp()
select_emp()
#select_one()