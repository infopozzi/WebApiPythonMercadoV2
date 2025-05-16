class PedidoDomain:
    def __init__(self, id_mercado):
        self.id_mercado = id_mercado        
        
    def to_dict(self):
        return {
            "id_mercado": self.id_mercado,
            "id_pedido": self.id_pedido
        }
