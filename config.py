class Config:
    DEBUG = True

    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://username:password@localhost/database_name'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = 'super-secret-key'
    JWT_ERROR_MESSAGE_KEY = 'message'
    JWT_BLACKLIST_ENABLED = True
    JWT_BLACKLIST_TOKEN_CHECK = ['access', 'refresh']



