# Common Script Interface

CSI is a web server modelled after the concept of [CGI
scripts](https://en.wikipedia.org/wiki/Common_Gateway_Interface). You can
configure URL endpoints that, when accessed, invoke a program.

```yaml
# config.yaml
listen: localhost:8000
routes:
  GET /now:
    command: date
```

```shell
$ csi config.yaml &
[1] 61036
$ curl localhost:8000/now
Sat Oct  8 01:01:46 EEST 2016
```
