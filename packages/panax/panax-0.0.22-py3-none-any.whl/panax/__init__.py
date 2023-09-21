import sys
import os
sys.path.append(os.getcwd())

import config.db
# from models import url_config

from wsgiref.simple_server import make_server
from panax.request import Request
from panax.panax_views.auto_view import auto_config


from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
# from sqlalchemy import Column, String, Integer


db = config.db.conn
engine = create_engine(db)
Base = declarative_base(engine)


urls = []
url_map = {}

# url_map = {
#     "users": {
#         "get": handler,
#         "post": handler
#     }
# }


request = Request()


# def url_match(route_url, req):
#     if route_url.endswith('}'):
#         route_path = route_url.rsplit('/', 1)[0]
#         route_param = route_url.rsplit('/', 1)[1].replace('{', '').replace('}', '')
#
#         req_path = req.rsplit('/', 1)[0]
#         req_param = req.rsplit('/', 1)[-1]
#
#         return route_path == req_path, {route_param: int(req_param)}
#     else:
#         return route_url == req, {}


def run_server(environ, star_response):
    star_response('200 OK', [('Content-Type', 'application/json;charset=urf-8')])
    request_path = environ['PATH_INFO'].replace('/api', '')
    # request_method = environ.get('REQUEST_METHOD', 'GET').upper()
    arr_path = str(request_path).split('/')
    # 资源
    path_resource = arr_path[1]
    # 方法
    path_operation = arr_path[2]
    # 参数
    path_param = int(arr_path[3]) if len(arr_path) == 4 else None

    # 请求地址 在url_map 中 已注册
    if path_resource in url_map:
        if path_operation in url_map[path_resource]:
            func = url_map[path_resource][path_operation]
            param = { "pk": path_param } if path_param is not None else {}

            request.bind(environ)
            response = str(func(request, **param)).encode('utf-8')
            return [response, ]
    else:
        if path_operation in auto_config:
            func = auto_config[path_operation]
            param = { "pk": path_param } if path_param is not None else {}

            request.bind(environ)
            response = str(func(request, path_resource, **param)).encode('utf-8')
            return [response, ]
        else:
            response = str({"code": 404, "msg": "Not Found!"}).encode('utf-8')
            return [response, ]


def route(resource, operation, method=['POST']):
    def wrapper(handler):
        if resource not in url_map:
            url_map[resource] = {}
        # url_map[resource][operation] = {
        #     "method": method,
        #     "handler": handler
        # }
        url_map[resource][operation] = handler
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
