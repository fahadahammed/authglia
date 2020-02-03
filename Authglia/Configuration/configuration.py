import os

if not os.path.exists('Logs'):
    os.makedirs('Logs')


LOGGING_CONFIG = {
    'version': 1,
    'formatters': {'default': {
        'format': '[%(asctime)s] %(levelname)s at %(threadName)s in %(module)s : %(message)s',
    }},
    'handlers': {
        'wsgi': {
            'class': 'logging.StreamHandler',
            'stream': 'ext://flask.logging.wsgi_errors_stream',
            'formatter': 'default'
        },
        'logfile': {
            'class': 'logging.FileHandler',
            'filename': 'Logs/logs.log',
            'formatter': 'default'
        }
    },
    'root': {
        'handlers': ['wsgi', 'logfile']
    }
}


class BaseConfig(object):
    PROTECTED_PATH = "ProtectedPath"
    THREADED = True

    ENV = 'dev'
    HOST = "127.0.0.1"
    PORT = 21433

    CACHE_TYPE = 'simple'

    # Database
    AUTHGLIA_DB_PORT = 27017
    AUTHGLIA_DB_HOST = "127.0.0.1"
    AUTHGLIA_DB_USER = "Authglia"
    AUTHGLIA_DB_PASSWORD = "Authglia"
    AUTHGLIA_DB_NAME = "Authglia"

    SECRET_KEY = "Yc30VUEQfSXtrbLazgFRDvvZb5dbEStjwyo8q12R"


class DevelopmentConfig(BaseConfig):
    DEBUG = True
    TESTING = True
    TEMPLATES_AUTO_RELOAD = True


class ProductionConfig(BaseConfig):
    DEBUG = False
    TESTING = False
    TEMPLATES_AUTO_RELOAD = False

    ENV = 'prod'

    CACHE_TYPE = 'redis'
    CACHE_REDIS_HOST = '127.0.0.1'
    CACHE_REDIS_PORT = 6379
    CACHE_REDIS_DB = '11'
    CACHE_KEY_PREFIX = '@Authglia'
    CACHE_DEFAULT_TIMEOUT = 43200


config = {
    "dev": "Authglia.Configuration.configuration.DevelopmentConfig",
    "prod": "Authglia.Configuration.configuration.ProductionConfig",
    "default": "Authglia.Configuration.configuration.DevelopmentConfig"
}


def configure_app(app):
    config_name = os.getenv('ENV', 'default')
    app.config.from_object(config[config_name])
