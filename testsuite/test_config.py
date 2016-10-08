from tempfile import NamedTemporaryFile
from csi import Configuration

def parse_config(config_yaml):
    with NamedTemporaryFile() as tmp:
        tmp.write(config_yaml.encode('utf-8'))
        tmp.flush()
        tmp.seek(0)
        return Configuration(tmp.name)

def test_listen():
    config = parse_config("listen: localhost:8000\n")
    assert config.host == 'localhost'
    assert config.port == 8000
