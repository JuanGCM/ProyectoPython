class Factura:
    def __init__(self, fecha_pago="", dni="", pago=0):
        self.__fecha_pago = fecha_pago
        self.__dni = dni
        self.__pago = pago

    @property
    def fecha_pago(self):
        return self.__fecha_pago

    @fecha_pago.setter
    def fecha_pago(self, nuevo):
        self.__fecha_pago = nuevo

    @property
    def dni(self):
        return self.__dni

    @dni.setter
    def dni(self, nuevo):
        self.__dni = nuevo

    @property
    def pago(self):
        return self.__pago

    @pago.setter
    def pago(self, nuevo):
        self.__pago = nuevo
