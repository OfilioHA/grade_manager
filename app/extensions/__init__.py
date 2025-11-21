from .alchemy import extension_alchemy
from .login import extension_login
from .turbo import extension_turbo

def register_extensions(app):
    extension_alchemy(app)
    extension_login(app)
    extension_turbo(app)