#sitema de empleados empresa
class empleado:
    def __init__(self,nombre, edad, salario):
        self.nombre=nombre
        self.edad=edad
        self.salario=salario

class jefededepartamento(empleado):
    def __init__(self, nombre, edad, salario,departamento_a,):
        super().__init__(nombre, edad, salario)
        self.dep_a=departamento_a
    def describir_rol(self):
        print(f"el lider de el departamento de {self.dep_a} es el ser responsable de las operaciones del departamento")
class supervisor(empleado):
    def __init__(self, nombre, edad, salario,grupo_a):
        super().__init__(nombre, edad, salario)
        self.grup_a=grupo_a
    def describir_rol(self):
        print(f"el supervisor del grupo {self.grup_a} se encarga de vigilar y gestionar a su equipo. También comunica a la gerencia el desempeño o necesidades de las personas a su cargo. Se trata de un rol enfocado principalmente en la administración y ejecución de tareas")
class secretario(empleado):
    def __init__(self, nombre, edad, salario, encargado):
        super().__init__(nombre, edad, salario)
        self.encargado=encargado
    def describir_rolf(self):
        print(f"la funcion de un secretario es prestar apoyo administrativo a los directivos y otros profesionales. Sus responsabilidades incluyen usar el ordenador para redactar cartas, informes y otros documentos, atender llamadas telefónicas, organizar reuniones, llevar la agenda de su jefe y atender a las visitas.")

e01=jefededepartamento("carla moya",65,500432,"informatica")
e02=supervisor("esteban quito",43,500000,"A1")
e03=secretario("martin bombin",54,1500000,"esteban quito")