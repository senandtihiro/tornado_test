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

