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

            if not nome or not cnpj or not email or not celular or not senha:
                return make_response(jsonify({"erro": "Existem campos requeridos para preenchimento"}), 400)

            mercado = MercadoService.salvar(nome, cnpj, email, celular, senha, 0)

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
                {"user": mercado.email, "id": mercado.id, "exp": datetime.utcnow() + timedelta(minutes=30)},
                SECRET_KEY,
                algorithm="HS256"
            )
            
            return make_response(jsonify(token=token), 200)
    
        except MercadoNaoEncontrado as e:
            return jsonify({ "message": str(e) }), 404
        
    @staticmethod
    def validar_acesso_restrito_mercado():
        SECRET_KEY = "senhaToken"

        # Obtém o token do cabeçalho da requisição
        auth_header = request.headers.get("Authorization")
        if not auth_header:
            return 0 #jsonify({ "message":"Token é necessário!"}), 403

        parts = auth_header.split()
        if parts[0].lower() != 'bearer' or len(parts) != 2:
            return 0 #jsonify({ "message":"Cabeçalho de autorização malformado!"}), 401
        token = parts[1]

        try:
            # Decodifica o token
            decoded = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
            return decoded['id'] #jsonify({ "message":f"Bem-vindo, {decoded['user']}!"})
        except jwt.ExpiredSignatureError:
            return False #jsonify({ "message":"Token expirado! Faça login novamente."}), 401
        except jwt.InvalidTokenError:
            return False #jsonify({ "message":"Token inválido!"}), 403