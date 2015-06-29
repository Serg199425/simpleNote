import tornado
import tornadoredis
from sockjs.tornado import SockJSConnection
import django
from django.utils.importlib import import_module
from django.conf import settings
from groups.models import GroupUser
from note.models import Note
import json as simplejson
_engine = import_module(settings.SESSION_ENGINE)
import time
from IPython import embed

def get_session(session_key):
    return _engine.SessionStore(session_key)


def get_user(session):
    class Dummy(object):
        pass

    django_request = Dummy()
    django_request.session = session

    return django.contrib.auth.get_user(django_request)

unjson = simplejson.loads
json = simplejson.dumps

ORDERS_REDIS_HOST = getattr(settings, 'ORDERS_REDIS_HOST', 'localhost')
ORDERS_REDIS_PORT = getattr(settings, 'ORDERS_REDIS_PORT', 6379)
ORDERS_REDIS_PASSWORD = getattr(settings, 'ORDERS_REDIS_PASSWORD', None)
ORDERS_REDIS_DB = getattr(settings, 'ORDERS_REDIS_DB', None)

class Connection(SockJSConnection):
    def __init__(self, *args, **kwargs):
        super(Connection, self).__init__(*args, **kwargs)
        self.listen_redis()

    @tornado.gen.engine
    def listen_redis(self):
        self.redis_client = tornadoredis.Client(
                host=ORDERS_REDIS_HOST,
                port=ORDERS_REDIS_PORT,
                password=ORDERS_REDIS_PASSWORD,
                selected_db=ORDERS_REDIS_DB
            )
        self.redis_client.connect()

        yield tornado.gen.Task(self.redis_client.subscribe, [
            'update_notes',
            'update_groups',
            'update_friends',
        ])
        self.redis_client.listen(self.on_redis_queue)

    def send(self, data):
        return super(Connection, self).send(data)

    def on_open(self, info):
        self.django_session = get_session(info.get_cookie('sessionid').value)
        self.user = get_user(self.django_session)

    def on_message(self):
        pass
    def on_redis_queue(self, message):
        if message.kind == 'message':
            data = self.get_notifications()
            body = unjson(message.body)[0]
            if message.channel == 'update_notes':
                if Note.objects.get(pk=body['pk']).has_access(self.user):
                    data['new_note'] = body
                    self.send(data)
            if message.channel == 'update_groups':
                if body['fields']['user'] == self.user.pk:
                    data['new_group'] = body
                    self.send(data)

    def on_close(self):
        self.redis_client.unsubscribe([
            'update_notes',
            'update_groups',
            'update_friends',
        ])
        self.redis_client.disconnect()

    def get_notifications(self):
        data = {}
        data['friends_invitations_count'] = self.user.account.invitations().count()
        try:
            data['unreaded_notes_count'] = self.user.account.shared_notes().filter(date__gte=self.user.account.shared_notes_last_seen).count()
        except:
            data['unreaded_notes_count'] = 0
        data['groups_invitations_count'] = GroupUser.objects.filter(user_id=self.user.id, confirmed=False).count()
        return data
