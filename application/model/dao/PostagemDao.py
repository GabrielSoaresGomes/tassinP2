class PostagemDao:
    def __init__(self):
        self._lista_postagens = []
    
    @property
    def lista_postagens(self):
        return self._lista_postagens
    
    @lista_postagens.setter
    def lista_postagens(self, lista_postagens):
        self._lista_postagens = lista_postagens
    
    def inserir_postagem(self, postagem):
        self._lista_postagens.append(postagem)
    
    def gerar_id(self):
        id = 0
        for postagem in self._lista_postagens:
            id = postagem.id if postagem.id > id else id
        return id

    def ordenar_data(self):
        return sorted(self._lista_postagens, key=lambda x:x._data, reverse=True)