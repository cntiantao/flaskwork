import pymysql


def getMySqlConn(host='localhost', port=3306, user='root', passwd='root', db='lecar', charset='utf8'):
    return pymysql.Connect(host=host, port=port, user=user, passwd=passwd, db=db, charset=charset, cursorclass=pymysql.cursors.DictCursor)

def getConn():
    return getMySqlConn()




def getCursor():
    return getConn().cursor()


def queryAll(sql, args=None):
    conn = getConn()
    cursor = getConn().cursor()
    cursor.execute(sql, args)
    rs = cursor.fetchall()
    cursor.close()
    conn.close()
    return rs
