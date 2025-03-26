from src.Application.Controllers.user_controller import UserController
from src.Application.Controllers.mercado_controller import MercadoController

from flask import jsonify, make_response

def init_routes(app):    
    @app.route('/api', methods=['GET'])
    def health():
        return make_response(jsonify({
            "mensagem": "API - OK; Docker - Up",
        }), 200)
    
    
    
    @app.route('/usuario/cadastrar', methods=['POST'])
    def cadastrar_usuario():
        return UserController.cadastrar_usuario()
    
    @app.route('/usuario/listar', methods=['GET'])
    def listar_usuarios():
        return UserController.listar_usuarios()    
    

    
    @app.route('/mercado', methods=['POST'])
    def registrar_mercado():
        return MercadoController.registrar_mercado()
    
    @app.route('/listar_mercados', methods=['GET'])
    def listar_mercados():
        return MercadoController.listar_mercados()

