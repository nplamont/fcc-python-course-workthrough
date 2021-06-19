import pika, json

#params = pika.URLParameters('amqps://@hippo.rmq2.cloudamqp.com/ndqtulje')
#params = pika.URLParameters('amqp://foo:bar@localhost:5672/masha')
#connection = pika.BlockingConnection(params)
url = 'amqp://foo:bar@localhost:5672/%2f/'

params = pika.URLParameters(url)

#connection = pika.BlockingConnection(params)

#channel = connection.channel()

body = '{"author" : "John Doe",  "bookDescription" : "History VOL: 1",  "bookID" : 1  }'
def publish(method, body):
    properties = pika.BasicProperties(method)
    #channel.basic_publish(exchange='', routing_key='masha', body=json.dumps(body), properties=properties)
    #channel.basic_publish(exchange='', routing_key='masha', body=json.dumps(body))

#url =  "amqp://guest:guest@localhost:5672/%2f"


#url = os.environ.get('CLOUDAMQP_URL', 'amqp://guest:guest@localhost:5672/%2f')
#params = pika.URLParameters(url)
#connection = pika.BlockingConnection(params)
#channel = connection.channel() # start a channel
#channel.queue_declare(queue='masha') # Declare a queue
#channel.basic_publish(exchange='',
#                  routing_key='masha',
#                  body='Hello CloudAMQP!')

#print(" [x] Sent 'Hello World!'")

#connection.close()

