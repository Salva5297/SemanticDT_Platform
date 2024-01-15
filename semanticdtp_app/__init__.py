from flask import Flask
import sys
import secrets
sys.stdout.flush()


def create_app():
    app = Flask(__name__)

    app.config['SECRET_KEY'] = '3ed554768ed1ccf065f80979d1840f2d' #secrets.token_hex(16)

    from .blueprints.shutdown import shutdown as shutdown_blueprint
    app.register_blueprint(shutdown_blueprint)



    return app