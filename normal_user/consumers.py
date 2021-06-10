import asyncio
import json
from channels.consumer import AsyncConsumer
from channels.generic.websocket import AsyncWebsocketConsumer
from .models import ChatMessage, ChatThread, TaskModel
from dateparser import parse
from channels.db import database_sync_to_async


class MessageNotify(AsyncConsumer):
	async def websocket_connect(self,event):
		user = self.scope['user']
		self.g_name = str(user.id)
		await self.channel_layer.group_add(
			self.g_name,
			self.channel_name
		)
		await self.send({
			'type':'websocket.accept'
		})
	async def websocket_receive(self,event):
		front_text = event.get('text', None)
		if front_text:
			load_dic_data = json.loads(front_text)
			user_id = load_dic_data.get('user_id')
			myResponse = {
				"data" : json.dumps(load_dic_data)
			}
			self.g_name = str(user_id)

			await self.channel_layer.group_send(
				self.g_name,
				{
					"type":"new_message",
					"text": json.dumps(myResponse)
				}
			)
			# await self.send({
			# 	'type' : 'websocket.send',
			# 	'text' : json.dumps(myResponse)
			# })
		# print(self.scope['user'])
	async def new_message(self,event):
		try:
			await self.send({
				"type":"websocket.send",
				"text":event.get('text')
			})
		except:
			pass
		
	async def websocket_disconnect(self,event):
		print("disconnected",event)


class ManagerNotify(AsyncConsumer):
	async def websocket_connect(self,event):
		user = self.scope['user']
		self.g_name = str(user.id)
		await self.channel_layer.group_add(
			self.g_name,
			self.channel_name
		)
		await self.send({
			'type':'websocket.accept'
		})
	async def websocket_receive(self,event):
		front_text = event.get('text', None)
		if front_text:
			load_dic_data = json.loads(front_text)
			user_id = load_dic_data.get('user_id')
			myResponse = {
				"data" : json.dumps(load_dic_data)
			}
			self.g_name = str(user_id)
			await self.channel_layer.group_send(
				self.g_name,
				{
					"type":"new_message",
					"text": json.dumps(myResponse)
				}
			)
	async def new_message(self,event):
		try:
			await self.send({
				"type":"websocket.send",
				"text":event.get('text')
			})
		except:
			pass
		
	async def websocket_disconnect(self,event):
		print("disconnected",event)


class ChatOnlineConsumer(AsyncConsumer):
	async def websocket_connect(self,event):
		user = self.scope['user']
		self.g_name = "message-notification"
		await self.channel_layer.group_add(
			self.g_name,
			self.channel_name
		)
		await self.send({
			'type':'websocket.accept'
		})
	async def websocket_receive(self,event):
		front_text = event.get('text', None)
		if front_text:
			load_dic_data = json.loads(front_text)
			# chat_message = load_dic_data.get('chat_message', None)
			online_status = load_dic_data.get('staff_div_id', None)

			myResponse = {
				"data" : json.dumps(load_dic_data)
			}
			self.g_name = "message-notification"
			await self.channel_layer.group_send(
				self.g_name,
				{
					"type":"new_message",
					"text": json.dumps(myResponse)
				}
			)
	async def new_message(self,event):
		try:
			await self.send({
				"type":"websocket.send",
				"text":event.get('text')
			})
		except:
			pass
		
	async def websocket_disconnect(self,event):
		print("disconnected",event)


class ChatConsumer(AsyncConsumer):
	async def websocket_connect(self,event):
		user = self.scope['user']
		self.g_name = str(user.id)
		await self.channel_layer.group_add(
			self.g_name,
			self.channel_name
		)
		await self.send({
			'type':'websocket.accept'
		})
	async def websocket_receive(self,event):
		front_text = event.get('text', None)
		if front_text:
			load_dic_data = json.loads(front_text)
			user_id = load_dic_data.get('user_id')
			manager_id = load_dic_data.get('manager_id')
			reciever_manager_id = load_dic_data.get('reciever_manager_id')
			if user_id:
				print(load_dic_data)
				sender_user = self.scope['user']
				chat_message = load_dic_data.get('chat_message')
				await self.get_thread(sender_user, user_id, load_dic_data, chat_message)
				myResponse = {
					"data" : json.dumps(load_dic_data)
				}
				self.g_name = str(user_id)
				await self.channel_layer.group_send(
					self.g_name,
					{
						"type":"new_message",
						"text": json.dumps(myResponse)
					}
				)
			elif manager_id or reciever_manager_id:
				sender_user = self.scope['user']
				chat_message = load_dic_data.get('chat_message')
				myResponse = {
					"data" : json.dumps(load_dic_data)
				}
				if manager_id:
					self.g_name = str(manager_id)
				else:
					self.g_name = str(reciever_manager_id)
				await self.channel_layer.group_send(
					self.g_name,
					{
						"type":"new_message",
						"text": json.dumps(myResponse)
					}
				)

	async def new_message(self,event):
		try:
			await self.send({
				"type":"websocket.send",
				"text":event.get('text')
			})
		except:
			pass
		
	async def websocket_disconnect(self,event):
		print("disconnected",event)

	@database_sync_to_async
	def get_thread(self, sender_user, reciever_user,load_dic_data, chat_message):
		try:
			print("load_dic_data : ---", load_dic_data)
			date = load_dic_data.get('backend_time')
			receiver_backend_time = load_dic_data.get("receiver_backend_time")
			# split_date = date.split(" , ")
			# split_date_date = split_date[0].split("/")
			# date = split_date_date[1]+"/"+split_date_date[0]+"/"+split_date_date[-1] +" , "+ split_date[1]

			thread_obj = ChatThread.objects.filter(sender_id = sender_user.id, reciever_id = int(reciever_user))
			thread_obj_1 = ChatThread.objects.filter(sender_id = int(reciever_user), reciever_id = sender_user.id)

			if thread_obj:
				ChatThread.objects.filter(sender_id = sender_user.id, reciever_id = int(reciever_user)).update(date_updated = parse(date), date_updated_receiver = parse(receiver_backend_time))
			elif thread_obj_1:
				ChatThread.objects.filter(sender_id = int(reciever_user), reciever_id = sender_user.id).update(date_updated = parse(date), date_updated_receiver = parse(receiver_backend_time))
			else:
				thread_id_2 = ChatThread(sender_id = sender_user.id, reciever_id = int(reciever_user), date_updated = parse(date), date_updated_receiver = parse(receiver_backend_time))
				thread_id_2.save()
			if thread_obj:
				thread_id = thread_obj[0].id
			elif thread_obj_1:
				thread_id = thread_obj_1[0].id
			else:
				thread_id = thread_id_2.id
			print("--------------------\n\n\n\n",parse(date) , parse(receiver_backend_time))
			ChatMessage.objects.create(sender_id = sender_user.id, reciever_id = int(reciever_user), message = chat_message, thread_id = thread_id, created = parse(date), name = load_dic_data.get('name'), created_receiver = parse(receiver_backend_time))
		except Exception as g:
			print("-------------------",g)


