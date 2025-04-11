from flask import request, jsonify, make_response
from src.Application.Service.produto_service import ProdutoService, ProdutoNaoEncontrado

class ProdutoController:
    @staticmethod
    def obter_produto():
        try:
            id = request.args.get('id')
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
            nome = request.form.get('nome')
            preco = float(request.form.get('preco'))
            quantidade = int(request.form.get('quantidade'))
            status = int(request.form.get('status'))
            imagem = request.files.get('imagem') 

            if not id or not nome or not preco or not quantidade or not status:
                return make_response(jsonify({"erro": "Existem campos requeridos para preenchimento"}), 400)

            nome_imagem = ''
            if imagem:
               imagem.save(f'./public/imagens/{imagem.filename}')
               nome_imagem = 'http://127.0.0.1:5000//imagens/' + imagem.filename

            produto = ProdutoService.salvar(nome, preco, quantidade, nome_imagem, status)

            return make_response(jsonify({
                "message": "Produto cadastrado com sucesso.",
                "mercado": produto.to_dict()
            }), 200)
        except ProdutoNaoEncontrado as e:
            return jsonify({ "message": str(e) }), 404

    @staticmethod
    def alterar_produto():
        try:
            id = request.form.get('id')
            nome = request.form.get('nome')
            preco = float(request.form.get('preco'))
            quantidade = int(request.form.get('quantidade'))
            status = int(request.form.get('status'))
            imagem = request.files.get('imagem') 
            imagem_existente = request.form.get('imagem_existente') 

            if not id or not nome or not preco or not quantidade:
                return make_response(jsonify({"erro": "Existem campos requeridos para preenchimento"}), 400)
            
            nome_imagem = imagem_existente
            if imagem:
               imagem.save(f'./public/imagens/{imagem.filename}')
               nome_imagem = 'http://127.0.0.1:5000//imagens/' + imagem.filename

            produto = ProdutoService.alterar(id, nome, preco, quantidade, nome_imagem, status)

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
