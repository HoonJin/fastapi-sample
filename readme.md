## Run command
```uvicorn main:app --reload```

## Install
### mac os
```LDFLAGS=-L/usr/local/opt/openssl/lib pip install mysqlclient```

참고: https://stackoverflow.com/questions/1857861/libmysqlclient15-dev-on-macs

### ubuntu
```sudo apt-get install libmysqlclient-dev```

### windows
라이브러리 지원이 안되니 하지 말것