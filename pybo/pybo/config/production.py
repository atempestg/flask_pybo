from pybo.config.default import *
from logging.config import dictConfig

SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://{user}:{pw}@{url}/{db}'.format(
    user='dbmasteruser',
    pw='B4,:zYXMvbLvoz4NN[+|bX%?MQN]9ey0',
    url='ls-999e6dda53b69892e260293c6dc26d15bd14e505.cvkqqskmwouw.ap-northeast-2.rds.amazonaws.com',
    db='flask_pybo')
SQLALCHEMY_TRACK_MODIFICATIONS = False
SECRET_KEY = "b'n4\x0c\x137{GHR\xed\x9b\xedk\x18\x9f\x08'"

dictConfig({
    'version' : 1,
    'formatters' : {
        'default' : {
            'format' : '[%(asctime)s %(levelname)s in %(module)s: %(message)s',
        }
    },
    'handlers' : {
        'file' : {
            'level' : 'INFO',
            'class' : 'logging.handlers.RotatingFileHandler',
            'filename' : os.path.join(BASE_DIR, 'logs/myproject.log'),
            'maxBytes' : 1024 * 1024 * 5, # 5MB
            'backupCount' : 5,
            'formatter' : 'default',
        },
    },
    'root' : {
        'level' : 'INFO',
        'handlers' : ['file']
    }
})