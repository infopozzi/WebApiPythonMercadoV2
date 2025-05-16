
class ProdutoDomain:
    def __init__(self, id_mercado, nome, preco, quantidade, imagem, status):
        self.id_mercado = id_mercado
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade
        self.imagem = imagem
        self.status = status
        
    def to_dict(self):
        return {
            "nome": self.nome,
            "preco": self.preco,
            "quantidade": self.quantidade,
            "imagem": self.imagem,
            "status": self.status
        }
