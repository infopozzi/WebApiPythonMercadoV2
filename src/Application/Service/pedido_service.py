from src.Domain.pedido import PedidoDomain
from src.Infrastructure.Model.pedido import Pedido

from src.Domain.detalhesPedido import DetalhesPedidoDomain
from src.Infrastructure.Model.detalhesPedido import DetalhesPedido

from src.config.data_base import db 
from datetime import datetime

from sqlalchemy import func

class PedidoService:

    @staticmethod
    def salvar(id_mercado):
        new_pedido = PedidoDomain(id_mercado)
        pedido = Pedido(id_mercado = new_pedido.id_mercado) 
        pedido.dt_pedido = datetime.now()
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
    
    @staticmethod
    def listar(id_mercado, data_inicio_str=None, data_termino_str=None):
        query = Pedido.query.filter_by(id_mercado=id_mercado)

        if data_inicio_str and data_termino_str:
            try:
                data_inicio = datetime.strptime(data_inicio_str, "%d/%m/%Y")
                data_termino = datetime.strptime(data_termino_str, "%d/%m/%Y")

                # filtro por intervalo de datas
                query = query.filter(
                    Pedido.dt_pedido >= data_inicio,
                    Pedido.dt_pedido <= data_termino
                )
            except ValueError:
                # você pode tratar erro de data inválida aqui se quiser
                pass

        return query.all()
        
class PedidoNaoEncontrado(Exception):
    pass
