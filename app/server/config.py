import os
basedir = os.path.abspath(os.path.dirname(__file__))

class BaseConfig(object):
    """Base configuration."""
    SECRET_KEY = 'mysupersecret'
    DEBUG = False
    BCRYPT_LOG_ROUNDS = 13
    WTF_CSRF_ENABLED = True
    DEBUG_TB_ENABLED = False
    DEBUG_TB_INTERCEPT_REDIRECTS = False

class DevelopmentConfig(BaseConfig):
    """Development configuration."""
    DEBUG = True
    BCRYPT_LOG_ROUNDS = 4
    WTF_CSRF_ENABLED = False
    DYNAMODB_HOST = 'localhost' # if set, overrides AWS_REGION
    DYNAMODB_PORT = 8000
    AWS_REGION = ''
    DEBUG_TB_ENABLED = True

class TestingConfig(BaseConfig):
    """Testing configuration."""
    DEBUG = True
    TESTING = True
    BCRYPT_LOG_ROUNDS = 4
    WTF_CSRF_ENABLED = False
    DYNAMODB_HOST = 'localhost' # if set, overrides AWS_REGION
    DYNAMODB_PORT = 8000
    AWS_REGION = ''
    DEBUG_TB_ENABLED = False
    PRESERVE_CONTEXT_ON_EXCEPTION = False

class ProductionConfig(BaseConfig):
    """Production configuration."""
    SECRET_KEY = 'mysupersecret'
    DEBUG = False
    DYNAMODB_HOST = 'localhost' # if set, overrides AWS_REGION
    DYNAMODB_PORT = 8000
    AWS_REGION = ''
    DEBUG_TB_ENABLED = False
