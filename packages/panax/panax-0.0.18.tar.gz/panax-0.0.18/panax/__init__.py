import sys
import os
sys.path.append(os.getcwd())

import config.db

from wsgiref.simple_server import make_server
from panax.request import Request


from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
# from sqlalchemy import Column, String, Integer


db = config.db.conn
engine = create_engine(db)
Base = declarative_base(engine)


urls = []


request = Request()


def run_server(environ, star_response):
    star_response('200 OK', [('Content-Type', 'text/html;charset=urf-8')])
    url = environ['PATH_INFO']
    func = None
    for i in urls:
        if i[0] == url:
            func = i[2]
            break
    if func:
        request.bind(environ)
        response = str(func(request)).encode('utf-8')
    else:
        response = str({"code": 404, "msg": "Not Found!"}).encode('utf-8')
    return [response, ]


def route(url, method=['GET', 'POST']):
    def wrapper(handler):
        urls.append([url, method, handler])
        return handler

    return wrapper


def run(host='127.0.0.1', port=8000, **kwargs):
    '''
    启动监听服务
    '''
    httpd = make_server(host, port, run_server)
    print('Courage server starting up ...')
    print('Listening on http://%s:%d/' % (host, port))
    print('Use Ctrl-C to quit.')
    print('')
    httpd.serve_forever()
