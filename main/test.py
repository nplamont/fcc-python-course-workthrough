import pika

url =  "amqp://foo:bar@localhost:5672/"

try:
#url = os.environ.get('CLOUDAMQP_URL', 'amqp://guest:guest@localhost:5672/%2f')
  params = pika.URLParameters(url)
  connection = pika.BlockingConnection(params)
 
  channel = connection.channel() # start a channel
  channel.queue_declare(queue='test') # Declare a queue
  channel.basic_publish(exchange='',
                    routing_key='',
                    body='Hello CloudAMQP!')
except AssertionError as error:
  print(error) 
  print(" [x] Sent 'Hello World!'")

connection.close()


