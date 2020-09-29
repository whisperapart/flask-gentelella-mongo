from bcrypt import gensalt, hashpw
from app import login_manager, mongoc


class LoginUser:
    def __init__(self, username):
        self.username = username

    @staticmethod
    def is_authenticated():
        return True

    @staticmethod
    def is_active():
        return True

    @staticmethod
    def is_anonymous():
        return False

    def get_id(self):
        return self.username


@login_manager.user_loader
def user_loader(id):
    u = mongoc.db.user_info.find_one({"username": id})
    if not u:
        return None
    return LoginUser(username=u['username'])


@login_manager.request_loader
def request_loader(request):
    username = request.form.get('username')
    u = mongoc.db.user_info.find_one({"username": username})
    if not u:
        return None
    return LoginUser(username=u['username'])
