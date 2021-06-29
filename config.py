import logging

import redis


class Config(object):
    """工程配置信息"""
    DEBUG = True
    SECRET_KEY = "iSVYsnWgmqtZDM7EgL+qI1UW44aQZCMyaOkBYqFdE6fsSNvWzhv4WQFCxixQ4KQa"

    # 数据库的配置信息
    SQLALCHEMY_DATABASE_URI = "mysql://root:qwerdf@127.0.0.1/information"
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # redis配置
    REDIS_HOST = "127.0.0.1"
    REDIS_PORT = 6379
    PASSWORD = "qwerdf"

    # flask_session的配置信息
    # 指定session保存到redis中
    SESSION_TYPE = "redis"
    # 让cookie 中的session_id被加密签名处理
    SESSION_USE_SIGNER = True
    # 使用redis的实例
    SESSION_REDIS = redis.StrictRedis(host=REDIS_HOST, port=REDIS_PORT, password=PASSWORD)
    # 设置需要过期
    SESSION_PERMANENT = False
    # 设置session过期时间，单位是秒
    PERMANENT_SESSION_LIFETIME = 86400 * 2

    # 设置日志等级
    LOG_LEVEL = logging.DEBUG


class DevelopmentConfig(Config):
    """开发环境下的配置"""
    DEBUG = True


class ProductionConfig(Config):
    """生产环境下的配置"""
    DEBUG = False
    LOG_LEVEL = logging.WARNING


config = {
    "development": DevelopmentConfig,
    "production": ProductionConfig
}