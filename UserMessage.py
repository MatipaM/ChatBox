from Observer import Observer

class UserMessage(Observer):
     def __init__(self, msg):
        self.msg = msg