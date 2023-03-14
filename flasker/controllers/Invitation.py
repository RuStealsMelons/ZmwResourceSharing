import random
import requests
import time
import hashlib
import json
from flask import Blueprint, jsonify
from models.Invitation import insertOneInvitation, selectAllInvitation, selectUsedInvitation, selectUnUsedInvitation, \
    exportALLUnUsedInvitation, exportSomeUnUsedInvitation

nums = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
ens = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V',
       'W', 'X', 'Y', 'Z']

generate = Blueprint('generateGenerations', __name__)

"""
生成一个验证码
"""


def CaptchaOneGeneration():
    code = ''.join(random.sample(ens, 5)) + "-" + ''.join(random.sample(nums, 5))
    hash_object = hashlib.md5(code.encode())
    md5_hash = hash_object.hexdigest()
    return code + "-" + md5_hash[:6]


# 请求爱发电 验证码是否付款 TODO
def requestCheckGeneration():
    user_id = "c05fafd889cf11edbf8b52540025c377"
    token = "CNDJp75UySnxHsRTc3uVgEmBb6XQYfAW"
    ts = int(time.time())
    params = {"page": 1}
    code = token + f'params{json.dumps(params).replace(" ", "")}' + f'ts{ts}' + f'user_id{user_id}'
    hash_object = hashlib.md5(code.encode())
    sign = hash_object.hexdigest()

    data = {"user_id": user_id, "params": json.dumps(params).replace(" ", ""), "ts": ts, "sign": sign}

    re = requests.post("https://afdian.net/api/open/query-sponsor", data=data)
    print(re.content.decode("utf-8"))
    print(code)
    print(sign)


"""
生成length个验证码
"""


@generate.route('/Generate/<length>', methods=['GET'])
def GenerateGenerations(length):
    for i in range(0, int(length)):
        code = CaptchaOneGeneration()
        insertOneInvitation(code)
    return {"success": True, "mess": f"已成功生成{length}个邀请码！"}


def MapInvitation(invitation):
    data = {
        "Invitation_id": invitation[0],
        "Invitation_code": invitation[1],
        "create_time": invitation[2],
        "use_time": invitation[3],
        "user_name": invitation[4],
    }
    if data["create_time"] is not None:
        data["create_time"] = data["create_time"].strftime("%Y-%m-%d %H:%M:%S")
    if data["use_time"] is not None:
        data["use_time"] = data["use_time"].strftime("%Y-%m-%d %H:%M:%S")
    return data


"""
查询邀请码使用情况
"""


@generate.route('/Invitation/<used>/<page>/<limit>', methods=['GET'])
def invitationUsed(used, page, limit):
    page, limit = int(page), int(limit)
    data = []
    length = 0
    offset = (page - 1) * limit
    if used == "all":
        data, length = selectAllInvitation(offset, limit)
    elif used == "used":
        data, length = selectUsedInvitation(offset, limit)
    elif used == "unused":
        data, length = selectUnUsedInvitation(offset, limit)

    data = list(map(MapInvitation, data))
    print(data)
    return {
        "success": True,
        "length": length,
        "data": data
    }


"""
查询邀请码使用情况
"""


@generate.route('/export/<length>', methods=['GET'])
def exportInvitation(length):
    length = int(length)
    if (length <= 0):
        data = exportALLUnUsedInvitation()
    else:
        data = exportSomeUnUsedInvitation(length)
    s = ""
    for it in data:
        s += it[0] + "\n"
    return {
        "success": True,
        "data": s
    }
