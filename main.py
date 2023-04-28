"""
SOLUCIÓN
Dados los antecedentes anteriores, es necesario desarrollar una solución tecnológica que cubra los
procesos de negocio descritos y que proponga una mejora en la gestión, el control, la seguridad, y
disponibilidad de información para el negocio y sus clientes. El sistema debe permitir presentar
productos, tomar pedidos y hacer seguimiento de estos y la gestión de clientes. Además, se requiere
que el sistema genere reportes y estadísticas que ayuden a tomar de decisiones y mejorar el
rendimiento de la empresa, considerando la cantidad de clientes, y la demanda de éstos. Es
imprescindible mantener comunicación con los encargados de entregar los pedidos, y darles la
posibilidad de realizar todas sus actividades teniendo conectividad a través de dispositivos móviles.

DESARROLLO - Continuación del trabajo.
Como parte de este ejercicio se necesita crear clases utilizando sintaxis de Python
En base al sistema desarrollado anteriormente en el módulo de Python básico, se solicita
Incorporar la creación de las siguientes clases.
● Clase Cliente.
● Clase Producto.
● Clase Vendedor.

La Clase Cliente deberá contar con los siguientes atributos:
a. ID Cliente
b. Nombre
c. Apellido
d. Correo
e. Fecha Registro
f. __Saldo

"""
clientes = []

class Usuario:
    def __init__(self, nivel, nombre, desc):
        self.nivel = nivel
        self.nombre = nombre
        self.desc = desc

#Se solicita que los atributos __Saldo (Cliente), __Impuesto (Producto) y __Comision (Vendedor) se
#encuentren encapsulados. (hecho ok)
class Cliente(Usuario):
    def __init__(self, ID_Cliente, Nombre, Apellido, Correo, Fecha_Registro, __Saldo):
        #tomo saldo como parametro porque en la tarea no le dan un valor por defecto
        self.ID_Cliente = ID_Cliente
        self.Nombre = Nombre
        self.Apellido = Apellido
        self.Correo = Correo
        self.Fecha_Registro = Fecha_Registro
        self.__Saldo = __Saldo #la encapsulacion la hago asi, con __ antes de la definicion del atributo de clase

    def agregar_saldo(self, saldo, ID_Cliente):
        if ID_Cliente == self.ID_Cliente:
            print("El saldo inicial es de: ", self.__Saldo)
            self.__Saldo += saldo
            print("Se agrego el saldo de: ", saldo)
            print("El saldo nuevo es de: ", self.__Saldo)
        else:
            print("No se encuentra el cliente indicado")
    def mostrar_saldo(self):
        print(f"Saldo de cliente es {self.__Saldo}")
#  Se debe crear métodos en la clase Cliente, lo cual puedan agregar y mostrar saldo.
#Como se encuentra trabajando en el desarrollo del módulo de Python Básico, se solicita integrar
#correctamente los métodos de las clases en las opciones del menú desarrollado.

class Vendedor(Usuario):
    def __init__(self, RUN, Nombre, Apellido, Seccion):
        self.RUN = RUN
        self.Nombre = Nombre
        self.Apellido = Apellido
        self.Seccion = Seccion
        self.__Comision = 0

class Producto():
    
    def __init__(self, SKU, Nombre, Categoria, Proveedor, Stock, Valor_Neto):
        self.SKU = SKU
        self.Nombre = Nombre
        self.Categoria = Categoria
        self.Proveedor = Proveedor
        self.Stock = Stock
        self.Valor_Neto = Valor_Neto
        self.__Impuesto = 1.19 
#usuario_invitado = invitado("invitado", "invitado", "cuenta invitado")

cliente1 = Cliente("id1", "Ignacio", "Fuentealba", "correo@gmail.com", "25-enero", 25000000)
cliente2 = Cliente("id2", "Juan", "Perez", "pepo@hotmail.com", "15-enero", 0)
cliente3 = Cliente("id3", "Pedro", "Gomez", "XXXXXXXXXXXXXXX", "20-enero", 0)
cliente4 = Cliente("id4", "Maria", "Lopez", "XXXXXXXXXXXXXXX", "20-marzo", 0)
cliente5 = Cliente("id5", "Luis", "Gonzalez", "XXXXXXXXXXXXXXX", "20-febrero", 0)

#TODO PENDIENTE:
#vendedor1-5
#producto1-5

"""
Desarrollar 5 instancias de cada clase creada en los puntos anteriores.
Piensen en una forma de graficar las relaciones entre las diferentes clases, puede ser un diagrama o
gráfica. Desarrollen el ejercicio de forma intuitiva.
"""
