from confluent_kafka import Consumer, KafkaError

def consume_messages(consumer, topic):
    consumer.subscribe([topic])
    count  = 0 
    while True:
        msg = consumer.poll(1.0)

        if msg is None:
            continue
        if msg.error():
            if msg.error().code() == KafkaError._PARTITION_EOF:
                continue
                count +1
            else:
                print(msg.error())
                break

        print(f"count : Consumida: {msg.value().decode('utf-8')}")

    consumer.close()

def main():
    # Configurações do Kafka
    kafka_config = {
        'bootstrap.servers': '20.84.11.171:9094',  # Endereço do broker do Kafka
        'group.id': 'lennon_vou_testar_tb',
        'auto.offset.reset': 'earliest'  # Define a estratégia para lidar com offsets iniciais
    }

    topic = 'local_teste_rastreamento'  # Substitua pelo nome do seu tópico

    consumer = Consumer(kafka_config)
    consume_messages(consumer, topic)

if __name__ == '__main__':
    main()
