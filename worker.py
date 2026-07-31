from pika import PlainCredentials, ConnectionParameters, BlockingConnection
from main import set_winner

credentials = PlainCredentials("guest", "guest")
conn_params = ConnectionParameters("localhost", 5672, credentials=credentials)

conn = BlockingConnection(conn_params)
channel = conn.channel()


def pick(channel, method, properties, body):
    print("Сообщение получено \n\n")
    print(f"winner is {body.decode()}")

    channel.basic_ack(delivery_tag=method.delivery_tag)

    set_winner(body.decode())

    print("*" * 20)


channel.basic_consume(queue="pick_winner", on_message_callback=pick, auto_ack=False)

try:
    channel.start_consuming()
except KeyboardInterrupt:
    channel.stop_consuming()
