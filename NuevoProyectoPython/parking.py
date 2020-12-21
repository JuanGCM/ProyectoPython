class Parking:
    def __init__(self, nplaza=0, tipo="", tarifa=0):
        self.__nplaza = nplaza
        self.__tipo = tipo
        self.__tarifa = tarifa

    @property
    def nplaza(self):
        return self.__nplaza

    @nplaza.setter
    def nplaza(self, nuevo):
        self.__nplaza = nuevo

    @property
    def tipo(self):
        return self.__tipo

    @tipo.setter
    def tipo(self, nuevo):
        self.__tipo = nuevo

    @property
    def tarifa(self):
        return self.__tarifa

    @tarifa.setter
    def tarifa(self, nuevo):
        self.__tarifa = nuevo

    def numero_plazas(self):
        return "Numero de plazas libres para "+ str(self.__tipo)+ ": "+ str(self.__nplaza)

    def informacion(self):
        print("Tipo de Plaza: ", self.__tipo, "\nTarifa: ", self.__tarifa)
