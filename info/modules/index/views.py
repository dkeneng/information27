from flask import render_template, current_app

from . import index_blu
from info import redis_store


@index_blu.route("/")
def index():
    # # 将session缓存到redis中
    # session["name"] = "cehsi"
    # session["password"] = "qwerdfhkhkhkjsd"

    # 测试打印日志
    # logging.debug("测试 debug")
    # logging.warning("测试 warning")
    # logging.error("测试 error")
    # logging.fatal("测试 fatal")

    # # 向redis中保存一个值
    # redis_store.set("name", "hahahah")
    # redis_store.set("name1", "aaaaaa")
    # redis_store.set("name2", "zzzzzz")
    # redis_store.set("name4", "cccccc")
    return render_template('news/index.html')
    # return "index"


# 在打开网页的时候，浏览器会默认去请求根路径+favicon.ico作为网站的小图标
# send_static_file是flask查找指定的静态文件所调用的方法
@index_blu.route('/favicon.ico')
def favicon():
    # print(__name__)
    # 查看当前应用的根路径
    # print(current_app.root_path)
    return current_app.send_static_file('news/favicon.ico')