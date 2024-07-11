from flask import Flask
from flask_migrate import Migrate

from routes.authRoute import auth
from routes.taskRoute import task

from config import db,SECRET_KEY

app = Flask(__name__)

app.config.from_object('config')
app.secret_key = SECRET_KEY

db.init_app(app)
migrate = Migrate(app, db)

app.register_blueprint(auth,url_prefix='/auth')
app.register_blueprint(task,url_prefix='/')


if __name__ == '__main__':
     app.run(debug=True)

