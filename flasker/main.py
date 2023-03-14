import os

from flask import Flask
from flask_cors import CORS
import logging
import config
from controllers.login import user
from controllers.Invitation import generate
from controllers.imgs import imgs
from models.connect import connectdb

# 自定义日志信息
logger = logging.getLogger()
logger.setLevel(logging.INFO)

# 建立一个file handler来把日志记录在文件里
file_handler = logging.FileHandler('logs/test.log', encoding="UTF-8")
# 设置日志格式
formatter = logging.Formatter("%(asctime)s - %(funcName)s - %(lineno)d - %(levelname)s - %(message)s")
file_handler.setFormatter(formatter)
# 将相应的handler添加在logger对象中
logger.addHandler(file_handler)

app = Flask(__name__)
CORS(app=app)

# 载入配置文件
app.config.from_object(config)
# 初始化数据库
connectdb()

# 载入蓝图
app.register_blueprint(user)
app.register_blueprint(generate)
app.register_blueprint(imgs)
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)

