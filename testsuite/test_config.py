from csi import Configuration

def test_listen(tmpdir):
    config_yaml = tmpdir / 'config.yaml'
    config_yaml.write("listen: localhost:8000\n")
    config = Configuration(str(config_yaml))
    assert config.host == 'localhost'
    assert config.port == 8000
