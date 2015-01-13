import os

BASEDIR = os.path.abspath(os.path.dirname(__file__))

# Project
# -------

TITLE = 'MEMEX EXPLORER'
ADMINS = []

# Server
# ------

HOST = '0.0.0.0'
PORT = 5000
DEBUG = True
SECRET_KEY = 'some_secret'

# Database
# --------

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(BASEDIR, 'resources/app.db')
SQLALCHEMY_MIGRATE_REPO = os.path.join(BASEDIR, 'db_repository')

# Email
# -----

MAIL_SERVER = 'smtp.gmail.com'
MAIL_PORT = 465
MAIL_USE_TLS = False
MAIL_USE_SSL = True
MAIL_USERNAME = ''
MAIL_PASSWORD = ''
MAIL_DEBUG = True
DEFAULT_MAIL_SENDER = MAIL_USERNAME


# Crawlers Path
# -------------

SEED_FILES = os.path.join(BASEDIR, 'resources/seeds/')
MODEL_FILES = os.path.join(BASEDIR, 'resources/models/')
CONFIG_FILES = os.path.join(BASEDIR, 'resources/configs/')
# Temporal location of libs/profiles
LANG_DETECT_PATH = os.path.join(BASEDIR, 'profiles/')

CRAWLS_PATH = os.path.join(BASEDIR, 'resources/crawls/')

IMAGE_SPACE_PATH= os.path.join(BASEDIR, 'resources/image_space/')

UPLOAD_DIR = os.path.join(IMAGE_SPACE_PATH, 'uploaded_images/')

ALLOWED_EXTENSIONS = set(('txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'))
