from src.Domain.pedido import PedidoDomain
from src.Infrastructure.Model.pedido import Pedido

from src.Domain.detalhesPedido import DetalhesPedidoDomain
from src.Infrastructure.Model.detalhesPedido import DetalhesPedido

from src.config.data_base import db 

class PedidoService:

    @staticmethod
    def salvar(id_mercado):
        new_pedido = PedidoDomain(id_mercado)
        pedido = Pedido(id_mercado = new_pedido.id_mercado)        
        db.session.add(pedido)
        db.session.commit()
        return pedido
    
    @staticmethod
    def detalhes(pedido, itens):
        for item in itens:

            id_produto = int(item.get('produto'))
            preco = float(item.get('preco'))
            qtde = int(item.get('quantidade'))

            new_detalhes = DetalhesPedidoDomain(pedido.id_pedido, id_produto, preco, qtde)
            detalhes_ = DetalhesPedido(id_pedido = new_detalhes.id_pedido, id_produto = new_detalhes.id_produto, preco = new_detalhes.preco, quantidade = new_detalhes.quantidade )        
            
            db.session.add(detalhes_)

        db.session.commit()
        return detalhes_    

    
class PedidoNaoEncontrado(Exception):
    pass
