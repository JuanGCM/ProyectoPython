class Plaza:
    def __init__(self, id=0, tipo="", matricula="", ocupado=False, reservado=False):
        self.__id = id
        self.__tipo = tipo
        self.__matricula = matricula
        self.__ocupado = ocupado
        self.__reservado = reservado

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, nuevo):
        self.__id = nuevo

    @property
    def matricula(self):
        return self.__matricula

    @matricula.setter
    def matricula(self, nuevo):
        self.__matricula = nuevo

    @property
    def tipo(self):
        return self.__tipo

    @tipo.setter
    def tipo(self, nuevo):
        self.__tipo = nuevo

    @property
    def ocupado(self):
        return self.__ocupado

    @ocupado.setter
    def ocupado(self, nuevo):
        self.__ocupado = nuevo

    @property
    def reservado(self):
        return self.__reservado

    @reservado.setter
    def reservado(self, nuevo):
        self.__reservado = nuevo

