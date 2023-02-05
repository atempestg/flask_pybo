from pybo.config.default import *

SQLALCHEMY_DATABASE_URI = 'sqlite:///{}'.format(os.path.join(BASE_DIR, 'pybo.db'))
SQLALCHEMY_TRACK_MODIFICATIONS = False
SECRET_KEY = "b'n4\x0c\x137{GHR\xed\x9b\xedk\x18\x9f\x08'"
