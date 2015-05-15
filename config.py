from os.path import join, dirname, abspath

_cwd = dirname(abspath(__file__))


class BaseConfiguration(object):
    SECRET_KEY = 'a-new-secret-key-you-will-never-guess'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + join(_cwd, 'app.db')
    SQLALCHEMY_ECHO = True

    # TODO: change it on Twitter before making this public
    CONSUMER_KEY = 'vssrFVzwRTeEMOM6XisOa2CBO'
    CONSUMER_SECRET = 'h9edawqgC2lwQBxAb2TPRQek6p4ueZ2GrzD123tRQdDvFAtyO4'
    ACCESS_TOKEN = '2160721916-7LppGgEidL7Gdq5RrP42rPQ9iM6zy7VpmXlX6rb'
    ACCESS_TOKEN_SECRET = 'mu7l5stXre4OyYikZUen6TpEXG9FZkmzxgcs8sVL3jRIx'
    USE_ADMIN_INTERFACE = True
    BOOTSTRAP_SERVE_LOCAL = True
    USE_HOOK = True


class TestConfiguration(BaseConfiguration):
    TESTING = True
    WTF_CSRF_ENABLED = False
    USE_ADMIN_INTERFACE = False
    USE_HOOK = False
    SQLALCHEMY_ECHO = False
    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'
