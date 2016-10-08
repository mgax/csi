import sys
import subprocess
import yaml
import flask
import waitress

class Route:

    def __init__(self, raw_spec, options):
        self.name = raw_spec
        (self.method, self.url) = raw_spec.split(None, 1)
        self.command = options['command']

    def register_on(self, app):
        @app.route(self.url, methods=[self.method], endpoint=self.name)
        def view():
            out = subprocess.check_output(self.command, shell=True)
            return out

class Configuration:

    def __init__(self, filename):
        with open(filename, 'rt', encoding='utf-8') as f:
            data = yaml.load(f)
        (self.host, port) = data.get('listen', 'localhost:8000').split(':')
        self.port = int(port)
        self.routes = [
            Route(raw_spec, options)
            for raw_spec, options in data.get('routes', {}).items()
        ]

def runserver(config_path):
    config = Configuration(config_path)
    app = flask.Flask(__name__)
    for route in config.routes:
        route.register_on(app)
    waitress.serve(app, host=config.host, port=config.port)

if __name__ == '__main__':
    runserver(sys.argv[1])
