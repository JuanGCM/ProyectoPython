import pickle
import tkinter
import random
from datetime import datetime
from controlador_menu import *
from parking import Parking
from ticket import Ticket
from ticketabonado import TicketAbonado
from plaza import Plaza
from usuario import Usuario


def aleatorio(a, b):
    return round(random.randint(a, b), 3)


def retiraVehiculoAbo(matricula, pin, idplaza, plazas, tickets_abonados):

    cont = 0

    for i in plazas:
        if i.matricula == matricula:
            i.ocupado = False

    for j in tickets_abonados:
        if j.pin == int(pin) and j.idplaza == int(idplaza):
            del tickets_abonados[cont]
            print("El vehiculo se ha retirado del parking...")
        cont += 1


def depositarVehiculoAbo(matricula, dni, plazas, tickets_abonados):

    dt = datetime.now()

    for i in plazas:
        if i.matricula == matricula:
            i.ocupado = True
            tickets_abonados += [TicketAbonado("{}/{}/{}".format(dt.day, dt.month, dt.year),"",matricula,i.tipo,i.id, aleatorio(100000, 999999), 90,dni)]
            print("El montacargas esta llevando el vehiculo a su plaza asignada...")


def retiraVehiculo(matricula, idplaza, pin, plazas, tickets, parkins):

    dt = datetime.now()
    fecha = ""
    coste = 0
    for i in tickets:
        if i.pin == int(pin):
            coste = i.coste
            fecha = i.fecha_entrada

    lista = fecha.split('/')
    dias = int(dt.day) - int(lista[0])
    horas = dias * 24
    minutos = horas * 60
    total = minutos * coste

    print("La tarifa es de ", coste, "€ por minuto.")
    print("Acabas de pagar ", total, "€ por retirar el vehiculo.")

    for i in parkins:
        for j in tickets:
            if i.tipo == j.tipo:
                if j.pin == int(pin):
                    i.nplaza += 1
                    #pago += [Pagos("{}/{}/{}".format(dt.day, dt.month, dt.year), round(monto * 100) / 100)]
    cont = 0

    for k in plazas:
        if k.matricula == matricula and k.id == int(idplaza):
            del plazas[cont]
            print("El vehiculo se ha retirado del parking...")
        cont += 1

    for i in parkins:
        print(i.nplaza,i.tipo)


def depositarVehiculo(matricula, tipo, plazas, tickets):

    dt = datetime.now()
    for i in parkins:
        if i.tipo == tipo:
            if i.nplaza > 0:
                print("El montacargas esta llevando el vehiculo a su plaza...")
                plazas += [Plaza(len(plazas)+1,tipo,matricula,True,False)]
                tickets += [Ticket("{}/{}/{}".format(dt.day, dt.month, dt.year),"",matricula,tipo,len(plazas), aleatorio(100000, 999999), i.tarifa)]
                i.nplaza -= 1
            else:
                print("Ya no quedan plazas en el parking de " + i.tipo)
                break
    for j in parkins:
        print(j.numero_plazas())


def opcionRetiraVehiculoAbonado(matri, pin, plazas):

    print(f"Matricula: {matri}")
    print(f"Pin: {pin}")
    for i in plazas:
        if i.matricula == matri:
            print(f"Id plaza: {i.id}")

    ventanaRetiAbo = tkinter.Tk()
    ventanaRetiAbo.geometry("500x400")

    pregunta1 = tkinter.Label(ventanaRetiAbo, text="Ingresa la matricula: ")
    matricula = tkinter.Entry(ventanaRetiAbo)
    pregunta2 = tkinter.Label(ventanaRetiAbo, text="Ingresa el pin: ")
    elpin = tkinter.Entry(ventanaRetiAbo)
    pregunta3 = tkinter.Label(ventanaRetiAbo, text="Ingresa el id de plaza: ")
    idplaza = tkinter.Entry(ventanaRetiAbo)
    boton = tkinter.Button(ventanaRetiAbo, text="Enviar", command=lambda: retiraVehiculoAbo(matricula.get(), elpin.get(), idplaza.get(), plazas, tickets_abonados))
    pregunta1.pack()
    matricula.pack()
    pregunta2.pack()
    elpin.pack()
    pregunta3.pack()
    idplaza.pack()
    boton.pack()

    ventanaRetiAbo.mainloop()


def opcionDepositaVehiculoAbonado(dni, matri):

    print(f"Matricula: {matri}")
    print(f"DNI: {dni}")

    ventanaDepoAbo = tkinter.Tk()
    ventanaDepoAbo.geometry("500x400")

    pregunta1 = tkinter.Label(ventanaDepoAbo, text="Ingresa la matricula: ")
    matricula = tkinter.Entry(ventanaDepoAbo)
    pregunta2 = tkinter.Label(ventanaDepoAbo, text="Ingresa tu dni: ")
    dni = tkinter.Entry(ventanaDepoAbo)
    boton = tkinter.Button(ventanaDepoAbo, text="Enviar", command=lambda: depositarVehiculoAbo(matricula.get(), dni.get(), plazas, tickets_abonados))
    pregunta1.pack()
    matricula.pack()
    pregunta2.pack()
    dni.pack()
    boton.pack()

    ventanaDepoAbo.mainloop()


