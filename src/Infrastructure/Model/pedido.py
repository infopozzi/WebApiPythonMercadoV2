from src.config.data_base import db 

class Pedido(db.Model):
    __tablename__ = 'pedido'
    id_pedido = db.Column(db.Integer, primary_key=True)
    id_mercado = db.Column(db.Integer)

    def to_dict(self):
        return {"id_pedido": self.id_pedido, "id_mercado": self.id_mercado }    
