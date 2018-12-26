import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'hard to guess string'
    SQLALCHEMY_COMMIT_ON_TEARDOWN =True
    MAIL_SERVER = os.environ.get('MAIL_SERVER', 'smtp.qq.com')
    #MAIL_PORT = int(os.environ.get('MAIL_PORT', '587'))
    MAIL_PORT= 587
    MAIL_USE_TLS = os.environ.get('MAIL_USE_TLS','True').lower() in ['true', 'on', '1']
    MAIL_USE_SSL = False
    FLASKY_MAIL_SUBJECT_PREFIX = '[Flasky]'
    FLASKY_MAIL_SENDER = 'Flasky Admin <1306237818@qq.com>'
    #FLASKY_ADMIN = os.environ.get('FLASKY_ADMIN')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    #MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    #MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    MAIL_USERNAME='1306237818@qq.com'
    MAIL_PASSWORD='ktvivyntvmfnbafb'
    FLASKY_ADMIN='1306237818@qq.com'

    @staticmethod
    def init_app(app):
        pass

class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir,'data-dev.sqlite')
class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI =os.environ.get('TEST_DATABASE_URL') or \
        'sqlite://'

class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI =os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir,'data.sqlite')

config = {
    'development':DevelopmentConfig,
    'testing':TestingConfig,
    'production':ProductionConfig,
    'default':DevelopmentConfig

}
