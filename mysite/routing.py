from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
from channels.security.websocket import AllowedHostsOriginValidator, OriginValidator
from django.urls import path,include
from normal_user.consumers import MessageNotify, ManagerNotify, ChatConsumer, ChatOnlineConsumer, CallConsumer, TaskNotify, Notifications
from django.conf.urls import url

application = ProtocolTypeRouter({
    'websocket' :AllowedHostsOriginValidator(
    	AuthMiddlewareStack(
    		URLRouter(
    			[
    				path('channels_url/<username>/',MessageNotify, name = 'channels_url'),
                    path('manager_notify/<username>/',ManagerNotify, name = 'manager_notify'),
                    path('char_bxx/',ChatConsumer, name = 'char_bxx'),
                    path('chat_bxx/',ChatOnlineConsumer, name = 'chat_bxx'),
                    path("ws/startCall/", CallConsumer, name = 'startCall'),
                    path("task_acknowledge/", TaskNotify, name = 'task_acknowledge'),
                    path("notifications/", Notifications, name = 'notifications'),
    			]
    		)
    	)
    )
})
