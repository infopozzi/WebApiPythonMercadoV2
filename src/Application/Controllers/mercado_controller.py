from flask import request, jsonify, make_response
from src.Application.Service.mercado_service import MercadoService, MercadoNaoEncontrado
from datetime import datetime, timedelta
import jwt

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
    
    @staticmethod
    def ativar_mercado():
        try:
            data = request.get_json()
            celular = data.get('celular')
            code = data.get('code')

            mercado = MercadoService.ativar(celular, code)

            return make_response(jsonify({
                "mensagem": "Mercado ativado com sucesso",
                "mercado": mercado.to_dict()
            }), 200)
    
        except MercadoNaoEncontrado as e:
            return jsonify({ "message": str(e) }), 404

    @staticmethod
    def login_mercado():
        try:
            SECRET_KEY = "senhaToken"

            data = request.get_json()
            email = data.get('email')
            senha = data.get('senha')

            mercado = MercadoService.login(email, senha)

            # Gerar o token com expiração
            token = jwt.encode(
                {"user": mercado.email, "exp": datetime.utcnow() + timedelta(minutes=30)},
                SECRET_KEY,
                algorithm="HS256"
            )
            
            return make_response(jsonify(token=token), 200)
    
        except MercadoNaoEncontrado as e:
            return jsonify({ "message": str(e) }), 404