import time

from flask import jsonify, current_app, request, Blueprint

from models.Invitation import checkInvitation, useInvitation
from models.user import check_user, register_user, select_user, failure_login, delete_failure
import base64
import hashlib
user = Blueprint('user', __name__)

def offset_str(s):
    res = ''
    for c in s:
        ascii_code = ord(c)  # 将字符转换成ASCII码
        offset_code = ascii_code - 10  # 偏移10
        offset_char = chr(offset_code)  # 将偏移后的ASCII码转换成字符
        res += offset_char
    return res


"""
登录
"""
@user.route('/login', methods=['POST'])
def login():
    if request.json is None:
        return {"success": False}
    username = request.json.get('username')
    password = request.json.get('password')
    ts = request.json.get('ts')
    if ts is None or ts == "" or int(offset_str(ts)) % 1000 == 0:
        return {"success": False, "mess": "请不要调试接口"}
    ts = int(offset_str(ts)) / 1000
    if time.time() - ts > 2*60:
        return {"success": False, "mess": "请求超时！"}
    db_res = select_user(username)
    if len(db_res) == 0:
        return {"success": False, "mess": "该账号不存在"}
    db_res = db_res[0]
    if password != db_res[2]:
        failure_login(username)
        return {"success": False, "mess": "密码错误"}
    if db_res[5] > 7:
        return {"success": False, "mess": "错误次数太多，请联系管理员！"}
    delete_failure(username)
    return {
        "username": username,
        "token": ts
    }
    # pass


def pad_key(key):
    missing_bytes = 16 - len(key) % 16
    return (key + bytes([missing_bytes] * missing_bytes).decode("utf-8")).encode("utf-8")

"""
注册
"""
@user.route('/register', methods=['POST'])
def register():
    if request.json is None:
        return {"success": False, "mess": "参数错误"}
    username = request.json.get('username')
    password = request.json.get('password')
    invitation = base64.b64decode(request.json.get('invitation')).decode('utf-8')

    if (len(username) < 1 or len(username) > 12) and (len(password) < 6 or len(password) > 12):
        return {"success": False, "mess": "账号或密码长度不符合要求"}

    if check_user(username) != 0:
        return {"success": False, "mess": "用户已经存在"}

    index = 0
    try:
        index = int(invitation[:3].lstrip("0"), 10)
    except Exception as err:
        return {"success": False, "mess": "验证码格式不符合要求！"}
    length = checkInvitation(index, invitation[4:])
    print(int(invitation[:3].lstrip("0"), 10), invitation[4:])
    if length == 0:
        return {"success": False, "mess": "邀请码错误"}

    useInvitation(int(invitation[:3].lstrip("0"), 10), invitation[4:], username)
    register_user(username, password, invitation)
    return {"success": True, "mess": f"注册成功，欢迎'{username}'加入我们！"}




