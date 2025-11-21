from .dashboard import dashboard_bp
from .students import students_bp
from .auth import auth_bp
from .courses import courses_bp


def register_routes(app):
    app.register_blueprint(dashboard_bp)
    app.register_blueprint(students_bp)
    app.register_blueprint(auth_bp)
    app.register_blueprint(courses_bp)
    