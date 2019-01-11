import tornado.web
import tornado.ioloop
import tornado.httpserver
import config
from views.index import IndexHandler
from application import Application

def main():
    app = Application()

    # app.listen(8000)
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(config.options['port'])

    tornado.ioloop.IOLoop.current().start()


if __name__ == '__main__':
    main()