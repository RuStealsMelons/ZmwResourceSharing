import pymysql

from models.connect import connectdb


def save_img(name, data):
    db = connectdb()
    cursor = db.cursor()
    try:
        sql = "INSERT INTO imgs (name, data) VALUES (%s, %s)"
        cursor.execute(sql, (name, data))
        db.commit()
    except pymysql.Error as err:
        print(err)
    finally:
        cursor.close()
        db.close()

def load_img(name):
    db = connectdb()
    cursor = db.cursor()
    try:
        sql = f"SELECT data FROM `imgs` WHERE name='{name}'"
        cursor.execute(sql)
        db.commit()
        result = cursor.fetchone()
        return result[0]
    except pymysql.Error as err:
        print(err)
    finally:
        cursor.close()
        db.close()
