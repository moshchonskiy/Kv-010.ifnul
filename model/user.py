__author__ = 'Evgen'


class User(object):
    def __init__(self, username="", password=""):
        self.username = username
        self.password = password

    @classmethod
    def Admin(cls):
        return cls(username="admin", password="nimda")

    @classmethod
    def random(cls):
        from random import randint
        return cls(username="user" + str(randint(0, 1000000)),
                   password="pass" + str(randint(0, 1000000)))
