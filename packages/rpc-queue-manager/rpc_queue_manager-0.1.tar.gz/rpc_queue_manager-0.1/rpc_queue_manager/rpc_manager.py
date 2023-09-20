import pika
import uuid
import json


class RPCQueueConsumer:
    def __init__(self, host='localhost', callback=None, **kwargs):
        self.username   =   kwargs.get('username','guest')
        self.password   =   kwargs.get('password','guest')
        self.queue_name =   kwargs.get('queue_name','rpc_queue')
        self.callback   =   callback

        credentials     =   pika.PlainCredentials(self.username, self.password)
        self.connection =   pika.BlockingConnection(pika.ConnectionParameters(host=host, credentials=credentials))
        self.channel    =   self.connection.channel()
        self.channel.queue_declare(queue=self.queue_name)


    def disconnect(self):
        """
        Disconnects from the RabbitMQ connection if it is not already closed.

        Returns:
            None
        """
        if self.connection and not self.connection.is_closed:
            self.connection.close()


    def queue_size(self):
        """
        Retrieves the current number of messages in the RabbitMQ queue.

        Returns:
            int: The number of messages in the queue.

        Raises:
            Exception: If there is an issue retrieving the queue size.
        """
        try:
            # Get the number of messages in the queue
            method_frame = self.channel.queue_declare(queue=self.queue_name, passive=True)
            return method_frame.method.message_count
        except Exception as e:
            raise Exception(f"Failed to get queue size: {e}")


    def close_connection(self):
        self.connection.close()



    def on_request(self, ch, method, props, body):
        """
        Handles an incoming request message from the RabbitMQ queue.

        Args:
            ch: The RabbitMQ channel.
            method: The RabbitMQ method frame.
            props: The RabbitMQ properties.
            body: The message body.

        Returns:
            None
        """
        try:
            body = body.decode().replace("'", '"')
            body = json.loads(body)

            response = self.callback(body)

            ch.basic_publish(exchange='',
                             routing_key=props.reply_to,
                             properties=pika.BasicProperties(correlation_id=props.correlation_id),
                             body=str(response))
            ch.basic_ack(delivery_tag=method.delivery_tag)

        except Exception as e:
            print("Error : ",e)


    def start_consuming(self):
        """
        Starts consuming messages from the RabbitMQ queue using the RPC pattern.

        The function sets up QoS (Quality of Service) to ensure that only one message is processed at a time
        by setting `prefetch_count` to 1.

        Returns:
            None
        """
        try:
            self.channel.basic_qos(prefetch_count=1)
            self.channel.basic_consume(queue=self.queue_name, on_message_callback=self.on_request)

            print(f"RPC Consumer Start ........")
            self.channel.start_consuming()
        except Exception as e:
            print(e)





class RPCQueueProducer:
    def __init__(self, host='localhost', **kwargs):
        self.username = kwargs.get('username', 'guest')
        self.password = kwargs.get('password', 'guest')
        self.queue_name = kwargs.get('queue_name', 'rpc_queue')

        credentials = pika.PlainCredentials(self.username, self.password)
        self.connection = pika.BlockingConnection(pika.ConnectionParameters(host=host, credentials=credentials))

        self.channel = self.connection.channel()

        result = self.channel.queue_declare(queue='', exclusive=True)
        self.callback_queue = result.method.queue

        self.channel.basic_consume(
            queue=self.callback_queue,
            on_message_callback=self.on_response,
            auto_ack=True)

        self.response = None
        self.corr_id = None



    def close_connection(self):
        self.connection.close()


    def on_response(self, ch, method, props, body):
        """
        Handles an incoming response message from the RPC server.

        Args:
            ch: The RabbitMQ channel.
            method: The RabbitMQ method frame.
            props: The RabbitMQ properties.
            body: The message body.

        Returns:
            None
        """
        if self.corr_id == props.correlation_id:
            # If the correlation IDs match, set the response
            self.response = body



    def set_queue(self, data):
        """
        Publishes a request message to the RabbitMQ queue and waits for a response.

        Args:
            data (dict): The data to be sent as a request message.

        Returns:
            dict or None: The response received from the RPC server, or None if an error occurs.
        """
        try:
            # Serialize the data as JSON
            data = json.dumps(data)

            # Initialize response and correlation ID
            self.response = None
            self.corr_id = str(uuid.uuid4())

            # Publish the request message to the queue with reply_to and correlation_id properties
            self.channel.basic_publish(
                exchange='',
                routing_key=self.queue_name,
                properties=pika.BasicProperties(
                    reply_to=self.callback_queue,
                    correlation_id=self.corr_id,
                ),
                body=str(data)
            )

            # Process data events to wait for a response
            self.connection.process_data_events(time_limit=None)

            # Return the response received
            return self.response
        except Exception as e:
            print(e)