def opcionRetiraVehiculo(pin):

    for i in tickets:
        print(i.info(pin))

    ventanaRetira = tkinter.Tk()
    ventanaRetira.geometry("500x400")

    pregunta1 = tkinter.Label(ventanaRetira, text="Ingresa la matricula: ")
    matricula = tkinter.Entry(ventanaRetira)
    pregunta2 = tkinter.Label(ventanaRetira, text="Ingresa el numero de plaza: ")
    plaza = tkinter.Entry(ventanaRetira)
    pregunta3 = tkinter.Label(ventanaRetira, text="Ingresa el pin: ")
    pin = tkinter.Entry(ventanaRetira)
    boton = tkinter.Button(ventanaRetira, text="Enviar", command=lambda: retiraVehiculo(matricula.get(), plaza.get(), pin.get(),plazas, tickets, parkins))
    pregunta1.pack()
    matricula.pack()
    pregunta2.pack()
    plaza.pack()
    pregunta3.pack()
    pin.pack()
    boton.pack()

    ventanaRetira.mainloop()


def opcionDepositaVehiculo():
    ventanaDeposita = tkinter.Tk()
    ventanaDeposita.geometry("500x400")

    pregunta1 = tkinter.Label(ventanaDeposita, text="Ingresa la matricula:")
    matricula = tkinter.Entry(ventanaDeposita)
    pregunta2 = tkinter.Label(ventanaDeposita, text="Ingresa el tipo (turismo,motocicleta,caravana): ")
    tipo = tkinter.Entry(ventanaDeposita)
    boton = tkinter.Button(ventanaDeposita, text="Enviar", command=lambda: depositarVehiculo(matricula.get(), tipo.get(), plazas, tickets))

    pregunta1.pack()
    matricula.pack()
    pregunta2.pack()
    tipo.pack()
    boton.pack()

    ventanaDeposita.mainloop()


def menuAdmin():
    ventanaAdmin = tkinter.Tk()
    ventanaAdmin.geometry("500x400")

    menu = tkinter.Label(ventanaAdmin, text="¿Que deseas consultar?")
    opcion1 = tkinter.Button(ventanaAdmin, text="Estado del Parking")
    opcion2 = tkinter.Button(ventanaAdmin, text="Facturación")
    opcion3 = tkinter.Button(ventanaAdmin, text="Abonados")
    opcion4 = tkinter.Button(ventanaAdmin, text="Abonos")
    opcion5 = tkinter.Button(ventanaAdmin, text="Caducidad de Abonos")

    menu.pack()
    opcion1.pack()
    opcion2.pack()
    opcion3.pack()
    opcion4.pack()
    opcion5.pack()

    ventanaAdmin.mainloop()


def menuCliente(esabonado, pin, dni, matri):
    ventanaMenu = tkinter.Tk()
    ventanaMenu.geometry("500x400")

    for i in parkins:
        numeroPlazas = tkinter.Label(ventanaMenu, text=i.numero_plazas())
        numeroPlazas.pack()

    menu = tkinter.Label(ventanaMenu, text="¿Que deseas hacer?")
    if esabonado:
        if pin == 0:
            opcion1 = tkinter.Button(ventanaMenu, text="Depositar Vehiculo", command=lambda: opcionDepositaVehiculo())
            opcion1.pack()
        else:
            opcion2 = tkinter.Button(ventanaMenu, text="Retirar Vehiculo", command=lambda: opcionRetiraVehiculo(pin))
            opcion2.pack()

    else:
        if pin == 0:
            opcion3 = tkinter.Button(ventanaMenu, text="Depositar Abonado", command=lambda: opcionDepositaVehiculoAbonado(dni, matri))
            opcion3.pack()
        else:
            opcion4 = tkinter.Button(ventanaMenu, text="Retirar Vehiculo Abonado", command=lambda: opcionRetiraVehiculoAbonado(matri,pin,plazas))
            opcion4.pack()

    menu.pack()
    ventanaMenu.mainloop()


def menulogin(email,contra):

    esOk = True
    esAdmin = True
    esAbonado = True
    pin = 0
    dni = ""
    matri =""
    nombre = ""

    for i in usuarios:
        if email == i.email:
            if contra == i.contrasena:
                nombre = i.nombre
                pin = i.pin
                dni = i.dni
                matri = i.matri_vehiculo
                esOk = False
                if i.esAdmin:
                    esAdmin = False
                elif i.esAbonado:
                    esAbonado = False

    if esOk:
        return print("Email o Contraseña incorrecta")

    else:
        if esAdmin:
            print(f"Bienvenido {nombre}")
            menuCliente(esAbonado, pin,dni,matri)
        else:
            print(f"Bienvenido administrador {nombre}")
            menuAdmin()


ficheroPark = open("lista_parking","rb")
parkins = pickle.load(ficheroPark)
ficheroPark.close()

fichUsu = open("listado_usuarios","rb")
usuarios = pickle.load(fichUsu)
fichUsu.close()

ficheroTic = open("listado_tickets","rb")
tickets = pickle.load(ficheroTic)
ficheroTic.close()

ficheroTicA = open("listado_tickets_abonados","rb")
tickets_abonados = pickle.load(ficheroTicA)
ficheroTicA.close()

ficheroPl = open("listado_plazas","rb")
plazas = pickle.load(ficheroPl)
ficheroPl.close()


ventana = tkinter.Tk()
ventana.geometry("500x400")

label1 = tkinter.Label(ventana, text="Email")
email = tkinter.Entry(ventana)
label2 = tkinter.Label(ventana, text="Contraseña")
contra = tkinter.Entry(ventana)
entrar = tkinter.Button(ventana, text="Entrar", command=lambda: menulogin(email.get(), contra.get()))
label1.pack()
email.pack()
label2.pack()
contra.pack()
entrar.pack()

ventana.mainloop()
