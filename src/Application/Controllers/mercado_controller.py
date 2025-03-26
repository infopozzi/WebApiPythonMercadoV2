from flask import request, jsonify, make_response
from src.Application.Service.mercado_service import MercadoService

class MercadoController:
    @staticmethod
    def cadastrar_mercado():
        try:
            data = request.get_json()
            nome = data.get('nome')
            cnpj = data.get('cnpj')
            email = data.get('email')
            celular = data.get('celular')
            senha = data.get('senha')
            status = data.get('status')

            if not nome or not cnpj or not email or not celular or not senha:
                return make_response(jsonify({"erro": "Existem campos requeridos para preenchimento"}), 400)

            mercado = MercadoService.salvar(nome, cnpj, email, celular, senha, status)

            return make_response(jsonify({
                "message": "Cadastro realiado com sucesso, sera enviado por whatsaap as instruções de ativação no telefone cadastrado.",
                "mercado": mercado.to_dict()
            }), 200)
        except MercadoNaoEncontrado as e:
            return jsonify({ "message": str(e) }), 404

    @staticmethod
    def listar_mercados():
        try:
            return jsonify([mercado.to_dict() for mercado in MercadoService.listar()], 200)
        except MercadoNaoEncontrado as e:
            return jsonify({ "message": str(e) }), 404
    
