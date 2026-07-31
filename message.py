from pika import PlainCredentials, ConnectionParameters, BlockingConnection
import json

participant = "Anna Karenina"
credentials = PlainCredentials("guest", "guest")
conn_params = ConnectionParameters("localhost", 5672, credentials=credentials)


def pick_winner(participants: list[str] | str = participant):
    with BlockingConnection(conn_params) as conn:
        message = json.dumps(participants)
        channel = conn.channel()

        channel.queue_declare(queue="pick_winner")

        channel.basic_publish(exchange="", routing_key="pick_winner", body=message)

        print("Сообщение отправлено")
