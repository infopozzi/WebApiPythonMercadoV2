from src.config.data_base import db 

class Produto(db.Model):
    __tablename__ = 'produto'
    id = db.Column(db.Integer, primary_key=True)
    id_mercado = db.Column(db.Integer)
    nome = db.Column(db.String(100))
    preco = db.Column(db.Float())
    quantidade = db.Column(db.Integer)
    imagem = db.Column(db.String(100))
    status = db.Column(db.Boolean)

    def to_dict(self):
        return {"id": self.id, "nome": self.nome, "preco": self.preco, "quantidade": self.quantidade, "imagem": self.imagem, "status": self.status}    
