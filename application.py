import tornado.web
from views import index
import config


class Application(tornado.web.Application):
    def __init__(self):
        handlers = [
            (r'/', index.IndexHandler),
            (r'/param_transmit/(\w+)/(\w+)/(\w+)', index.ParamURIHandler),
            (r'/get_method', index.GetMethodHandler),
        ]
        super(Application, self).__init__(handlers, **config.options)