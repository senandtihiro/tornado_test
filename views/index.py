import tornado.web
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