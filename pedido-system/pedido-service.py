from models import Pedido
from database import get_database
from bson import ObjectId #usado para converter strings em IDs válidos do MongoDB.

db = get_database()
colecao_pedidos = db["pedidos"] #tabela onde os pedidos serão armazenados.


def criar_pedido(nome_cliente, produto, quantidade):
    if not all([nome_cliente, produto, quantidade]):
        raise ValueError("Todos os campos são obrigatórios.")
    
    pedido = Pedido(nome_cliente, produto, quantidade)
    result = colecao_pedidos.insert_one(pedido.to_dict())
    pedido.id = result.inserted_id #Armazena o ID gerado automaticamente pelo Mongo (ObjectId) no objeto.
    print(f"Pedido criado com ID: {pedido.id}")
    return pedido

def buscar_pedido_por_id(id_pedido):
    try:
        pedido_dict = colecao_pedidos.find_one({"_id": ObjectId(id_pedido)}) #Converte o ID (string) para ObjectId e busca no banco
        if pedido_dict:
            return Pedido.from_dict(pedido_dict)
        return None
    except Exception as e:
        print(f"Erro ao buscar pedido: {e}")
        return None
