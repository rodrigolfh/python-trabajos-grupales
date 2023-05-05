#Se solicita que los atributos __saldo (Cliente), __Impuesto (Producto) y __Comision (Bodeguero) se
#encuentren encapsulados. (hecho ok)
productos = []
clientes = []

class Cliente:
    def __init__(self, id_cliente, nombre, apellido, correo, fecha_Registro, __saldo, edad = None):

        #tomo saldo como parametro porque en la tarea no le dan un valor por defecto
        self.id_cliente = id_cliente
        self.nombre = nombre
        self.apellido = apellido
        self.correo = correo
        self.fecha_registro = fecha_Registro
        self.__saldo = __saldo #la encapsulacion la hago asi, con __ antes de la definicion del atributo de clase
        self.edad = edad

    def get_saldo(self):
        return self.__saldo
    
    def set_saldo(self, cambio_saldo):
                    if (self.get_saldo() + cambio_saldo)>0: #si la suma (considerando un negativo posiblemente) es mayor a 0
                        self.__saldo = self.__saldo + cambio_saldo #entonces hace la suma (o resta) de stock.
                        if cambio_saldo>=0: print(f"Saldo de {self.nombre} {self.apellido} actualizado, se agregó ${cambio_saldo} de saldo, nuevo saldo: {self.__saldo}")
                        if cambio_saldo<0: print(f"Saldo de {self.nombre} {self.apellido} actualizado, se descontó ${abs(cambio_saldo)} de saldo, nuevo saldo: {self.__saldo}")
                    else: 
                        print("No hay saldo suficiente para ejecutar la transacción")

    def set_comision(self, nueva_comision):
        self.__comision = nueva_comision

    def get_comision(self):
        return self.__comision    
    
#============================FIN CLASE CLIENTE==================================


class Vendedor:
    def __init__(self, run, nombre, apellido, seccion, __comision, edad = None):
        self.run = run
        self.nombre = nombre
        self.apellido = apellido
        self.seccion = seccion
        self.__comision = __comision
        self.edad = edad
    
    def set_comision(self, nueva_comision):
        self.__comision = nueva_comision

    def get_comision(self):
        return self.__comision    
    
    def porcentaje_comision(self, run, porcentaje):
        if run == self.run:
            self.__comision = porcentaje
            print(f"El vendedor RUT {run} tiene ahora un porcentaje de comisión del {self.__comision}%")
        else:
            print("Vendedor no existe, intente con otro RUT.")
    def mostrar_comision(self, run):
       print(f"El vendedor RUT {run} tiene un porcentaje de comisión del {self.__comision}%")
#============================FIN CLASE VENDEDOR==================================

class Producto:
    
    def __init__(self, sku, nombre, categoria, proveedor, valor_neto, stock, color = None):
        self.sku = sku
        self.nombre = nombre
        self.categoria = categoria
        self.proveedor = proveedor
        self.valor_neto = valor_neto
        self.__impuesto = 19
        self.valor_total = valor_neto + int(round(valor_neto * (self.__impuesto/100)))
        self._stock = stock
        self.color = color
    
    def definir_impuesto_producto(self, sku, porcentaje_impuesto):
        if sku == self.sku:
            self.__impuesto = porcentaje_impuesto
        else:
            print("No se encuentra ese producto")
        
    def mostrar_impuesto(self, sku):
        print(f"El impuesto del producto SKU {sku} es {self.__impuesto}%")
    
    def lista(self):
        pass

    def set_comision(self, nueva_comision):
        self.__comision = nueva_comision

    def get_comision(self):
        return self.__comision  

    #def get_stock(self):
    #    return self.stock

    """
   @property
    def name(self):
         return self._name
    
    @name.setter
    def name(self, name):
         if not name:
              raise ValueError("Missing name")
         self._name = name
    """

    @property
    def stock(self):
        return self._stock

    #TODO: pendiente sobrecargar alguno de los métodos
    @stock.setter
    def stock(self, cambio):
                #print(cambio) <<- toma valor entero menos con lo que lo llamaste
                if (cambio)>0: #si la suma (considerando un negativo posiblemente) es mayor a 0
                    #suma = self._stock + cambio #entonces hace la suma (o resta) de stock. TA MALO
                    self._stock = cambio
                    #este flavor text no funciona asi, necesitaré saber el delta para poder anotar el cambio como parte del return.
                    #if cambio>=0: print(f"Stock de {self.nombre} actualizado, se agregó ${cambio} de stock, nuevo stock: {self._stock}")
                    #if cambio<0: print(f"Stock de {self.nombre} actualizado, se descontó ${abs(cambio)} de stock, nuevo stock: {self._stock}")
                else: 
                    print("No hay stock suficiente para ejecutar la transacción")

#============================FIN CLASE PRODUCTO==================================

