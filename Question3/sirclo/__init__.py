from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate, MigrateCommand
from sirclo.config import Config

app = Flask(__name__)
db = SQLAlchemy(app)

migrate = Migrate(app, db)

def create_app(configfile=None):
    app.config.from_object(Config)
    return app

from sirclo import routes

if __name__ == '__main__':
    create_app().run(debug=True,host='0.0.0.0')
