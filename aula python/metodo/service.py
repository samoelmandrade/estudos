from kafka_producer import enviar_mensagem_kafka

def meu_servico():
    topic = "local_teste_rastreamento"
    mensagem = "Mensagem do meu serviço para o Kafka!"

    enviar_mensagem_kafka(topic, mensagem)

if __name__ == "__main__":
    meu_servico()
