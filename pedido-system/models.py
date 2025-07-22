from datetime import datetime

class Pedido:
    def __init__(self, nome_cliente, produto, quantidade):
        self.id = None  # Será gerado automaticamente
        self.nome_cliente = nome_cliente
        self.produto = produto
        self.quantidade = quantidade
        self.data_criacao = datetime.now()

#  método que transforma o objeto Pedido em um dicionário Python,
#  para que ele possa ser enviado ao MongoDB:
    def to_dict(self):
        return {
            "_id": self.id,
            "nome_cliente": self.nome_cliente,
            "produto": self.produto,
            "quantidade": self.quantidade,
            "data_criacao": self.data_criacao
        }
# método faz o contrário de to_dict: 
# ele recebe um dicionário e cria um objeto Pedido a partir desses dados.
    @staticmethod
    def from_dict(data):
        pedido = Pedido(
            nome_cliente=data["nome_cliente"],
            produto=data["produto"],
            quantidade=data["quantidade"]
        )
        pedido.id = data["_id"]
        pedido.data_criacao = data["data_criacao"]
        return pedido
