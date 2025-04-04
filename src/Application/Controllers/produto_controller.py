from flask import request, jsonify, make_response
from src.Application.Service.produto_service import ProdutoService, ProdutoNaoEncontrado

class ProdutoController:
    @staticmethod
    def obter_produto():
        try:
            data = request.get_json()
            id = data.get('id')
            produto = ProdutoService.obter(id)
            return jsonify(produto.to_dict(), 200)
        except ProdutoNaoEncontrado as e:
            return jsonify({ "message": str(e) }), 404

    @staticmethod
    def listar_produtos():
        try:
            return jsonify([produto.to_dict() for produto in ProdutoService.listar()], 200)
        except ProdutoNaoEncontrado as e:
            return jsonify({ "message": str(e) }), 404
    
    @staticmethod
    def cadastrar_produto():
        try:
            data = request.get_json()
            nome = data.get('nome')
            preco = data.get('preco')
            quantidade = data.get('quantidade')
            imagem = data.get('imagem')
            status = data.get('status')

            if not nome or not preco or not quantidade or not status:
                return make_response(jsonify({"erro": "Existem campos requeridos para preenchimento"}), 400)

            produto = ProdutoService.salvar(nome, preco, quantidade, imagem, status)

            return make_response(jsonify({
                "message": "Cadastro realiado com sucesso.",
                "mercado": produto.to_dict()
            }), 200)
        except ProdutoNaoEncontrado as e:
            return jsonify({ "message": str(e) }), 404

    @staticmethod
    def alterar_produto():
        try:
            data = request.get_json()
            id = data.get('id')
            nome = data.get('nome')
            preco = data.get('preco')
            quantidade = data.get('quantidade')
            imagem = data.get('imagem')
            status = data.get('status')

            if not id or not nome or not preco or not quantidade or not status:
                return make_response(jsonify({"erro": "Existem campos requeridos para preenchimento"}), 400)

            produto = ProdutoService.alterar(id, nome, preco, quantidade, imagem, status)

            return make_response(jsonify({
                "message": "Produto alterado com sucesso.",
                "mercado": produto.to_dict()
            }), 200)
        except ProdutoNaoEncontrado as e:
            return jsonify({ "message": str(e) }), 404
    
    @staticmethod
    def excluir_produto():
        try:
            data = request.get_json()
            id = data.get('id')

            ProdutoService.excluir(id)

            return make_response(jsonify({
                "message": "Produto excluído com sucesso."
            }), 200)
    
        except ProdutoNaoEncontrado as e:
            return jsonify({ "message": str(e) }), 404
