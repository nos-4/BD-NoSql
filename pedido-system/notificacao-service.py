import pika
import json

# Função chamada toda vez que uma nova mensagem for recebida
def callback(ch, method, properties, body):
    try:
        # Converte o JSON recebido
        mensagem = json.loads(body)

        # Extrai dados do pedido
        pedido_id = mensagem.get('pedido_id')
        cliente = mensagem.get('cliente')
        produto = mensagem.get('produto')
        quantidade = mensagem.get('quantidade')

        # Simula envio de e-mail
        print("\n📬 [Notificação Recebida]")
        print(f"Simulando envio de e-mail para {cliente}...")
        print(f"Pedido #{pedido_id}: {quantidade}x {produto}")
        print("📧 E-mail enviado com sucesso! (simulado)\n")

        # Confirma que a mensagem foi processada
        ch.basic_ack(delivery_tag=method.delivery_tag)
    except Exception as e:
        print(f"Erro ao processar mensagem: {e}")
        ch.basic_nack(delivery_tag=method.delivery_tag)

# Função principal do serviço
def iniciar_consumidor():
    try:
        # Conecta ao RabbitMQ
        conexao = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
        canal = conexao.channel()

        # Garante que a fila exista
        canal.queue_declare(queue='pedido_criado', durable=True)

        # Configura o consumidor
        canal.basic_qos(prefetch_count=1)
        canal.basic_consume(queue='pedido_criado', on_message_callback=callback)

        print("📡 Aguardando mensagens da fila 'pedido_criado'...")
        print("🔁 Pressione CTRL+C para encerrar.")
        canal.start_consuming()
    except KeyboardInterrupt:
        print("\n❌ Serviço de notificação encerrado manualmente.")
    except Exception as e:
        print(f"Erro ao iniciar consumidor: {e}")

# Executa se chamado diretamente
if __name__ == "__main__":
    iniciar_consumidor()
