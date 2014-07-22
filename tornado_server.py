import tornado.httpserver
import tornado.websocket
import tornado.ioloop
import tornado.web
from commands import parse
 
class WSHandler(tornado.websocket.WebSocketHandler):
    def open(self):
        print 'new connection'
        self.set_nodelay(True)
        self.write_message(u"By what name do you wish to be mourned?")

      
    def on_message(self, message):
        print 'message received %s' % message
        self.write_message(u"swag"+parse(message))
        self.write_message(u"prompt stuff wdwdwdwd")
        #self.write_message(parse(message))

 
    def on_close(self):
      print 'connection closed'
 
 
application = tornado.web.Application([
    (r'/ws', WSHandler),
])


if __name__ == "__main__":
    http_server = tornado.httpserver.HTTPServer(application)
    http_server.listen(50000)
    tornado.ioloop.IOLoop.instance().start()
