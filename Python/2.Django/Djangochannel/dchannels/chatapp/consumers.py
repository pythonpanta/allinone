from channels.consumer import StopConsumer,SyncConsumer,AsyncConsumer
from asgiref.sync import async_to_sync
class MysyncConsumer(SyncConsumer):
    def websocket_connect(self,event):
        # print('websocket connect.........')
        # print('channel layer.....',self.channel_layer)
        # print('channel name......',self.channel_name)
        async_to_sync(self.channel_layer.group_add)('programmer',self.channel_name)
        self.send({'type':'websocket.accept'})
    
    def websocket_receive(self,event):
        '''
        function will run when message will send from client ot server
        '''
        # print('websocket receive.....')
        # print(event['text'])
        async_to_sync(self.channel_layer.group_send)('programmer',{'type':'chat.message','message':event['text']})
    # we need to send message to client for that we took help from the event as chat_message
    #send message to group and send message to client is two different thinhgs need to be be understand
    #send to group means send message to group and send to client me send so taht it will show in frontend
    def chat_message(self,event):
        # print('Event...',event['message'])
        # print('actual type',type(event['message']))
        self.send({
            'type':'websocket.send',
            'text':event['message']
        }
        )
           
    def websocket_disconnect(self,event):
        # print('websocket disconnect............')
        # print(event)
        async_to_sync(self.channel_layer.group_discard)('programmer',self.channel_name)
        raise StopConsumer()   