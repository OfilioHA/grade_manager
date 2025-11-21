from turbo_flask import Turbo

turbo = Turbo()

def extension_turbo(app):
    turbo.init_app(app)
    return app