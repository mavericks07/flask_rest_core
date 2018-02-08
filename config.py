from playhouse.db_url import connect


class Config(object):
    DEBUG = True
    DATABASE = 'mysql+pool://root:qw010203@localhost/flask_test?max_connections=100&stale_timeout=300'


class DevConfig(Config):
    DEBUG = True


class TestConfig(Config):
    DEBUG = False


class ProdConfig(Config):
    DEBUG = False


config = {
    'default': DevConfig,
    'dev': DevConfig,
    'test': TestConfig,
    'prod': ProdConfig
}
