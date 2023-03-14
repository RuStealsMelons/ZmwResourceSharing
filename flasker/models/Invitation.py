import datetime

import pymysql

from models.connect import connectdb


# 向数据库插入一条邀请码
def insertOneInvitation(Invitation_code):
    db = connectdb()
    cursor = db.cursor()
    try:
        sql = f"insert into invitation (Invitation_code, create_time) value('{Invitation_code}', '{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}')"
        cursor.execute(sql)
        db.commit()
    except pymysql.Error as err:
        print(err)
    finally:
        cursor.close()
        db.close()


# 检查数据库中的邀请码存在且未被使用
def checkInvitation(id, Invitation_code):
    db = connectdb()
    cursor = db.cursor()
    try:
        sql = f"SELECT * FROM invitation WHERE use_time IS NULL AND  Invitation_id={id} AND Invitation_code='{Invitation_code}'"
        print(sql)
        res = cursor.execute(sql)
        db.commit()
        return res
    except pymysql.Error as err:
        print(err)
    finally:
        cursor.close()
        db.close()


# 更新 使用某个邀请码
def useInvitation(id, Invitation_code, username):
    db = connectdb()
    cursor = db.cursor()
    try:
        sql = f"UPDATE invitation SET use_time='{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}', user_name='{username}' WHERE use_time IS NULL AND  Invitation_id={id} AND Invitation_code='{Invitation_code}'"
        res = cursor.execute(sql)
        db.commit()
    except pymysql.Error as err:
        print(err)
    finally:
        cursor.close()
        db.close()

def selectAllInvitation(offset, length):
    db = connectdb()
    cursor = db.cursor()
    try:
        sql = f"SELECT * FROM invitation  LIMIT {offset}, {length};"
        cursor.execute(sql)
        db.commit()
        data = cursor.fetchall()

        sql = f"SELECT count(1) FROM invitation"
        cursor.execute(sql)
        length = cursor.fetchall()[0][0]
        db.commit()

        return data, length
    except pymysql.Error as err:
        print(err)
    finally:
        cursor.close()
        db.close()


def selectUsedInvitation(offset, length):
    db = connectdb()
    cursor = db.cursor()
    try:
        sql = f"SELECT * FROM invitation WHERE use_time IS NOT NULL  LIMIT {offset}, {length};"
        cursor.execute(sql)
        db.commit()
        data = cursor.fetchall()

        sql = f"SELECT count(1) FROM invitation WHERE use_time IS NOT NULL"
        cursor.execute(sql)
        length = cursor.fetchall()[0][0]
        db.commit()

        return data, length
    except pymysql.Error as err:
        print(err)
    finally:
        cursor.close()
        db.close()

def selectUnUsedInvitation(offset, length):
    db = connectdb()
    cursor = db.cursor()
    try:
        sql = f"SELECT * FROM invitation WHERE use_time IS NULL  LIMIT {offset}, {length};"
        cursor.execute(sql)
        db.commit()
        data = cursor.fetchall()

        sql = f"SELECT count(1) FROM invitation WHERE use_time IS NULL"
        cursor.execute(sql)
        length = cursor.fetchall()[0][0]
        db.commit()

        return data, length
    except pymysql.Error as err:
        print(err)
    finally:
        cursor.close()
        db.close()


def exportSomeUnUsedInvitation(length):
    db = connectdb()
    cursor = db.cursor()
    try:
        sql = f"SELECT CONCAT(LPAD(Invitation_id%1000, 3, '0'), '-',Invitation_code) as code FROM invitation WHERE use_time IS NULL  LIMIT {length}"
        cursor.execute(sql)
        db.commit()
        data = cursor.fetchall()
        return data
    except pymysql.Error as err:
        print(err)
    finally:
        cursor.close()
        db.close()

def exportALLUnUsedInvitation():
    db = connectdb()
    cursor = db.cursor()
    try:
        sql = f"SELECT CONCAT(LPAD(Invitation_id%1000, 3, '0'), '-',Invitation_code) as code FROM invitation WHERE use_time IS NULL  "
        cursor.execute(sql)
        db.commit()
        data = cursor.fetchall()
        return data
    except pymysql.Error as err:
        print(err)
    finally:
        cursor.close()
        db.close()