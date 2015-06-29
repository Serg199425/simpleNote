import tornado
from sockjs.tornado import SockJSRouter
import tornadio2 as tornadio
from django.core.management.base import NoArgsCommand

from websocket_server.socket_server import Connection


class Command(NoArgsCommand):
    def handle_noargs(self, **options):
        router = SockJSRouter(Connection, '/update_notifications')
        app = tornado.web.Application(router.urls)
        app.listen(8989)
        tornado.ioloop.IOLoop.instance().start()