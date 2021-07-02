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

    # 向redis中保存一个值
    redis_store.set("name", "hahahah")
    redis_store.set("name1", "aaaaaa")
    redis_store.set("name2", "zzzzzz")
    redis_store.set("name4", "cccccc")
    return "index"