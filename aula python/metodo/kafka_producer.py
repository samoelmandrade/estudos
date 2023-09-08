from confluent_kafka import Producer

def delivery_report(err, msg):
    if err is not None:
        print('Erro ao enviar a mensagem: {}'.format(err))
    else:
        print('Mensagem enviada para o tópico {} [{}]'.format(msg.topic(), msg.partition()))

def enviar_mensagem_kafka(topic, message):
    conf = {
        'bootstrap.servers': '20.84.11.171:9094',  # Endereço do servidor Kafka
        'client.id': 'python-producer'
    }

    producer = Producer(conf)
    producer.produce(topic, value=message, callback=delivery_report)
    producer.flush()

if __name__ == "__main__":
    topic = "local_teste_rastreamento"
    mensagem = "Olá, Kafka!"

    enviar_mensagem_kafka(topic, mensagem)
