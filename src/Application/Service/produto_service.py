from src.Domain.produto import ProdutoDomain
from src.Infrastructure.Model.produto import Produto
from src.config.data_base import db 

class ProdutoService:
    @staticmethod
    def obter(id):
        produto = Produto.query.get(id)
        if not produto:
            raise ProdutoNaoEncontrado(f"Produto com ID {id} não foi encontrado.")
        return produto

    @staticmethod
    def listar(id_mercado):
        return Produto.query.filter_by(id_mercado=id_mercado).all()

    @staticmethod
    def salvar(id_mercado, nome, preco, quantidade, imagem, status):
        new_produto = ProdutoDomain(id_mercado, nome, preco, quantidade, imagem, status)
        produto = Produto(id_mercado = new_produto.id_mercado, nome=new_produto.nome, preco=new_produto.preco, quantidade=new_produto.quantidade, imagem = new_produto.imagem, status = new_produto.status )        
        db.session.add(produto)
        db.session.commit()
        return produto

    @staticmethod
    def alterar(id, nome, preco, quantidade, imagem, status):
        produto = Produto.query.get(id)
        if not produto:
            raise ProdutoNaoEncontrado(f"Produto com ID {id} não foi encontrado.")
        
        #new_produto = ProdutoDomain(nome, preco, quantidade, imagem, status)
        #produto = Produto(id = id, nome=new_produto.nome, preco=new_produto.preco, quantidade=new_produto.quantidade, imagem = new_produto.imagem, status = new_produto.status)        
        produto.nome = nome
        produto.preco = preco
        produto.quantidade = quantidade
        produto.imagem = imagem
        produto.status = status

        db.session.commit()
        return produto
    
    @staticmethod
    def baixar_estoque(id, quantidade):
        produto = Produto.query.get(id)
        if not produto:
            raise ProdutoNaoEncontrado(f"Produto com ID {id} não foi encontrado.")
        
        produto.quantidade = produto.quantidade - quantidade

        db.session.commit()
        return produto

    @staticmethod
    def excluir(id):
        produto = Produto.query.get(id)
        if not produto:
            raise ProdutoNaoEncontrado(f"Produto com ID {id} não foi encontrado.")
        
        db.session.delete(produto)
        db.session.commit()

class ProdutoNaoEncontrado(Exception):
    pass
