from Message import AIMessage
from Message import UserMessage
from Message import FriendlyMessage
from Message import SophisticatedMessage

class MessageFactory:
    @staticmethod
    def createMessage(message_type, message): #to show scalable, make friendly AI or mean AI
        if message_type == 'user':
            return UserMessage(message)
        elif message_type == 'ai':
            return AIMessage(message)
        elif message_type == 'friendly_ai':
            return FriendlyMessage(message)
        elif message_type == 'sophisticated_ai':
            return SophisticatedMessage(message)
