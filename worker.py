from pika import PlainCredentials, ConnectionParameters, BlockingConnection
import httpx

credentials = PlainCredentials("guest", "guest")
conn_params = ConnectionParameters("localhost", 5672, credentials=credentials)

conn = BlockingConnection(conn_params)
channel = conn.channel()


def pick(channel, method, properties, body):
    print("Сообщение получено \n\n")

    httpx.post("http://localhost:8000/choose_winner")

    channel.basic_ack(delivery_tag=method.delivery_tag)

    print("Победитель выбран")


channel.basic_consume(queue="pick_winner", on_message_callback=pick, auto_ack=False)

try:
    channel.start_consuming()
except KeyboardInterrupt:
    channel.stop_consuming()