"""
def datos_venta(producto, cliente, vendedor, cantidad):
    while True:
        valor_total = input("Ingrese producto: ").valor_total()
        valor_neto = input("Ingrese producto: ").valor_neto()
        cliente = input("Ingrese cliente: ")
        vendedor = input("Ingrese vendedor: ")
        cantidad = input("Ingrese cantidad: ")
"""
class Proveedor:

    def __init__(self, rut, nombre, razon_social, pais, tipo_persona):
        self.rut = rut
        self.nombre = nombre
        self.razon_social = razon_social
        self.pais = pais
        self.tipo_persona = tipo_persona

##se agrega la clase compra
class Compra:
    def __init__(self, cliente, producto, vendedor, cantidad):
        self.cliente = cliente
        self.producto = producto
        self.vendedor = vendedor
        self.cantidad = cantidad
    
    def procesar_compra(self):
        #if ((self.validar_stock() and self.validar_saldo())==True):
        if ((self.producto._stock > #mayor a la cantidad entrante) and self.cliente.get_saldo()> mayor al gasto)==True):
            self.producto._stock -= self.cantidad #actualiza stock
            saldo = self.cliente.get_saldo()
            nuevo_saldo = saldo - (self.cantidad * self.producto.valor_neto) #guarda variable para actualizar saldo en la clase cliente
            self.cliente.set_saldo(nuevo_saldo)
            print("Compra realizada con éxito.")
            return nuevo_saldo

class Venta(Producto, Cliente, Vendedor):
    def __init__(self, producto, cliente, vendedor, cantidad):
       
        self.producto = producto
        self.cliente = cliente
        self.vendedor = vendedor
        self.cantidad = cantidad
        self.valor_total = producto.valor_total()
     
        valor_a_pagar = int(round((self.valor_total +  (vendedor.get_comision()*self.valor_neto))*self.cantidad))
        #revisa si saldo de puntos/dinero es suficiente
        if  (valor_a_pagar <= cliente.getter_temporal_saldo()) and (self._stock >= cantidad):
            cliente.setter_descontar_saldo(valor_a_pagar)
            self._stock -= cantidad 

        else:
            print(("No hay suficientes unidades o el cliente no tiene saldo suficiente"))

#===================================INSTANCIACIONES DE EJEMPLO=====================================
proveedor1 = Proveedor("111111111", "Proveedor1", "Falabella", "Mexico", "Persona Juridica")
proveedor2 = Proveedor("222222222", "Proveedor2", "Ripley", "Chile", "Persona Juridica")
proveedor3 = Proveedor("333333333", "Proveedor3", "CAT", "USA", "Persona Juridica")
proveedor4 = Proveedor("444444444", "Proveedor4", "Doite", "USA", "Persona Juridica")
proveedor5 = Proveedor("555555555", "Proveedor5", "Samsung", "Corea", "Persona Juridica")

producto1 = Producto("001", "Producto 1", "Menaje", proveedor1, 100, 19990)
producto2 = Producto("002", "Producto 2", "Menaje", proveedor2, 100, 9990)
producto3 = Producto("003", "Producto 3", "Zapatería", proveedor3, 100, 8990)
producto4 = Producto("004", "Producto 4", "Deportes", proveedor4, 100, 5990)
producto5 = Producto("005", "Producto 5", "Electro", proveedor5, 100, 29990)

vendedor1 = Vendedor("12345677-1", "Hugo", "Araya", "Zapatería", 0.5)
vendedor2 = Vendedor("12345688-2", "Paco", "Iriarte", "Deportes", 0.5)
vendedor3 = Vendedor("12345699-3", "Luis", "Gómez", "Juguetería", 0.5)
vendedor4 = Vendedor("12345655-4", "Ana", "Rodríguez", "Electro", 0.5)
vendedor5 = Vendedor("12345622-5", "María", "González", "Menaje", 0.5)

#Se debe crear métodos en la clase Cliente, lo cual puedan agregar y mostrar saldo.
#Como se encuentra trabajando en el desarrollo del módulo de Python Básico, se solicita integrar
#correctamente los métodos de las clases en las opciones del menú desarrollado.
cliente1 = Cliente("id1", "Ignacio", "Fuentealba", "correo@gmail.com", "25-enero", 25000000)
cliente2 = Cliente("id2", "Juan", "Perez", "pepo@hotmail.com", "15-enero", 0)
cliente3 = Cliente("id3", "Pedro", "Gomez", "XXXXXXXXXXXXXXX", "20-enero", 0)
cliente4 = Cliente("id4", "Maria", "Lopez", "XXXXXXXXXXXXXXX", "20-marzo", 0)
cliente5 = Cliente("id5", "Luis", "Gonzalez", "XXXXXXXXXXXXXXX", "20-febrero", 0)


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

