from confluent_kafka import Producer, KafkaError
import threading

def produce_messages(producer, topic, num_messages):
    for i in range(num_messages):
        message = f"Mensagem {i}"
        producer.produce(topic, key=str(i), value=message)
        producer.poll(0.5)  # Permite o envio assíncrono
        print(f"Produzida para o lennon: {message}")

    producer.flush()

def main():
    # Configurações do Kafka
    kafka_config = {
        'bootstrap.servers': '20.84.11.171:9094' # Endereço do broker do Kafka
      
    }

    topic = 'local_teste_rastreamento'  # Substitua pelo nome do seu tópico
    num_messages = 100  # Número de mensagens a serem produzidas

    producer = Producer(kafka_config)
    threads = []

    # Cria múltiplas threads para produzir mensagens em paralelo
    for _ in range(5):
        thread = threading.Thread(target=produce_messages, args=(producer, topic, num_messages))
        threads.append(thread)
        thread.start()

    # Espera todas as threads concluírem
    for thread in threads:
        thread.join()

    producer.close()

if __name__ == '__main__':
    main()