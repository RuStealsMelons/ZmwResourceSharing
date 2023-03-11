import pymysql
import config


def connectdb():
    print("连接SQL服务器")
    db = pymysql.connect(host=config.HOSTNAME, user=config.USERNAME, passwd=config.PASSWORD, port=int(config.PORT))
    print("连接上了！")
    return db
