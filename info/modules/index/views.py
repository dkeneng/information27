from flask import render_template, current_app, session, request, jsonify

from . import index_blu
from info import redis_store, constants
from ...models import User, News, Category
from ...utils.response_code import RET


@index_blu.route("/")
def index():
    """
    显示首页
    1、如果用户已经登录，将当前登录用户的数据传到模板中，供模板显示
    :return:
    """
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

    # 显示用户是否登录逻辑
    # 取到用户id
    user_id = session.get("user_id", None)
    user = None
    if user_id:
        # 查询用户的模型
        try:
            user = User.query.get(user_id)
        except Exception as e:
            current_app.logger.error(e)

    # 右侧的新闻排行的逻辑
    news_list = []
    try:
        news_list = News.query.order_by(News.clicks.desc()).limit(constants.CLICK_RANK_MAX_NEWS)
    except Exception as e:
        current_app.logger.error(e)

    # 定义一个空的字典列表，里面装的就是字典
    news_dict_li = []
    # 遍历对象列表，将对象的字典添加到字典列表中
    for news in news_list:
        news_dict_li.append(news.to_basic_dict())
    # print(news_dict_li)

    # 查询分类数据，通过模板的形式渲染出来
    categories = Category.query.all()

    category_li = []
    for category in categories:
        category_li.append(category.to_dict())

    data = {
        "user": user.to_dict() if user else None,
        "news_dict_li": news_dict_li,
        "category_li": category_li
    }
    # print(data)
    return render_template('news/index.html', data=data)
    # return "index"


# 在打开网页的时候，浏览器会默认去请求根路径+favicon.ico作为网站的小图标
# send_static_file是flask查找指定的静态文件所调用的方法
@index_blu.route('/favicon.ico')
def favicon():
    # print(__name__)
    # 查看当前应用的根路径
    # print(current_app.root_path)
    return current_app.send_static_file('news/favicon.ico')


@index_blu.route('/news_list')
def news_list():
    """
    获取首页新闻数据
    :return:
    """
    # 1、获取参数
    # 新闻的分类id
    cid = request.args.get("cid", "1")
    page = request.args.get("page", "1")
    per_page = request.args.get("per_page", "10")

    # 2、校验参数
    try:
        cid = int(cid)
        page = int(page)
        per_page = int(per_page)
    except Exception as e:
        current_app.logger.error(e)
        return jsonify(errno=RET.PARAMERR, errmsg="参数错误")

    filters = [News.status == 0]
    if cid != 1:
        filters.append(News.category_id == cid)

    # 查询数据
    try:
        paginate = News.query.filter(*filters).order_by(News.create_time.desc()).paginate(page, per_page, False)
    except Exception as e:
        current_app.logger.error(e)
        return jsonify(errno=RET.DBERR, errmsg="数据查询错误")

    # 取到当前页的数据
    news_model_list = paginate.items  # 模型对象列表
    total_page = paginate.pages
    current_page = paginate.page

    # 将模型对象列表转成字典列表
    news_dict_li = []
    for news in news_model_list:
        news_dict_li.append(news.to_basic_dict())

    data = {
        "total_page": total_page,
        "current_page": current_page,
        "news_dict_li": news_dict_li
    }

    return jsonify(errno=RET.OK, errmsg="OK", data=data)