#sistema de reserva

class reserva:
    def __init__(self,nombre_del_pasajero,numero_de_vuelo,fecha):
        self.nom_d_pasajero=nombre_del_pasajero
        self.num_d_vue=numero_de_vuelo
        self.fecha=fecha
    def mostrar_detalles(self):
        print(f"la resrvacion esta a nombre de {self.nom_d_pasajero} su numero de vuelo es {self.num_d_vue} y esta agendado para la fecha {self.fecha}")
        return ""
class economica(reserva):
    def __init__(self, nombre_del_pasajero, numero_de_vuelo, fecha, ventana_o_pasillo):
        super().__init__(nombre_del_pasajero, numero_de_vuelo, fecha)
        self.v_o_p=ventana_o_pasillo
    def mostrar_detalles(self):
        return super().mostrar_detalles() 
    def cambiar_posision_de_asiento(self):
        print(f"la posision actual de esta reserva es {self.v_o_p}")
        cambio=input("inserte [ventana] si desea estar en la ventana / inserte un [pasillo] si desea estar en el pasillo: ")
        if self.v_o_p == cambio:
            print("se a equivocado al modificar la posicion por lo que se mantendra")
            return ""
        elif cambio == "ventana":
            self.v_o_p = "ventana"
            print("se a cambiado de forma exitosa a ventana su posicion")
            return ""
        elif cambio == "pasillo":
            self.v_o_p = "pasillo"
            print("se a cambiado de forma existosa a pasillo su posicion")
        return
    
class business(reserva):
    def __init__(self, nombre_del_pasajero, numero_de_vuelo, fecha, menu):
        super().__init__(nombre_del_pasajero, numero_de_vuelo, fecha)
        self.menu=menu
    def mostrar_detalles(self):
        return super().mostrar_detalles()
    def el_menu(self):
        print(f"el menu actual de esta reserva es de {self.menu}")
        print("")
        print("el menu A consiste de arroz con pollo y un vaso de vino")
        print("el menu B consiste de sebiche con vino blanco")
        cambio=input("inserte [A] si desea el menu A / inserte [B] si desea el menu B: ")
        if self.menu == cambio:
            print("se a equivocado al modificar el menu por lo que se mantendra")
            return ""
        elif cambio == "A" or cambio == "a":
            self.menu = "A"
            print("se a cambiado de forma exitosa a el menu A")
            return ""
        elif cambio == "B" or cambio == "b":
            self.menu = "B"
            print("se a cambiado de forma existosa a el menu B")
        return ""

class first_class(reserva):
    def __init__(self, nombre_del_pasajero, numero_de_vuelo, fecha, reserva_del_hotel_incluido):
        super().__init__(nombre_del_pasajero, numero_de_vuelo, fecha)
        self.r_d_h_i=reserva_del_hotel_incluido
    def mostrar_detalles(self):
        return super().mostrar_detalles()
    def el_hotel_incluido_es(self):
        print(f"el hotel incluido con su reserva es {self.r_d_h_i}")
        return ""
ec01=economica("pedro pascal", 123456 ,"12/12/2023","ventana")
print(ec01.mostrar_detalles())
ec01.cambiar_posision_de_asiento()        
bu02=business("alejandro urrutria", 232331, "12/11/2023","A")
print(bu02.mostrar_detalles())
bu02.el_menu()
fc03=first_class("armando cabezas", 456123 , "01/01/2023","hotel silver fang")
print(fc03.mostrar_detalles())
print(fc03.el_hotel_incluido_es())