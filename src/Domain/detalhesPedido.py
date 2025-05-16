class DetalhesPedidoDomain:
    def __init__(self, id_pedido, id_produto, preco, quantidade):
        self.id_pedido = id_pedido,
        self.id_produto = id_produto,
        self.preco = preco
        self.quantidade = quantidade
        
    def to_dict(self):
        return {
            "id_pedido": self.id_pedido,
            "id_produto": self.id_produto,
            "preco": self.preco,
            "quantidade": self.quantidade

        }
