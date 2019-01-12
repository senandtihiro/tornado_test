import tornado.web
import os
import config
from tornado.web import RequestHandler

class IndexHandler(RequestHandler):
    '''
    类比diango中的视图
    '''
    def get(self, *args, **kwargs):
        self.write('hello tornado!')

    def post(self, *args, **kwargs):
        pass


class ParamURIHandler(RequestHandler):
    '''
    类比diango中的视图
    当请求的URI为 r'/param_transmit/p1/p2/p3'的时候
    '''
    def get(self, param1, param2, param3, *args, **kwargs):
        print('debug ParamURIHandler params:', param1, param2, param3)
        self.write('hello tornado paramURIHandler!')

    def post(self, *args, **kwargs):
        pass


class GetMethodHandler(RequestHandler):
    '''
    类比diango中的视图
    当请求的URI为 r'/get_method?a=1&b=2&c=3'的时候
    '''
    def get(self, *args, **kwargs):
        a = self.get_query_argument('a')
        b = self.get_query_argument('b')
        c = self.get_query_argument('c')
        # 获取同名参数值的列表
        d = self.get_query_arguments('c')
        print('debug GetMethodHandler params:', a, b, c)
        self.write('hello tornado GetMethodHandler!')

    def post(self, *args, **kwargs):
        pass


class PostMethodHandler(RequestHandler):
    '''
    类比diango中的视图
    当请求的URI为 r'/get_method?a=1&b=2&c=3'的时候
    '''
    def get(self, *args, **kwargs):
        self.render('post_file.html')

    def post(self, *args, **kwargs):
        username = self.get_body_argument('username')
        password = self.get_body_argument('password')
        print('debug username and password', username, password)


class RequestObjHandler(RequestHandler):
    '''
    GET
    localhost:8000
    /request_object
    /request_object

    HTTP/1.1
    Host: localhost:8000
    Upgrade-Insecure-Requests: 1
    User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36
    Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8
    Accept-Encoding: gzip, deflate, br
    Accept-Language: zh-CN,zh;q=0.9,en;q=0.8
    Connection: keep-alive

    b''
    ::1
    {}
    '''
    def get(self, *args, **kwargs):
        print(self.request.method)
        print(self.request.host)
        print(self.request.uri)
        print(self.request.path)
        print(self.request.query)
        print(self.request.version)
        print(self.request.headers)
        print(self.request.body)
        print(self.request.remote_ip)
        print(self.request.files)
        self.write('request object attributes')


class FileUploadHandler(RequestHandler):
    '''
    类比diango中的视图
    当请求的URI为 r'/get_method?a=1&b=2&c=3'的时候
    '''
    def get(self, *args, **kwargs):
        self.render('post_file.html')

    def post(self, *args, **kwargs):
        files = self.request.files
        for file_name in files:
            file_list = files[file_name]
            for file in file_list:
                file_path = os.path.join(config.BASE_DIRS, 'upfile/' + file.filename)
                with open(file_path, 'wb') as f:
                    f.write(file.body)
        self.write('upload files ok')