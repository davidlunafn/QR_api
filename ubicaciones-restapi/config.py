class Config:
    pass

class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:gameover1024@localhost:5432/ubicaciones'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    PASSWORD = 'gameover1024'

config = {
    'development': DevelopmentConfig,
}