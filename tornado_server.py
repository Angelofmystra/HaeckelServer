import tornado.httpserver
import tornado.websocket
import tornado.ioloop
import tornado.web
from commands import parse

clients = {}
client_data = []

class WSHandler(tornado.websocket.WebSocketHandler):
    def open(self):
        print "[+] Someone has connected."
        self.set_nodelay(True)
        self.write_message(u"By what name do you wish to be mourned?")
        d = {}
        d["state"] = "unknown"
        clients[str(self)] = d

    def on_message(self, message):
        print 'message received %s' % message
        print "self: "+str(self)
        if "@" in message:
            self.write_message("Unacceptable input")
        else:
            if (clients[str(self)]["state"] == "unknown"):
                clients[str(self)]["username"] = message
                clients[str(self)]["state"] = "gave_username"
                self.write_message("Please give a password: ")
            elif (clients[str(self)]["state"] == "gave_username"):
                clients[str(self)]["password"] = message
                self.write_message("Pleaes confirm your password: ")
                clients[str(self)]["state"] = "confirm_password"
            elif (clients[str(self)]["state"] == "confirm_password"):
                if (clients[str(self)]["password"] == message):
                    clients[str(self)]["state"] = "logged_in"
                    print parse("@make_character")
                    self.write_message("Welcome to Haeckel!")
                    self.write_message(parse("look"))
                    self.write_message(parse("prompt"))
                else:
                    self.write_message("Password did not match.")
                    clients[str(self)]["password"] = ""
                    self.write_message("Please give a password: ")
                    clients[str(self)]["state"] = "gave_username"
            elif (clients[str(self)]["state"] == "logged_in"):
                self.write_message(parse(message))
                self.write_message(parse("prompt"))

    def on_close(self):
        print "[+] Connection has closed."


application = tornado.web.Application([
    (r'/ws', WSHandler),
])


if __name__ == "__main__":
    http_server = tornado.httpserver.HTTPServer(application)
    http_server.listen(50000)
    tornado.ioloop.IOLoop.instance().start()
