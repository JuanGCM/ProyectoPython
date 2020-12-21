from ticket import Ticket


class TicketAbonado(Ticket):

    def __init__(self, fecha_entrada, fecha_salida, matricula, tipo, idplaza, pin, coste, dni=""):
        super().__init__(fecha_entrada,fecha_salida,matricula, tipo,idplaza,pin,coste)
        self.__dni = dni

    @property
    def dni(self):
        return self.__dni

    @dni.setter
    def dni(self, nuevo):
        self.__dni = nuevo
