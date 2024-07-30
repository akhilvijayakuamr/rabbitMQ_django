import pika
import json



class RpcServer:
    def __init__(self):
        connection = pika.BlockingConnection(pika.URLParameters('amqp://guest:guest@172.17.0.2:5672/'))
        self.channel = connection.channel()
        self.channel.queue_declare(queue='rpc_queue')
        self.channel.basic_consume(queue='rpc_queue', on_message_callback=self.on_request, auto_ack=True)\
            
            
    def on_request(self, ch, method, properties, body):
        number = json.loads(body)
        n1 = number['number1']
        n2 = number['number2']
        response = n1+n2
        
        self.channel.basic_publish(
            exchange='',
            routing_key=properties.reply_to,
            properties=pika.BasicProperties(correlation_id=properties.correlation_id),
            body=str(response)
        )
        
    def start(self):
        print("RPC server is started.... waiting for messages")
        self.channel.start_consuming()
        
        
if __name__ == '__main__':
    server = RpcServer()
    server.start()