import tornado.web
import tornado.ioloop
import tornado.httpserver
import tornado.options

class IndexHandler(tornado.web.RequestHandler):
    '''
    类比diango中的视图
    '''

    def get(self, *args, **kwargs):
        self.write('hello tornado!')

    def post(self, *args, **kwargs):
        pass


def main():
    app = tornado.web.Application([(r'/', IndexHandler)])
    tornado.options.parse_config_file('config')

    # app.listen(8000)
    http_server = tornado.httpserver.HTTPServer(app)
      # 将服务器绑定到指定的端口
    # 消灭硬编码
    # http_server.bind(5000)
    tornado.options.define('port', default=8000, type=int)
    http_server.bind(tornado.options.options.port)
    # 开启的进程数目，值为None或者小于0 默认开启cpu核心数目
    http_server.start(5)

    tornado.ioloop.IOLoop.current().start()


if __name__ == '__main__':
    main()