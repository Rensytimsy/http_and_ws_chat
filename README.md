# HTTP_AND_WS_CHAT

## WS(web sockets) 
This protocols provides **bidirectional** communication, in sense that only an http request is made in the beginng to initialize a connection *(101 switching protocols status)*, then an open connection is created where both the server and the client can communicate, with low latency.
Diagram illustration on docs/diagrams/ws_communication.mmd
**NB: SSE (server side events) [(https://en.wikipedia.org/wiki/Server-sent_events)]**, which can also be used for push notification but has ambigious code just to achieve what one can achieve with ws(web sockets), it's architecture is one direction only server -> client. Good for push notification from the sys(system/server).

## HTTP(hyper text transfer protocols)
Standard web protocol uses a **request,response** mechanism, for each communication to happen a request must be initilized and sent to the server, high latency up to 500ms, no open connection, communication is based on the number of requests being made by the client.
Diagram illustration on docs/diagrams/http_communcation.mmd

## Django Channels
Channels enables one to use websockets and more other none http-protocols when working with django framework. Extends django beyond http, to accept more protocols for communications.

# Setting Up Channels Routes And Consumers

 # Intergrating Channels library
 Channels uses a django specification ASGI (asynchronus server gateway interface) to provide a url configuration, which provides the routing for the channels to use, and specifically tells http what code to run from the channel server. code present at *apps/chat/asgi.py*
 intergrating is straight forward, just need channels routing, and asgi applicatin definatin then add it to settings module *ASGI_APPLICATION="chat.asgi.application"*
 ```
    import os
    from channels.routing import ProtocolTypeRouter
    from django.core.asgi import get_asgi_application

    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "apps.settings")
    application = ProtocolTypeRouter({
        "http": get_asgi_application()
    })

 ```
 The code above takes over default django server usually handles http protocols, and exposes it using dhapne to accept/handle more protocols beyond http, the server is officially run by daphne.

 # Writing WebSocket Consumer
 By default when a ws request is made *e.g ws://127.0.0.1:8000/chat/lobby*, default channels url configuration is consulted, and returns the targeted web socket url, all the websocket url lifecycle is defined in the consumer, consumer.py file.
 A consumer basically has four common events 
 - connect
 - accept
 - receive
 - disconnect

 # Channel layer
 A channel layer enables mulitiple consumers to communicate with each other, in this case of both the chatgpt and chat application this is a crucial piece of code to have a final working project.
 A channel provides the following abstraction 
 1. channel - think of this as a mailbox where messages should be sent and received e.g channel would be a group name.
 2. group - a group of channels, one can add or remove channels in a group or send message to all channel in a group, think of channels as logged in users in a chat appliation, and a group is a whatsApp group lets say FATA Kenya in this case.
 channels(users) send messages to group (Fata kenya) and every channel(user) in the group gets to see the message.

 **NB:** Each  consumer has a unique channel name, one can communicate with a channel using the channel layer. for better illustration check diagram on *docs/diagrams/channel_layer.mmd*

 Now for a chat application we need multiple instances of our consumer **ChatWebsocketConsumer** to have a send/receive message flow in a group, that is handled by channel_layer

 
