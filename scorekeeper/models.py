__author__ = 'lassebrostedpedersen'

class User(object):
    def __init__(self, name, email, notifications, password_hash):
        self.name = name
        self.email = email
        self.notifications = notifications
        self.password_hash = password_hash

class Bet(object):
    def __init__(self, id, name, description, timestamp, participants):
        pass

