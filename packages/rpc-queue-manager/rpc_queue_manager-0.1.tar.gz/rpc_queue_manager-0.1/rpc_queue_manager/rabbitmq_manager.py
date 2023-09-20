import pika

class RabbitMQManager:
    def __init__(self, host, **kwargs):
        self.username = kwargs.get('username', 'guest')
        self.password = kwargs.get('password', 'guest')
        self.queue_name = kwargs.get('queue_name', 'mq_queue')

        credentials = pika.PlainCredentials(self.username, self.password)
        self.connection = pika.BlockingConnection(pika.ConnectionParameters(host=host, credentials=credentials))
        self.channel = self.connection.channel()
        self.channel.queue_declare(queue=self.queue_name)


    def close(self):
        """
            Closes the RabbitMQ connection if it is open.

            Returns:
                None
        """
        if self.connection and self.connection.is_open:
            self.connection.close()



    def queue_size(self):
        """
        Retrieves the number of messages currently in the RabbitMQ queue.

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



    def publish(self, message):
        """
        Publishes a message to the RabbitMQ queue.

        Args:
            message (str or bytes): The message to be published to the queue.

        Raises:
            ValueError: If there is an issue with publishing the message to the queue.

        Returns:
            None
        """
        try:
            # Publish a message to the queue
            self.channel.basic_publish(exchange='', routing_key=self.queue_name, body=str(message))
        except Exception as e:
            raise ValueError(f"Failed to publish message to the queue: {str(e)}")



    def consume(self, callback=None):

        """
         Continuously consumes messages from the queue and processes them using the provided callback function.

         Args:
             callback (function): The callback function to process incoming messages.
                 It should accept parameters (ch, method, properties, body).

         Returns:
             None
         """

        try:
            print(f"Waiting for messages from '{self.queue_name}'. To exit, press CTRL+C")

            while True:
                # Check for a message
                method_frame, header_frame, body = self.channel.basic_get(self.queue_name, auto_ack=True)
                if method_frame:
                    # A message is available, process it
                    callback(None, None, None, body)
                else:
                    # Queue is empty, exit the loop
                    print("Queue is empty. Closing the connection...")
                    self.close()
                    break
        except KeyboardInterrupt:
            # Gracefully exit if interrupted (CTRL+C)
            self.close()
        except Exception as e:
            raise ValueError(f"Failed to consume messages from the queue: {str(e)}")