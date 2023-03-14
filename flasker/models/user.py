import datetime

import pymysql

from models.connect import connectdb


def delete_failure(username):
    db = connectdb()
    cursor = db.cursor()
    try:
        sql = f"""
        UPDATE users SET try_times = 0 where username='{username}';
        """
        cursor.execute(sql)
        db.commit()
    except pymysql.Error as err:
        print(err)
    finally:
        cursor.close()
        db.close()

def failure_login(username):
    db = connectdb()
    cursor = db.cursor()
    try:
        sql = f"""
        UPDATE users SET try_times = try_times + 1 where username='{username}';
        """
        cursor.execute(sql)
        db.commit()
    except pymysql.Error as err:
        print(err)
    finally:
        cursor.close()
        db.close()

# 查询某个用户的具体信息
def select_user(username):
    db = connectdb()
    cursor = db.cursor()
    try:
        sql = f"""
        SELECT
            user_id,
            username,
            PASSWORD,
            token,
            token_time_out,
            try_times,
            Invitation_code,
            create_at,
            role 
        FROM
            users 
        WHERE
            username = '{username}' 
            AND
            delete_time IS NULL;
        """
        cursor.execute(sql)
        db.commit()
        return cursor.fetchall()
    except pymysql.Error as err:
        print(err)
    finally:
        cursor.close()
        db.close()


# 检查username用户是否存在
def check_user(username):
    db = connectdb()
    cursor = db.cursor()
    try:
        sql = f"SELECT * FROM users WHERE username='{username}'"
        print(sql)
        res = cursor.execute(sql)
        db.commit()
        return res
    except pymysql.Error as err:
        print(err)
    finally:
        cursor.close()
        db.close()


# 向User表注册一个用户
def register_user(username, password, invitation):
    db = connectdb()
    cursor = db.cursor()
    try:
        sql = f"INSERT INTO users (username, password, Invitation_code, create_at, try_times) VALUES('{username}', '{password}', '{invitation}', '{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}', 0)"
        res = cursor.execute(sql)
        db.commit()
        return res
    except pymysql.Error as err:
        print(err)
    finally:
        cursor.close()
        db.close()