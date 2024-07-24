from Observer import Observer

class AIMessage(Observer):
     def __init__(self, msg):
        self.msg = msg


class UserMessage(Observer):
     def __init__(self, msg):
        self.msg = msg

class FriendlyMessage(Observer):
     def __init__(self, msg):
        self.msg = msg

class SophisticatedMessage(Observer):
     def __init__(self, msg):
        self.msg = msg