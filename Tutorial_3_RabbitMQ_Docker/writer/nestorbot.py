class NestorBot:

    # The constructor for the class. It takes the channel name as the a
    # parameter and then sets it as an instance variable
    def __init__(self, channel):
        self.channel = channel

    # Craft and return the entire message payload as a dictionary.
    def get_message_payload(self, message):
        return {
            "channel": self.channel,
            "blocks": [{
                "dict":{
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": message
                }
                }
            }]
        }
