from flask_sqlalchemy import SQLAlchemy
import os
db = SQLAlchemy()

SECRET_KEY = os.urandom(32)
SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:edaly20044@127.0.0.1:3306/tasks'
SQLALCHEMY_TRACK_MODIFICATION = False
