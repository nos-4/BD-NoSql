from models import Pedido
from database import get_database
from bson import ObjectId #usado para converter strings em IDs válidos do MongoDB.
from cache import get_pedido_cache, set_pedido_cache

db = get_database()
colecao_pedidos = db["pedidos"] #tabela onde os pedidos serão armazenados.


def criar_pedido(nome_cliente, produto, quantidade):
    if not all([nome_cliente, produto, quantidade]):
        raise ValueError("Todos os campos são obrigatórios.")
    
    pedido = Pedido(nome_cliente, produto, quantidade)
    result = colecao_pedidos.insert_one(pedido.to_dict())
    pedido.id = str(result.inserted_id)  # Armazena como string!
    print(f"Pedido criado com ID: {pedido.id}")
    return pedido

def buscar_pedido_por_id(id_pedido):
    try:
        # 1 Verificar o cache
        cached_pedido = get_pedido_cache(id_pedido)
        if cached_pedido:
            print("🔄 Pedido encontrado no cache!")
            return Pedido.from_dict(cached_pedido)
        
        # 2 Busca no mongoDB
        pedido_dict = colecao_pedidos.find_one({"_id": ObjectId(id_pedido)})
        if pedido_dict:
            print("Pedido encontrado no MongoDb. Atualizandoo o cahe")
            set_pedido_cache(id_pedido, pedido_dict)
            return Pedido.from_dict(pedido_dict)
        return None
    except Exception as e:
        print(f"Erro ao buscar pedido: {e}")
        return None
