from channels.consumer import AsyncConsumer,StopConsumer
class MyChatSyn(AsyncConsumer):
    async def websocket_connect(self,event):
        # print('connected websocket.....')
        await self.send({'type':'websocket.accept'})
        self.gname=self.scope['url_route']['kwargs']['groupname']
        await self.channel_layer.group_add(self.gname,self.channel_name)
  
    async def websocket_receive(self,event):
        # print('message from cleient to server....')
        # print(event['text'])
        await self.channel_layer.group_send(self.gname,{'type':'chat.message','message':event['text']})

    async def chat_message(self,event):
        # print('start...')
        await self.send({
            'type':'websocket.send',
            'text':event['message']
        }
        )


    async def websocket_disconnect(self,event):
        # print('web socket disconnected...')
        self.channel_layer.group_discard(self.gname,self.channel_name)
        raise StopConsumer