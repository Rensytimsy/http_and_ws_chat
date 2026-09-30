import json #to handle data received and sent


from channels.generic.websocket import WebsocketConsumer
# from channels.generic.websocket import

class ChatWebSocketConsumer(WebsocketConsumer):
    
    # def accept():
    #     pass
    
    def connect(self):
        print("connected!")
        self.accept()
        return ""
    
    # def send():
    #     pass
    
    def receive(self, text_data): 
        text_data_json = json.loads(text_data)
        message = text_data_json["message"]
        
        self.send(text_data=json.dumps({
            "message": message
        }))
    
    # def close(): 
    #     pass
    
    def disconnect(self):
        print("disconnected!")
        pass