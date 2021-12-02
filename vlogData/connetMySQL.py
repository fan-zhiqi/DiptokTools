import pymysql

def read_data():
    conn = pymysql.connect(host="193.112.224.186",port=3306, user="root", password="Wwzaixian2019.", db="flo")
    cur = conn.cursor()
    sql = "SELECT id from moment  WHERE audit_status = 1"
    cur.execute(sql)
    a=cur.fetchall()

    conn.close()

    c = []
    for i in a:
        b=list(i)
        c+=b

    return c


if __name__ == '__main__':
    print(read_data())


