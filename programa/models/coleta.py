class Coleta:
    def __init__(self, id, data, descricao, pontos, confirmado=False):
        self.set_id(id)
        self.set_data(data)
        self.set_descricao(descricao)
        self.set_pontos(pontos)
        self.set_confirmado(confirmado)

    def __str__(self):
        return f"{self.__id} - {self.__data} - {self.__descricao} - {self.__pontos}"

    def set_id(self, id):
        self.__id = id

    def set_data(self, data):
        self.__data = data

    def set_descricao(self, descricao):
        self.__descricao = descricao

    def set_pontos(self, pontos):
        self.__pontos = pontos

    def set_confirmado(self, confirmado):
        self.__confirmado = confirmado

    def get_id(self):
        return self.__id

    def get_data(self):
        return self.__data

    def get_descricao(self):
        return self.__descricao

    def get_pontos(self):
        return self.__pontos

    def get_confirmado(self):
        return self.__confirmado
