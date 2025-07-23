
import redis
import json

# Conexão com o Redis
redis_client = redis.Redis(host='localhost', port=6379, db=0, decode_responses=True)

def get_pedido_cache(pedido_id):
    """Busca um pedido no cache pelo ID."""
    pedido_json = redis_client.get(f"pedido:{pedido_id}")
    if pedido_json:
        return json.loads(pedido_json)
    return None

def set_pedido_cache(pedido_id, pedido_data):
    """Salva um pedido no cache."""
    redis_client.set(f"pedido:{pedido_id}", json.dumps(pedido_data), ex=3600)  # Expira em 1 hora
