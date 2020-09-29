from app import login_manager, mgConnection


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
def user_loader(username):
    u = mgConnection.db.user_info.find_one({"username": username})
    return None if not u else LoginUser(username=u['username'])


@login_manager.request_loader
def request_loader(request):
    u = mgConnection.db.user_info.find_one({"username": request.form.get('username')})
    return None if not u else LoginUser(username=u['username'])
