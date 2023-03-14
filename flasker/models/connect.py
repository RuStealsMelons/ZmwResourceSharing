import pymysql
import config

def connectdb():
    db = pymysql.connect(host=config.HOSTNAME, user=config.USERNAME, passwd=config.PASSWORD, port=int(config.PORT),
                         database=config.DATABASE)
    return db


if __name__ == '__main__':
    db = connectdb()
    cursor = db.cursor()
    try:
        sql = f"SELECT * FROM ZmwResourceSharing.users WHERE ZmwResourceSharing.users.username='123123'"
        res = cursor.execute(sql)
        db.commit()
        print(res)
    except pymysql.Error as err:
        print(err)
    finally:
        cursor.close()
        db.close()
