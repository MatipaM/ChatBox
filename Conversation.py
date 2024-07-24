from Observer import Observer
from Message import UserMessage
from Message import AIMessage
from Message import FriendlyMessage
from Message import SophisticatedMessage
from datetime import datetime

class Conversation(): #Observable
    __instance = None

    @classmethod
    def get_instance(cls):
        if cls.__instance is None:
            cls.__instance = cls()

        return cls.__instance
    def __init__(self) -> None:
        self.observers: list[Observer] = []

    def add(self, observer: Observer):
        self.observers.append(observer)

    def update(self):
        for observer in (self.observers):
            if isinstance(observer, UserMessage):   
                observer.notify(f"User: {observer.msg}, {datetime.now()}")
            elif isinstance(observer, AIMessage):     
                observer.notify(f"AI: {observer.msg}, {datetime.now()}")
            elif isinstance(observer, FriendlyMessage):     
                observer.notify(f"Friendly AI: {observer.msg}, {datetime.now()}")
            elif isinstance(observer, SophisticatedMessage):     
                observer.notify(f"Sophisticated AI: {observer.msg}, {datetime.now()}")
    