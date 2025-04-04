from src.Application.Controllers.user_controller import UserController
from src.Application.Controllers.mercado_controller import MercadoController
from src.Application.Controllers.produto_controller import ProdutoController

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
    

    
    @app.route('/mercado/cadastrar', methods=['POST'])
    def cadastrar_mercado():
        return MercadoController.cadastrar_mercado()
    
    @app.route('/mercado/listar', methods=['GET'])
    def listar_mercados():
        return MercadoController.listar_mercados()
    
    @app.route('/mercado/ativar', methods=['POST'])
    def ativar_mercado():
        return MercadoController.ativar_mercado()
    
    @app.route('/mercado/login', methods=['POST'])
    def login_mercado():
        return MercadoController.login_mercado()
    
    @app.route('/mercado/validar_acesso_restrito', methods=['POST'])
    def validar_acesso_restrito_mercado():
        return MercadoController.validar_acesso_restrito_mercado()
    

       
    @app.route('/produto/cadastrar', methods=['POST'])
    def cadastrar_produto():
        return ProdutoController.cadastrar_produto()
    
    @app.route('/produto/alterar', methods=['POST'])
    def alterar_produto():
        return ProdutoController.alterar_produto()
    
    @app.route('/produto/listar', methods=['GET'])
    def listar_produto():
        return ProdutoController.listar_produtos()
    
    @app.route('/produto/obter', methods=['GET'])
    def obter_produto():
        return ProdutoController.obter_produto()
    
    @app.route('/produto/excluir', methods=['POST'])
    def excluir_produto():
        return ProdutoController.excluir_produto()
