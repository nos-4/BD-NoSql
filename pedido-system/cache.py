import redis
import json
from bson import ObjectId
from datetime import datetime

try:
    redis_client = redis.Redis(host='localhost', port=6379, db=0, decode_responses=True)
    redis_client.ping()
    print("Conexão com Redis estabelecida com sucesso!")
except redis.ConnectionError:
    print("Falha na conexão com Redis. Verifique se o servidor está rodando.")

def serialize_data(data):
    for k, v in data.items():
        if isinstance(v, ObjectId):
            data[k] = str(v)
        elif isinstance(v, datetime):
            data[k] = v.isoformat()  # Converte datetime para string ISO
    return data

def set_pedido_cache(pedido_id, pedido_data):
    pedido_copy = pedido_data.copy()
    pedido_copy = serialize_data(pedido_copy)
    redis_client.set(f"pedido:{pedido_id}", json.dumps(pedido_copy), ex=3600) #Expirar em 1 hora

def get_pedido_cache(pedido_id):
    pedido_json = redis_client.get(f"pedido:{pedido_id}")
    if pedido_json:
        return json.loads(pedido_json)
    return None

