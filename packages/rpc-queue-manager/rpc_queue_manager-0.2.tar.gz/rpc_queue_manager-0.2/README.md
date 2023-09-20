# RabbitMQ RPC message

[![License](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)


## Features

- [Introduction](#introduction)
- [Installation](#installation)
- [Usage](#usage)

## Introduction

rpc queue manager is a Python package that simplifies RPC communication between two projects by leveraging the power of RabbitMQ queues. It provides a seamless and efficient way for applications to exchange data and invoke remote procedures across different services or components.

## Key Features
**Effortless Communication:** With rpc queue manager, you can establish a reliable and real-time communication channel between your projects with minimal effort.

**RPC Queues:** Harness the capabilities of RabbitMQ to create RPC queues for your applications, facilitating synchronous communication between services.

**Queue Management:** Manage queues effortlessly—start and maintain consumers for continuous data exchange.

**Callback Responses:** Push data into a queue and receive callback responses, enabling dynamic interactions between services.


## Installation

- pip install rpc-queue-manager==0.1 

## Usage

**RPC Consumer**

To Start Consuer Server
- create a consumer_service.py file 
```python
from rpc_queue_manager.rpc_manager import RPCQueueConsumer

class ConsumerService:
    
    def callback(self,body):
        print(f"Received message: {body}")
        response  = body 
        return response

    def start_consumer(self):
        credentials = {"username": "guest", "password": "guest", "queue_name": "rpc_college_listing"}
        consumer_obj = RPCQueueConsumer(host='localhost', callback=self.callback, **credentials)
        consumer_obj.start_consuming()
```

- add below code into app.py in your django app. 

```python
from django.apps import AppConfig
from .consumer_service import ConsumerService #import file where you creat it 
import threading

class MainsiteConfig(AppConfig):
    name = 'mainsite'

    def ready(self):
        consumer_obj = ConsumerService()

        consumer_thread = threading.Thread(target=consumer_obj.start_consumer)
        # Set the thread as a daemon so it terminates when the main program exits
        consumer_thread.daemon = True
        # Start the consumer thread
        consumer_thread.start()
```


- run your django project 

**RPC Producer**

```python
from rpc_queue_manager.rpc_manager import RPCQueueProducer

credentials = {"username": "guest", "password": "guest"}
producer_obj = RPCQueueProducer(host='localhost', **credentials)


data = {
    "queue": "rpc_college_listing",
    "function_name" : "get_college_detail",
    "data":{
        "college_id" : 1234567 
    }
}
producer_obj.publish(data)
producer_obj.close_connection()

```