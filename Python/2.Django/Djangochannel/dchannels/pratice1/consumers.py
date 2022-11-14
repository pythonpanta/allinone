from channels.consumer import StopConsumer,SyncConsumer,AsyncConsumer
from time import sleep
import json
class MysyncConsumer(SyncConsumer):
    def websocket_connect(self,event):
        print('websocket connect.........')
        print(event)
        self.send({'type':'websocket.accept'})
    def websocket_receive(self,event):
        print('websocket receive.....')
        print(event)
        print(event['text']) #message from client to server
       
        for i in range(10):
            # send message from server to client 
            self.send({
            'type':'websocket.send',
            'text':json.dumps({'count':i}) #convert python object into string
            })
            sleep(1)
           
    def websocket_disconnect(self,event):
        print('websocket disconnect............')
        print(event)
        raise StopConsumer()   