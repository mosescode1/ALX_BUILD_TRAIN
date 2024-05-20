from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///todo.db"
app.config["SECRET_KEY"] = '678892f9521e150a640b2342c771b43b'
db = SQLAlchemy()
db.init_app(app)
