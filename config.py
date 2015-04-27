from os.path import join, dirname, abspath

_cwd = dirname(abspath(__file__))

SECRET_KEY = 'You will never guess'
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + join(_cwd, 'app.db')
SQLALCHEMY_ECHO = True