#gestion de productos
class product:
    def __init__(self,name , cost, category):
        self.name=name
        self.cost=cost
        self.category=category
    def sHOWdETAILS(self):
        print(f"el producto {self.name} posee un costo de {self.cost} esta dentrro de la categoria {self.category}")
        return ""
class electronics(product):
    def __init__(self , name , cost , category , consumption , num_serial):
        super().__init__( name , cost , category)
        self.consumption=consumption
        self.num_serial=num_serial
    def sHOWdETAILS(self):
        print(f"el producto {self.name} posee un costo de {self.cost} esta dentrro de la categoria {self.category} el cual posee un consumo de {self.consumption} y su numero de serie es {self.num_serial}")
        return ""
class alimentation(product):
    def __init__(self,name,cost,category,cosecha_F,vencimiento_F):
        super().__init__(name,cost,category)
        self.cosecha_F=cosecha_F
        self.vencimiento_F=vencimiento_F
    def sHOWdETAILS(self):
        print(f"el producto {self.name} posee un costo de {self.cost} esta dentrro de la categoria {self.category} la fecha en al cual fue cosechado es en {self.cosecha_F} la fecha en la cual este producto se malograra es {self.vencimiento_F}")
        return ""
class clothes(product):
    def __init__(self, name, cost, category, marca, coleccion):
        super().__init__(name, cost, category)
        self.marca=marca
        self.coleccion=coleccion
    def sHOWdETAILS(self):
        print(f"el producto {self.name} posee un costo de {self.cost} esta dentrro de la categoria {self.category} la marca a la cual pertenece el producto es {self.marca} a su ves este es de la coleccion {self.coleccion}")
        return ""
p01 = electronics("computador","10","tecnologia","8.000.000 w/h","755")
print(p01.sHOWdETAILS())
p02= alimentation("tomate","1000","alimentacion","2022-02-11","2022-02-18")
print(p02.sHOWdETAILS())
p03= clothes("pantalon mariano dross","3500000","ropa","supreme","colaboraciones mariano dross")
print(p03.sHOWdETAILS())
        
        
