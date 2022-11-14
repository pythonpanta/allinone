from channels.consumer import StopConsumer,SyncConsumer,AsyncConsumer
from time import sleep
import asyncio
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
            self.send({
            'type':'websocket.send',
            'text':str(i)})
            sleep(1)
           
    def websocket_disconnect(self,event):
        print('websocket disconnect............')
        print(event)
        raise StopConsumer()   

    # async consumer 
class MyASsyncConsumer(AsyncConsumer):
    async def websocket_connect(self,event):
        print('websocket connect for async.........')
        print(event)
        await self.send({'type':'websocket.accept'})
    async def websocket_receive(self,event):
        print('websocket receive..... for async')
        print(event)
        print(event['text']) #message from client to server
        # await self.send({
        #     'type':'websocket.send',
        #     'text':'message from server to client from saync consumer'
        # })
        for i in range(10):
            await self.send({
            'type':'websocket.send',
            'text':str(i)})
            await asyncio.sleep(1)
    async def websocket_disconnect(self,event):
        print('websocket disconnect............ for async')
        print(event)
        raise StopConsumer()   