from datetime import datetime

class Postagem:
    def __init__(self,id, estagiario, mensagem):
        self._id = id
        self._estagiario = estagiario
        self._mensagem = mensagem
        self._data = datetime.now().strftime("%d/%m/%Y")

    @property
    def id(self):
        return self._id
    
    @id.setter
    def id(self, id):
        self._id = id

    @property
    def estagiario(self):
        return self._estagiario

    @estagiario.setter
    def estagiario(self, estagiario):
        self._estagiario = estagiario

    @property
    def mensagem(self):
        return self._mensagem

    @mensagem.setter
    def mensagem(self, mensagem):
        self._mensagem = mensagem

    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, data):
        self._data = data
    
    

