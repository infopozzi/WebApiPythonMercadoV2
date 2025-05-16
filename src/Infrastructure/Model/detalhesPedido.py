from src.config.data_base import db 

class DetalhesPedido(db.Model):
    __tablename__ = 'itensPedido'
    id = db.Column(db.Integer, primary_key=True)
    id_pedido = db.Column(db.Integer)
    id_produto = db.Column(db.Integer)
    preco = db.Column(db.Float())
    quantidade = db.Column(db.Integer)

    def to_dict(self):
        return {"id": self.id, "id_pedido": self.id_pedido, "id_produto": self.id_produto, "preco": self.preco, "quantidade": self.quantidade}    
