import tornado.web
from views import index
import config


class Application(tornado.web.Application):
    def __init__(self):
        handlers = [
            (r'/', index.IndexHandler),
            (r'/time_sleep', index.TimeSleepHandler),
            (r'/time_sleep_with_res', index.TimeSleepResHandler),
            (r'/param_transmit/(\w+)/(\w+)/(\w+)', index.ParamURIHandler),
            (r'/get_method', index.GetMethodHandler),
            (r'/post_method', index.PostMethodHandler),
            (r'/request_object', index.RequestObjHandler),
            (r'/file_upload', index.FileUploadHandler),
            (r'/home', index.HomeHandler),
            (r'/func', index.FuncHandler),
            (r'/stutents', index.StudentsHandler),
            (r'/cookie_count', index.CookieCountHandler),
            (r'/login', index.LoginHandler),
            (r'/async_request', index.AsyncRequestHandler),
            (r'/async_coroutine', index.AsyncCoroutineHandler),
        ]
        super(Application, self).__init__(handlers, **config.options)