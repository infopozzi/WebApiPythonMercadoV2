from src.config.data_base import db 
import hashlib

class Mercado(db.Model):
    __tablename__ = 'mercado'
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100))
    cnpj = db.Column(db.String(20))
    email = db.Column(db.String(100))
    celular = db.Column(db.String(20))
    senha = db.Column(db.String(300))
    status = db.Column(db.Boolean)

    def to_dict(self):
        return {"id": self.id, "nome": self.nome, "cnpj": self.cnpj, "email": self.email, "celular": self.celular, "status": self.status}    

    def criptografar_senha(self, senha):
            return hashlib.sha256(senha.encode()).hexdigest()