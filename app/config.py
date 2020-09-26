import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())


class Config:
    DEBUG = False
    TESTING = False
    JSON_SORT_KEYS = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_RECORD_QUERIES = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URI')


class DevelopmentConfig(Config):
    DEBUG = True
    JSON_SORT_KEYS = True


class ProductionConfig(Config):
    pass


env_app = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
}