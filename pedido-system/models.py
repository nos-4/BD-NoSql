from datetime import datetime

class Pedido:
    def __init__(self, nome_cliente, produto, quantidade):
        self.id = None  # Será gerado automaticamente
        self.nome_cliente = nome_cliente
        self.produto = produto
        self.quantidade = quantidade
        self.data_criacao = datetime.now()

    # método que transforma o objeto Pedido em um dicionário Python
    def to_dict(self):
        data = {
            "nome_cliente": self.nome_cliente,
            "produto": self.produto,
            "quantidade": self.quantidade,
            "data_criacao": self.data_criacao
        }
        if self.id is not None:
            from bson import ObjectId
            data["_id"] = ObjectId(self.id)  # Converte de volta para ObjectId
        return data

    # método estático que cria um objeto Pedido a partir de um dicionário
    @staticmethod
    def from_dict(data):
        pedido = Pedido(
            nome_cliente=data["nome_cliente"],
            produto=data["produto"],
            quantidade=data["quantidade"]
        )
        pedido.id = str(data["_id"])

        # Verifica se data_criacao é string e converte
        if isinstance(data["data_criacao"], str):
            pedido.data_criacao = datetime.fromisoformat(data["data_criacao"])
        else:
            pedido.data_criacao = data["data_criacao"]

        return pedido
