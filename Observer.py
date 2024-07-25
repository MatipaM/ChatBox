import os
import json


class Observer:
    def notify(self, message:str):
        print("Observer code being called")
        print("message", message)

        if os.path.exists("Chat.json"):
            try:
                with open("Chat.json", "r") as f:
                    previous_messages = json.load(f)
                    print("JSON load", previous_messages)
            except json.JSONDecodeError as e:
                    previous_messages = []
                    print(f"Error: {e.msg}, {e.lineno}, {e.colno}")
            except Exception as e:
                    previous_messages = []
                    print(f"Unexpected error: {e}")
        else:
            previous_messages = []

        previous_messages.append(message)

        with open("Chat.json", "w") as f:
            print("previous_messages", previous_messages)
            json.dump(previous_messages, f, indent=4)
            print("JSON updated with new messages data")

    