from flask import Flask
from app.extensions import db, migrate, bcrypt, jwt
from app.models.student import student_blueprint
from app import create_app


def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')
    app.config['JWT_SECRET_KEY'] = '2003'

    db.init_app(app)
    migrate.init_app(app, db)
    bcrypt.init_app(app)
    jwt.init_app(app)

    from app.models.student import Student

    app.register_blueprint(student_blueprint, url_prefix='/api/v1/student')

    @app.route('/')
    def home():
        return "Hello programmers"

    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
