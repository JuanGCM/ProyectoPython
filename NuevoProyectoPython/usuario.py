class Usuario:

    def __init__(self, nombre="", apellidos="", email="",contrasena="", esAdmin=False, dni="", tar_credito=0, pin=0, esAbonado=False, tipo_abono="", matri_vehiculo=""):
        self.__nombre = nombre
        self.__apellidos = apellidos
        self.__email = email
        self.__contrasena = contrasena
        self.__esAdmin = esAdmin
        self.__dni = dni
        self.__tar_credito = tar_credito
        self.__pin = pin
        self.__esAbonado = esAbonado
        self.__tipo_abono = tipo_abono
        self.__matri_vehiculo = matri_vehiculo

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, nuevo):
        self.__nombre = nuevo

    @property
    def apellidos(self):
        return self.__apellidos

    @apellidos.setter
    def apellidos(self, nuevo):
        self.__apellidos = nuevo

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, nuevo):
        self.__email = nuevo

    @property
    def contrasena(self):
        return self.__contrasena

    @contrasena.setter
    def contrasena(self, nuevo):
        self.__contrasena = nuevo

    @property
    def esAdmin(self):
        return self.__esAdmin

    @esAdmin.setter
    def esAdmin(self, nuevo):
        self.__esAdmin = nuevo

    @property
    def dni(self):
        return self.__dni

    @dni.setter
    def dni(self, nuevo):
        self.__dni = nuevo

    @property
    def tar_credito(self):
        return self.__tar_credito

    @tar_credito.setter
    def tar_credito(self, nuevo):
        self.__tar_credito = nuevo

    @property
    def pin(self):
        return self.__pin

    @pin.setter
    def pin(self, nuevo):
        self.__pin = nuevo

    @property
    def esAbonado(self):
        return self.__esAbonado

    @esAbonado.setter
    def esAbonado(self, nuevo):
        self.__esAbonado = nuevo

    @property
    def tipo_abono(self):
        return self.__tipo_abono

    @tipo_abono.setter
    def tipo_abono(self, nuevo):
        self.__tipo_abono = nuevo

    @property
    def matri_vehiculo(self):
        return self.__matri_vehiculo

    @matri_vehiculo.setter
    def matri_vehiculo(self, nuevo):
        self.__matri_vehiculo = nuevo
