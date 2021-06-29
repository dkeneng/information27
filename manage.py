import logging

from info import create_app

app = create_app("development")


@app.route('/')
def index():
    # session["name"] = "cehsi"
    # session["password"] = "qwerdfhkhkhkjsd"

    # 测试打印日志
    logging.debug("测试 debug")
    logging.warning("测试 warning")
    logging.error("测试 error")
    logging.fatal("测试 fatal")
    return "index"


if __name__ == '__main__':
    app.run()