from src.Domain.mercado import MercadoDomain
from src.Infrastructure.Model.mercado import Mercado
from src.config.data_base import db 

class MercadoService:
    @staticmethod
    def obter(id):
        mercado = Mercado.query.get(id)
        if not mercado:
            raise MercadoNaoEncontrado(f"Mercado com ID {id} não foi encontrado.")
        return mercado

    @staticmethod
    def listar():
        return Mercado.query.all()

    @staticmethod
    def salvar(nome, cnpj, email, celular, senha, status):
        new_mercado = MercadoDomain(nome, cnpj, email, celular, senha, status)
        mercado = Mercado(nome=new_mercado.nome, cnpj=new_mercado.cnpj, email=new_mercado.email, celular = new_mercado.celular, senha = new_mercado.senha, status = new_mercado.status)        
        db.session.add(mercado)
        db.session.commit()
        return mercado

    @staticmethod
    def alterar(id, nome, cnpj, email, celular, senha, status):
        mercado = Mercado.query.get(id)
        if not mercado:
            raise MercadoNaoEncontrado(f"Mercado com ID {id} não foi encontrado.")
        
        new_mercado = MercadoDomain(nome, cnpj, email, celular, senha, status)
        mercado = Mercado(nome=new_mercado.nome, cnpj=new_mercado.cnpj, email=new_mercado.email, celular = new_mercado.celular, senha = new_mercado.senha, status = new_mercado.status)        
        db.session.add(mercado)
        db.session.commit()
        return mercado

    @staticmethod
    def excluir(id):
        mercado = MercadoDomain(id)
        if not mercado:
            raise MercadoNaoEncontrado(f"Mercado com ID {id} não foi encontrado.")
        
        db.session.delete(mercado)
        db.session.commit()

class MercadoNaoEncontrado(Exception):
    pass
