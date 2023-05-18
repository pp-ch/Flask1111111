
SECRET_KEY = "asdfasdfjasdfjasd;lf"

# 数据库的配置信息
HOSTNAME = 'localhost'
PORT     = '3306'
DATABASE = 'tec9'
USERNAME = 'root'
PASSWORD = '214214'
DB_URI = 'mysql+pymysql://{}:{}@{}:{}/{}?charset=utf8'.format(USERNAME,PASSWORD,HOSTNAME,PORT,DATABASE)
SQLALCHEMY_DATABASE_URI = DB_URI


# 邮箱配置
MAIL_SERVER = "smtp.qq.com"
MAIL_USE_SSL = True
MAIL_PORT = 465
MAIL_USERNAME = "1214567382@qq.com"
MAIL_PASSWORD = "komkhbwvxumaihdh"
MAIL_DEFAULT_SENDER = "1214567382@qq.com"