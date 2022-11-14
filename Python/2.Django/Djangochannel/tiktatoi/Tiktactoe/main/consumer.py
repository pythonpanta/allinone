from channels.consumer import SyncConsumer,StopConsumer
import json
class MySyncConsumer(SyncConsumer):
    mydict={}
    def websocket_connect(self,event):
        self.send({
            'type':'websocket.accept'
        })
    def websocket_receive(self,event):
        value=event['text']
        myd=json.loads(value)
        id=myd['value']
        user=myd['user']
        self.mydict[id]=user
        for key,value in self.mydict.items():
            print(key,':',value)

    def websocket_disconnect(self,event):
        raise StopConsumer
    