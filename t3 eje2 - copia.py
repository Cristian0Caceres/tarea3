#sitema de animales

class animal:
    def __init__(self,nombre,edad,soni):
        self.nombre=nombre
        self.edad=edad
        self.soni=soni
    def sonido(self):
        print(f"mi sonido es {self.soni}")
        return ""

class canino(animal):
    def __init__(self, nombre, edad, soni ,nombre_cientifico, rama):
        super().__init__(nombre, edad, soni)
        self.n_cientifico=nombre_cientifico
        self.rama=rama
    def sonido(self):
        return super().sonido()
    
    def quien_soy(self):
        print(f"mi nombre comun es {self.nombre} pero la comunidad cientifica me conoce como {self.n_cientifico} y pertenesco a los caninos en la rama {self.rama}")
        return ""
    
class felino(animal):
    def __init__(self, nombre, edad, soni , tipo_de_felino, maulla_o_ruje):
        super().__init__(nombre, edad, soni)
        self.tipo_de_f=tipo_de_felino
        self.miau_o_rawr=maulla_o_ruje
    def sonido(self):
        return super().sonido()
    def que_digo_y_soy(self):
        print(f"mi nombre es {self.nombre} dentro de los felinos soy un {self.tipo_de_f} y yo {self.miau_o_rawr}")
class ave(animal):
    def __init__(self, nombre, edad, soni,dieta,habitad):
        super().__init__(nombre, edad, soni)
        self.dieta=dieta
        self.habitad=habitad
    def sonido(self):
        return super().sonido()
    def que_como_y_donde_vivo(self):
        print(f"soy {self.nombre} y mi sieta es princcipalmente {self.dieta} y  mi habitad es {self.habitad} ")
        return ""
anima=canino("chihuahua", "3" , "wau wau" , " Canis lupus familiaris" , "canis familiaris")
print(anima.quien_soy())
print(anima.sonido())
animq1=felino("leon",7,"rawr rawr", "gran felino" , "ruje")
print(animq1.que_digo_y_soy())
print(animq1.sonido())
anima2=ave("buitre", 1 , "graaa graaa" , "carroñera" , "terrenos montañosos, del sur de Europa y norte de África hasta el centro de Asia")
print(anima2.sonido())
print(anima2.que_como_y_donde_vivo())