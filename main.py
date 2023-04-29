#Se solicita que los atributos __Saldo (Cliente), __Impuesto (Producto) y __Comision (Bodeguero) se
#encuentren encapsulados. (hecho ok)
class Cliente():
    def __init__(self, id_cliente, nombre, apellido, correo, fecha_Registro, __saldo):
        #tomo saldo como parametro porque en la tarea no le dan un valor por defecto
        self.id_cliente = id_cliente
        self.nombre = nombre
        self.apellido = apellido
        self.correo = correo
        self.fecha_registro = fecha_Registro
        self.__saldo = __saldo #la encapsulacion la hago asi, con __ antes de la definicion del atributo de clase

    def agregar_saldo(self, saldo, id_cliente):
        if id_cliente == self.id_cliente:
            print("El saldo inicial es de: ", self.__saldo)
            self.__saldo += saldo
            print("Se agrego el saldo de: ", saldo)
            print("El saldo nuevo es de: ", self.__saldo)
        else:
            print("No se encuentra el cliente indicado")

    def mostrar_saldo(self):
        print(f"Saldo de cliente {self.nombre} {self.apellido} es: {self.__saldo}")
#Se debe crear métodos en la clase Cliente, lo cual puedan agregar y mostrar saldo.
#Como se encuentra trabajando en el desarrollo del módulo de Python Básico, se solicita integrar
#correctamente los métodos de las clases en las opciones del menú desarrollado.
cliente1 = Cliente("id1", "Ignacio", "Fuentealba", "correo@gmail.com", "25-enero", 25000000)
cliente2 = Cliente("id2", "Juan", "Perez", "pepo@hotmail.com", "15-enero", 0)
cliente3 = Cliente("id3", "Pedro", "Gomez", "XXXXXXXXXXXXXXX", "20-enero", 0)
cliente4 = Cliente("id4", "Maria", "Lopez", "XXXXXXXXXXXXXXX", "20-marzo", 0)
cliente5 = Cliente("id5", "Luis", "Gonzalez", "XXXXXXXXXXXXXXX", "20-febrero", 0)

class Vendedor():
    def __init__(self, run, nombre, apellido, seccion, __comision):
        self.run = run
        self.nombre = nombre
        self.apellido = apellido
        self.seccion = seccion
        self.__comision = __comision 
    
    def porcentaje_comision(self, run, porcentaje):
        if run == self.run:
            self.__comision = porcentaje
            print(f"El vendedor RUT {run} tiene ahora un porcentaje de comisión del {self.__comision}%")
        else:
            print("Vendedor no existe, intente con otro RUT.")
    def mostrar_comision(self, run):
       print(f"El vendedor RUT {run} tiene un porcentaje de comisión del {self.__comision}%")

vendedor1 = Vendedor("12345677-1", "Hugo", "Araya", "Zapatería", 0)
vendedor2 = Vendedor("12345688-2", "Paco", "Iriarte", "Deportes", 0)
vendedor3 = Vendedor("12345699-3", "Luis", "Gómez", "Juguetería", 0)
vendedor4 = Vendedor("12345655-4", "Ana", "Rodríguez", "Electro", 0)
vendedor5 = Vendedor("12345622-5", "María", "González", "Menaje", 0)

print('\n>>>vendedor1.mostrar_comision("12345677-1")')
vendedor1.mostrar_comision("12345677-1")

print('\n>>>vendedor1.porcentaje_comision("12345677-1", 2)')
vendedor1.porcentaje_comision("12345677-1", 2)

class Producto():
    
    def __init__(self, sku, nombre, categoria, proveedor, stock, valor_neto):
        self.sku = sku
        self.nombre = nombre
        self.categoria = categoria
        self.proveedor = proveedor
        self.stock = stock
        self.valor_Neto = valor_neto
        self.__impuesto = 19
    
    def definir_impuesto_producto(self, sku, porcentaje_impuesto):
        if sku == self.sku:
            self.__impuesto = porcentaje_impuesto
        else:
            print("No se encuentra ese producto")
        
    def mostrar_impuesto(self, sku):
        print(f"El impuesto del producto SKU {sku} es {self.__impuesto}%")
    def lista(self):
        pass



producto1 = Producto("001", "Producto 1", "Menaje", "Proveedor1", 100, 19990)
producto2 = Producto("002", "Producto 2", "Menaje", "Proveedor1", 100, 9990)
producto3 = Producto("003", "Producto 3", "Zapatería", "Proveedor3", 100, 8990)
producto4 = Producto("004", "Producto 4", "Deportes", "Proveedor2", 100, 5990)
producto5 = Producto("005", "Producto 5", "Electro", "Proveedor2", 100, 29990)

#prueba de método mostrar y modificar saldo
print('\n>>>cliente2.mostrar_saldo()')
cliente2.mostrar_saldo()
print('\n>>>cliente1.agregar_saldo(500, "id1")')
cliente1.agregar_saldo(500, "id1")


#prueba de métodos de impuesto
print('\n>>>producto1.mostrar_impuesto("001")')
producto1.mostrar_impuesto("001")
print('\n>>>producto1.definir_impuesto_producto("001", 18)')
producto1.definir_impuesto_producto("001", 18)
print('\n>>>producto1.mostrar_impuesto("001")')
producto1.mostrar_impuesto("001")

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
    print("Consultar Telopuntos = 4")
    print("Pagar usando TeloPuntos = 5")
    print("Pagar con Efectivo/Tarjeta = 6") #Pronto!
    print("Volver = 7")
    
    cliente = input("Ingrese número único del cliente a atender : ") #para no preguntarlo a cada rato
    opcion = int(input("Ingrese el número de la opción deseada: \n"))

    switcher = {
        1: agregar_item_carrito,
        2: eliminar_item_carrito,
        3: ver_carrito,
        4: consultar_telopuntos,
        5: pago_con_telopuntos, 
        6: pago_normal, #Pronto!
        7: menu_principal        
    }    
    funcion = switcher.get(opcion)
    if funcion:
        funcion()
    else:
        print("Opción no válida")

carrito = []
def agregar_item_carrito(item):
    item = input("Ingrese Número de Producto (sku): ")
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


    


