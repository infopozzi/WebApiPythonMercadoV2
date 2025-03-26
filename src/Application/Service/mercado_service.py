from src.Domain.mercado import MercadoDomain
from src.Infrastructure.Model.mercado import Mercado
from src.config.data_base import db 
from src.Infrastructure.http.whats_app import Enviar_mensagem

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
        mercado = Mercado.query.filter(Mercado.celular == celular).first()
        if not mercado:
            new_mercado = MercadoDomain(nome, cnpj, email, celular, senha, status)
            mercado = Mercado(nome=new_mercado.nome, cnpj=new_mercado.cnpj, email=new_mercado.email, celular = new_mercado.celular, senha = new_mercado.gerarSenhaCriptografada(), status = new_mercado.status, code = new_mercado.gerarCode())        
            db.session.add(mercado)
            db.session.commit()
            Enviar_mensagem(mercado.celular, f"Plataforma de vendas para mercado, efetue ativação no nosso site http://link_ativacao com seu número de celular: {new_mercado.celular} e o código: {mercado.code}")
            return mercado
        else: raise MercadoNaoEncontrado(f"Celular: {celular} ja cadastrado, tente com outro número.")     

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

    @staticmethod
    def ativar(celular, code):
        mercado = Mercado.query.filter(Mercado.celular == celular, Mercado.code == code).first()
        if not mercado:
            raise MercadoNaoEncontrado(f"Mercado com Celular: {celular} e Código: {code} não foi encontrado.")        
        mercado.status = 1
        db.session.commit()
        return mercado

class MercadoNaoEncontrado(Exception):
    pass
