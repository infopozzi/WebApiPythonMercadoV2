from flask import request, jsonify, make_response
from src.Application.Service.pedido_service import PedidoService, PedidoNaoEncontrado
from src.Application.Controllers.mercado_controller import MercadoController  
from src.Application.Service.produto_service import ProdutoService

class PedidoController:

    @staticmethod
    def cadastrar_pedido():
        try:
            id_mercado = MercadoController.validar_acesso_restrito_mercado()

            if (id_mercado > 0):
                data = request.get_json()
                itens = data.get('itens')

                if not itens:
                    return make_response(jsonify({"erro": "Existem campos requeridos para preenchimento"}), 400)

                pedido = PedidoService.salvar(id_mercado)
                PedidoService.detalhes(pedido, itens)

                for item in itens:
                    id_produto = int(item.get('produto'))            
                    qtde = int(item.get('quantidade'))
                    ProdutoService.baixar_estoque(id_produto, qtde)

                return make_response(jsonify({
                    "message": f"Pedido cadastrado com sucesso, número do pedido: {pedido.id_pedido}"
                }), 200)
            else:
                return jsonify({ "message": "Sessão expirou ou token inválido" }, 404)

        except PedidoNaoEncontrado as e:
            return jsonify({ "message": str(e) }), 404
        

    @staticmethod
    def listar_pedidos():
        try:
            id_mercado = MercadoController.validar_acesso_restrito_mercado()
            if (id_mercado > 0):
                data = request.get_json()
                dataInicio = data.get('dataInicio')
                dataTermino = data.get('dataTermino')

                return jsonify([pedido.to_dict() for pedido in PedidoService.listar(id_mercado, dataInicio, dataTermino)], 200)
            else: 
                return jsonify({ "message": "Sessão expirou ou token inválido" }), 404
        except PedidoNaoEncontrado as e:
            return jsonify({ "message": str(e) }), 404