from time import time, sleep
from contextlib import contextmanager
import subprocess

CONFIG_YAML = """\
listen: localhost:14877
routes:
  GET /now:
    command: echo hello world
"""

def wait_for_url(url):
    t0 = time()
    while True:
        try:
            subprocess.check_call(['curl', '-s', url])
            return
        except subprocess.CalledProcessError:
            if time() - t0 < 3:
                sleep(.1)
            else:
                raise

@contextmanager
def server(config_yaml):
    p = subprocess.Popen(
        ['python', 'csi.py', str(config_yaml)],
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
    )
    wait_for_url('http://localhost:14877')

    try:
        yield

    finally:
        p.terminate()
        out, _ = p.communicate()
        print(out.decode('utf-8'))
        p.wait()

def test_serve(tmpdir):
    config_yaml = tmpdir / 'config.yaml'
    config_yaml.write(CONFIG_YAML)
    with server(config_yaml):
        url = 'http://localhost:14877/now'
        content = subprocess.check_output(['curl', '-s', url])
    assert content == b'hello world\n'
