# ProyectoPython
*Usuarios para probar el proyecto:

Usuario administrador:

   email       -   contraseña
   
luismi@gmail.com - luismi123

Usuario no abonado(Depositar Coche):

   email       -   contraseña
   
luis@gmail.com - luis123

Usuario no abonado(Retirar Coche):

   email       -   contraseña
   
oscar@gmail.com - oscar123

Usuario abonado(Depositar abonado):

   email       -   contraseña
   
juan@gmail.com - juan123

Usuario abonado(Retirar abonado):

  email       -   contraseña
   
maria@gmail.com - maria123


Clases y sus listas:

Clase Parking:(nplazas,tipo,tarifa)

Lista:

lista_parking = [
       Parking(67,"turismo",0.12),
       Parking(13,"motocicleta",0.08),
       Parking(13,"caravana",0.10)]


Clase Usuarios:(nombre,apellidos,email,contrasena,esAdmin,dni,tar_credito,pin,esAbonado,tipo_abono,matri_vehiculo)

Lista:

listado_usuarios = [
            Usuario("Antonio", "Wally", "antonio@gmail.com", "antonio123", False, "69427754y", 75698425874, 166448, False, "", ""),
            Usuario("Fiorela", "Laghter", "fiorela@gmail.com", "fiorela123", False, "36449855o", 79988556241, 615762, False, "", ""),
            Usuario("Oscar", "Leiva", "oscar@gmail.com", "oscar123", False, "21057987p", 77445158694, 615897, False, "", ""),
            Usuario("Carla", "Mandal", "carla@gmail.com", "carla123", False, "55266677h", 78445005998, 689987, False, "", ""),
            Usuario("Luis", "Rodriguez", "luis@gmail.com", "luis123", False, "56971005v", 73360059874, 0, False, "", ""),
            Usuario("Angela", "Muñoz", "angela@gmail.com", "angela123",False, "95887225b", 89745844057, 0, False, "", ""),
            Usuario("Luismi", "Triana", "luismi@gmail.com", "luismi123", True, "", 0, 0, False, "", ""),
            Usuario("Miguel", "Triana", "miguel@gmail.com", "miguel123", True, "", 0, 0, False, "", ""),
            Usuario("Juan", "Marlon", "juan@gmail.com", "juan123", False, "75841245t", 78454164544, 0, True, "mensual", "olv1"),
            Usuario("Maria", "Marge", "maria@gmail.com", "maria123", False, "48484848y", 12455454515, 965587, True, "trimestral", "d4ne"),
            Usuario("Jhon", "Edgar", "jhon@gmail.com", "jhon123", False, "84654564e", 78745451512, 247584, True, "anual", "hero"),
            Usuario("Frank", "Podgar", "frank@gmail.com", "frank123", False, "87484845s", 848156156115, 689248, True, "anual", "gh4r"),
            Usuario("Omar", "Moron", "omar@gmail.com", "omar123", False, "26699005x", 75699300566, 633998, True, "anual", "tr10"),
            Usuario("Lucas", "Hateo", "lucas@gmail.com", "lucas123", False, "21004875u", 77784456250, 674847, True, "anual", "c4r5"),
            Usuario("Hana", "Montana", "hana@gmail.com", "hana123", False, "66984558q", 74101474105, 690045, True, "anual", "khe1")]
            
            
Clase Ticket:(fecha_entrada,fecha_salida,matricula,tipo,idplaza,pin,tarifa)

Lista:

tickets = [
           Ticket("15/12/2020", "", "papu", "turismo", 1, 166448, 0.12),
           Ticket("20/12/2020", "", "g4ru", "motocicleta", 2, 615762, 0.08),
           Ticket("18/12/2020", "", "m4st", "caravana", 3, 615897, 0.10),
           Ticket("20/12/2020", "21/12/2020", "ups5", "turismo", 5, 689987, 0.12)]
           
           
Clase TicketAbonado(Ticket):(fecha_entrada,fecha_salida,matricula,tipo,idplaza,pin,tarifa,matricula)

Lista:

tickets_abonados = [
                    TicketAbonado("18/12/2020", "", "d4ne", "turismo", 4, 965587, 70, "48484848y"),
                    TicketAbonado("16/12/2020", "", "hero", "caravana", 5, 247584, 200, "84654564e"),
                    TicketAbonado("15/12/2020", "", "gh4r", "motocicleta", 6, 689248, 200, "87484845s"),
                    TicketAbonado("19/12/2020", "22/12/2020", "tr10", "turismo", 6, 633998, 200, "26699005x"),
                    TicketAbonado("21/12/2020", "22/12/2020", "c4r5", "motocicleta", 7, 674847, 200, "21004875u"),
                    TicketAbonado("20/12/2020", "21/12/2020", "khe1", "turismo", 8, 690045, 200, "66984558q")]
       
       
Clase Plaza:(id,tipo,matricula,ocupado,reservado)

Lista:

listaplazas = [
            Plaza(1, "turismo", "papu", True, False),
            Plaza(2, "motocicleta", "g4ru", True, False),
            Plaza(3, "caravana", "m4st", True, False),
            Plaza(4, "turismo", "d4ne", True, True),
            Plaza(5, "caravana", "hero", True, True),
            Plaza(6, "motocicleta", "gh4r", True, True),
            Plaza(7, "turismo", "olv1", False, True)]
      
      
Clase Factura:(fecha_salida,matricula,pago)

Lista:

facturas = [
    Factura("21/12/2020", "55266677h", 250),
    Factura("22/12/2020", "26699005x", 200),
    Factura("22/12/2020", "21004875u", 200),
    Factura("21/12/2020", "66984558q", 200)]            
            
