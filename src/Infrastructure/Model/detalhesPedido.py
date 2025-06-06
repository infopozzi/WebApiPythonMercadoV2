from src.config.data_base import db 

from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship

class DetalhesPedido(db.Model):
    __tablename__ = 'itensPedido'
    id = db.Column(db.Integer, primary_key=True)
    id_pedido = Column(Integer, ForeignKey('pedido.id_pedido'))
    id_produto = db.Column(db.Integer)
    preco = db.Column(db.Float())
    quantidade = db.Column(db.Integer)
    pedido = relationship("Pedido", back_populates="itens")

    def to_dict(self):
        return {"id": self.id, "id_pedido": self.id_pedido, "id_produto": self.id_produto, "preco": self.preco, "quantidade": self.quantidade}    
