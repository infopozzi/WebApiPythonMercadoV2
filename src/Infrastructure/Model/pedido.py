from src.config.data_base import db 

from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship

class Pedido(db.Model):
    __tablename__ = 'pedido'
    id_pedido = db.Column(db.Integer, primary_key=True)
    id_mercado = db.Column(db.Integer)
    dt_pedido = db.Column(db.DateTime)
    itens = relationship("DetalhesPedido", back_populates="pedido")

    def to_dict(self):
        total = sum(item.preco * item.quantidade for item in self.itens)
        return {
            "id_pedido": self.id_pedido,
            "id_mercado": self.id_mercado,
            "dt_pedido": self.dt_pedido.strftime('%Y-%m-%d %H:%M:%S') if self.dt_pedido else None,
            "total_pedido": total
        }