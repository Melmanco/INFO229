import os

from pymongo import MongoClient

# Create the JamesBot Class
class JamesBot:

    # Create a constant that contains the default texts for the message
    GREETINGS = [
        {
            "dict":{
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": "Hola mundo!"
                }
            }

        },{
            "dict":{
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": "Hello world!"
                }
            }

        },{
            "dict":{
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": "Bonjour monde!"
                }
            }

        }
    ]

    
    # The constructor for the class.
    def __init__(self, channel):
        self.channel = channel
        self.client = MongoClient(os.environ.get("MONGO_PORT"))
        self.db = self.client.greetings
        self.greetings = self.db.greetings
        self.greetings.insert_many(self.GREETINGS)

    
    #Get random message from db
    def _choose_message(self):
        return self.greetings.aggregate([{ "$sample": {"size": 1} }]).next()["dict"]
    

    # Craft and return the entire message payload as a dictionary.
    def get_message_payload(self):
        return {
            "channel": self.channel,
            "blocks": [
                self._choose_message()
            ]
        }
