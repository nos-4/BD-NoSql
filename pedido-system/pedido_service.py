from models import Pedido
from database import get_database
from bson import ObjectId #usado para converter strings em IDs válidos do MongoDB.
from cache import get_pedido_cache, set_pedido_cache , redis_client

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
            print("Pedido encontrado no cache!")
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

def atualizar_pedido(id_pedido, novo_nome=None, novo_produto=None, nova_quantidade=None):
    try:
        campos_para_atualizar = {}

        if novo_nome:
            campos_para_atualizar["nome_cliente"] = novo_nome
        if novo_produto:
            campos_para_atualizar["produto"] = novo_produto
        if nova_quantidade:
            campos_para_atualizar["quantidade"] = nova_quantidade

        if not campos_para_atualizar:
            print("Nenhum campo fornecido para atualização.")
            return False

        resultado = colecao_pedidos.update_one(
            {"_id": ObjectId(id_pedido)},
            {"$set": campos_para_atualizar}
        )

        if resultado.modified_count > 0:
            print(" Pedido atualizado com sucesso!")
            # Atualiza cache (busca novo pedido do Mongo e atualiza)
            pedido_atualizado = colecao_pedidos.find_one({"_id": ObjectId(id_pedido)})
            set_pedido_cache(id_pedido, pedido_atualizado)
            return True
        else:
            print(" Pedido não encontrado ou dados iguais aos anteriores.")
            return False
    except Exception as e:
        print(f"Erro ao atualizar pedido: {e}")
        return False

def cancelar_pedido(id_pedido):
    try:
        resultado = colecao_pedidos.delete_one({"_id": ObjectId(id_pedido)})
        if resultado.deleted_count > 0:
            print("Pedido cancelado com sucesso!")
            # Remove do cache também
            redis_client.delete(f"pedido:{id_pedido}")
            return True
        else:
            print(" Pedido não encontrado para cancelamento.")
            return False
    except Exception as e:
        print(f"Erro ao cancelar pedido: {e}")
        return False
