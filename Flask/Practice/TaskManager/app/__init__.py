from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_migrate import Migrate


db = SQLAlchemy()
login_manager = LoginManager()

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'supersecretkey'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tasks.db'

    db.init_app(app)
    login_manager.init_app(app)
    login_manager.login_view = 'main.login'  # Redirect to login if user not authenticated

    from .routes import main
    app.register_blueprint(main)

    migrate = Migrate(app, db)

    with app.app_context():
        from .models import User, Task
        db.create_all()

    return app
