import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'change-me'
    
    DATABASE = os.path.join(basedir, 'booking.db')

    MAIL_SERVER ='sandbox.smtp.mailtrap.io'
    MAIL_PORT = 2525
    MAIL_USERNAME = '42fc145fb36e3d'
    MAIL_PASSWORD = '89be663209d6a1'
    MAIL_USE_TLS = True
    MAIL_USE_SSL = False
    MAIL_DEFAULT_SENDER = MAIL_USERNAME
