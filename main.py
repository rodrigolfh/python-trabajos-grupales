"""
SOLUCIÓN
Dados los antecedentes anteriores, es necesario desarrollar una solución tecnológica que cubra los
procesos de negocio descritos y que propongagit  una mejora en la gestión, el control, la seguridad, y
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
● Clase Bodeguero.

La Clase Cliente deberá contar con los siguientes atributos:
a. ID Cliente
b. Nombre
c. Apellido
d. Correo
e. Fecha Registro
f. __Saldo

"""
#Se solicita que los atributos __Saldo (Cliente), __Impuesto (Producto) y __Comision (Bodeguero) se
#encuentren encapsulados. (hecho ok)
class Cliente():
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
        print(f"Saldo de cliente {self.Nombre} {self.Apellido} es: {self.__Saldo}")
#Se debe crear métodos en la clase Cliente, lo cual puedan agregar y mostrar saldo.
#Como se encuentra trabajando en el desarrollo del módulo de Python Básico, se solicita integrar
#correctamente los métodos de las clases en las opciones del menú desarrollado.

class Vendedor():
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

cliente1 = Cliente("id1", "Ignacio", "Fuentealba", "correo@gmail.com", "25-enero", 25000000)
cliente2 = Cliente("id2", "Juan", "Perez", "pepo@hotmail.com", "15-enero", 0)
cliente3 = Cliente("id3", "Pedro", "Gomez", "XXXXXXXXXXXXXXX", "20-enero", 0)
cliente4 = Cliente("id4", "Maria", "Lopez", "XXXXXXXXXXXXXXX", "20-marzo", 0)
cliente5 = Cliente("id5", "Luis", "Gonzalez", "XXXXXXXXXXXXXXX", "20-febrero", 0)

producto1 = Producto("001", "Producto 1", "Menaje", "Proveedor1", 100, 19990)
producto2 = Producto("002", "Producto 2", "Menaje", "Proveedor1", 100, 9990)
producto3 = Producto("003", "Producto 3", "Zapatería", "Proveedor3", 100, 8990)
producto4 = Producto("004", "Producto 4", "Deportes", "Proveedor2", 100, 5990)
producto5 = Producto("005", "Producto 5", "Electro", "Proveedor2", 100, 29990)

vendedor1 = Vendedor("12345677-1", "Hugo", "Araya", "Zapatería")
vendedor2 = Vendedor("12345688-2", "Paco", "Iriarte", "Deportes")
vendedor3 = Vendedor("12345699-3", "Luis", "Gómez", "Juguetería")
vendedor4 = Vendedor("12345655-4", "Ana", "Rodríguez", "Electro")
vendedor5 = Vendedor("12345622-5", "María", "González", "Menaje")

cliente1.agregar_saldo(500, "id1")
cliente2.mostrar_saldo()
#TODO PENDIENTE:

def menu_principal():
    print("--------Bienvenido a Telovendo SPA--------")
    print("Menú Clientes = 1")
    print("Menú Ventas = 2")
    print("Menú Productos = 3")

    opcion = int(input("Ingrese el número de la opción deseada: \n"))

    
    switcher = {
        1: menu_clientes,
        2: menu_ventas,
        3: menu_productos
    }
    funcion = switcher.get(opcion)
    if funcion:
        funcion()
    else:
        print("Opción no válida") 

    
def menu_clientes():
    print("")
    print("--------Menú Cliente-------")
    print("Agregar un Cliente = 1")
    print("Modificar un Cliente = 2")
    print("Eliminar un Cliente = 3")
    print("Consultar TeloPuntos = 4")
    print("Recargar TeloPuntos = 5")
    print("Volver = 6")
   
    opcion = int(input("Ingrese el número de la opción deseada: \n"))

    switcher = {
        1: agregar_cliente,
        2: modificar_cliente,
        3: eliminar_cliente,
        4: consultar_telopuntos,
        5: recargar_telopuntos,
        6: menu_principal
    }    
    funcion = switcher.get(opcion)
    if funcion:
        funcion()
    else:
        print("Opción no válida")

def agregar_cliente():
    pass
def modificar_cliente():
    pass
def eliminar_cliente():
    pass
def consultar_telopuntos():
    pass
def recargar_telopuntos():
    pass

def menu_ventas():
    print("")
    print("--------Menú Venta-------")
    print("Agregar al Carrito = 1")
    print("Eliminar del Carrito = 2")
    print("Ver Carrito = 3")
    print("Pagar usando TeloPuntos= 4")
    print("Pagar con Efectivo/Tarjeta = 5") #Pronto!
    print("Volver = 6")

    cliente = input("Ingrese número único del cliente: ")
    opcion = int(input("Ingrese el número de la opción deseada: \n"))

    switcher = {
        1: agregar_item_carrito,
        2: eliminar_item_carrito,
        3: ver_carrito,
        4: pago_con_telopuntos, 
        5: pago_normal #Pronto!
        
    }    
    funcion = switcher.get(opcion)
    if funcion:
        funcion()
    else:
        print("Opción no válida")

def agregar_item_carrito():
    pass
def eliminar_item_carrito():
    pass
def ver_carrito():
    pass
def pago_con_telopuntos():
    pass
def pago_normal():
    pass

def menu_productos():
    print("")
    print("--------Menú Productos-------")
    print("Agregar un Producto = 1")
    print("Modificar un Producto = 2")
    print("Eliminar un Producto = 3")
    print("Consultar Stock = 4")
    print("Volver = 5")
   
    opcion = int(input("Ingrese el número de la opción deseada: \n"))

    switcher = {
        1: agregar_producto,
        2: modificar_producto,
        3: eliminar_producto,
        4: consultar_stock,
        5: menu_principal
    }    
    funcion = switcher.get(opcion)
    if funcion:
        funcion()
    else:
        print("Opción no válida")

def agregar_producto():
    pass
def modificar_producto():
    pass
def eliminar_producto():
    pass
def consultar_stock():
    pass
def menu_principal():
    pass


    



"""

def agregar_saldo():
    pass


Desarrollar 5 instancias de cada clase creada en los puntos anteriores.
Piensen en una forma de graficar las relaciones entre las diferentes clases, puede ser un diagrama o
gráfica. Desarrollen el ejercicio de forma intuitiva.
"""
