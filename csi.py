import yaml

class Configuration:

    def __init__(self, filename):
        with open(filename, 'rt', encoding='utf-8') as f:
            data = yaml.load(f)
        (self.host, port) = data['listen'].split(':')
        self.port = int(port)