class CallConsumer(AsyncConsumer):

    async def websocket_connect(self,event):
        user = self.scope['user']
        self.groupname = str(user.id)
        # self.groupname = 'callNotification'
        # # Join room group
        await self.channel_layer.group_add(
            self.groupname,
            self.channel_name
        )

        await self.send({
			'type':'websocket.accept'
        })

    async def websocket_disconnect(self, event):
        # Leave group
        print("disconnected",event)
        

    # Receive message from WebSocket
    async def websocket_receive(self, text_data):
        # print("-----",type(text_data))
        text_data_json = json.loads(text_data["text"])
        # print(text_data)
        meeting_id = text_data_json['meeting_id']
        # print(meeting_id)
        # user_id = text_data_json.get('user_id')
        self.groupname = str(meeting_id)
        myResponse = {"meeting_id" : meeting_id}
        await self.channel_layer.group_send(
            self.groupname,
            {
                'type': 'new_message',
                'text': json.dumps(myResponse)
            }
        )

    
    async def new_message(self, event):
        # print("-----------------------")
        try:
            # print(type(event.get("text")))
            await self.send( {
            	"type":"websocket.send", 
            	"text" : event.get("text")
            })
        except Exception as h:
            print(h)


class TaskNotify(AsyncConsumer):
	async def websocket_connect(self,event):
		user = self.scope['user']
		self.g_name = str(user.id)
		await self.channel_layer.group_add(
			self.g_name,
			self.channel_name
		)
		await self.send({
			'type':'websocket.accept'
		})
	async def websocket_receive(self,event):
		front_text = event.get('text', None)
		if front_text:
			load_dic_data = json.loads(front_text)
			user_id = load_dic_data.get('user_id')
			myResponse = {
				"data" : json.dumps(load_dic_data)
			}
			self.g_name = str(user_id)

			await self.channel_layer.group_send(
				self.g_name,
				{
					"type":"new_message",
					"text": json.dumps(myResponse)
				}
			)
			# await self.send({
			# 	'type' : 'websocket.send',
			# 	'text' : json.dumps(myResponse)
			# })
		# print(self.scope['user'])
	async def new_message(self,event):
		try:
			await self.send({
				"type":"websocket.send",
				"text":event.get('text')
			})
		except:
			pass
		
	async def websocket_disconnect(self,event):
		print("disconnected",event)


class Notifications(AsyncConsumer):
	async def websocket_connect(self,event):
		user = self.scope['user']
		self.g_name = str(user.id)
		await self.channel_layer.group_add(
			self.g_name,
			self.channel_name
		)
		await self.send({
			'type':'websocket.accept'
		})
	async def websocket_receive(self,event):
		front_text = event.get('text', None)
		if front_text:
			load_dic_data = json.loads(front_text)
			user_id = load_dic_data.get('user_id')
			myResponse = {
				"data" : json.dumps(load_dic_data)
			}
			self.g_name = str(user_id)

			await self.channel_layer.group_send(
				self.g_name,
				{
					"type":"new_message",
					"text": json.dumps(myResponse)
				}
			)
			# await self.send({
			# 	'type' : 'websocket.send',
			# 	'text' : json.dumps(myResponse)
			# })
		# print(self.scope['user'])
	async def new_message(self,event):
		try:
			await self.send({
				"type":"websocket.send",
				"text":event.get('text')
			})
		except:
			pass
		
	async def websocket_disconnect(self,event):
		print("disconnected",event)


