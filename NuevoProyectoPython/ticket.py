class Ticket:
    def __init__(self, fecha_entrada="", fecha_salida="", matricula="", tipo="", idplaza=0, pin=0, coste=0):
        self.__fecha_entrada = fecha_entrada
        self.__fecha_salida = fecha_salida
        self.__matricula = matricula
        self.__tipo = tipo
        self.__idplaza = idplaza
        self.__pin = pin
        self.__coste = coste

    @property
    def fecha_entrada(self):
        return self.__fecha_entrada

    @fecha_entrada.setter
    def fecha_entrada(self, nuevo):
        self.__fecha_entrada = nuevo

    @property
    def fecha_salida(self):
        return self.__fecha_salida

    @fecha_salida.setter
    def fecha_salida(self, nuevo):
        self.__fecha_salida = nuevo

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
    def idplaza(self):
        return self.__idplaza

    @idplaza.setter
    def idplaza(self, nuevo):
        self.__idplaza = nuevo

    @property
    def pin(self):
        return self.__pin

    @pin.setter
    def pin(self, nuevo):
        self.__pin = nuevo

    @property
    def coste(self):
        return self.__coste

    @coste.setter
    def coste(self, nuevo):
        self.__coste = nuevo

    def info(self,pin):
        if self.__pin == pin:
            print("Matricula del coche: ", self.__matricula, "\nNº de Plaza: ", self.__idplaza, "\nPin: ", self.__pin)
