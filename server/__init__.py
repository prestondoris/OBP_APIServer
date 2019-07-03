import logging
from flask import Flask, current_app, redirect, url_for

def create_app(config, debug=false, testing = false, config_overrides=None):
    app = Flask(__name__)
    app.config.from_object(config)

    app.debug = debug
    app.testing = testing
    
    if config_overrides:
        app.config.update(config_overrides)

    if not app.testing:
        logging.basicConfig(level=logging.INFO)

    with app.app_context():
        model = get_model()
        model.init_app(app)
        
    from blueprints.income_crud import crud
    app.register_blueprint('income_crud', url_prefix='/api/income')
    

    @app.route('/')
    def index():
        return 
    
    @app.errorhandler(500)
    def server_error(e):
        return """
        An internal error occurred: <pre>{}</pre>
        See logs for full stacktrace.
        """.format(e), 500
    
    return app

def get_model():
    from . import model
    model = Model
    return model