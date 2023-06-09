"""
Exigencias 4.3

DESARROLLO - Continuación del trabajo.
Como parte de este ejercicio se necesita crear clases utilizando sintaxis de Python, para comprender las
ventajas de la programación orientada a objetos.
En vista a nuestro sistema desarrollado anteriormente se solicita lo siguiente:
Si el atributo stock de la clase Sucursal cuenta con un stock menos de 50, este automáticamente deberá
mostrar un mensaje el cual indique que se está solicitando y reponiendo productos y desde la clase
Bodega se deberá descontar 300 del atributo stock y sumarlos a Sucursal. En el caso de que no quede
suficiente stock en la clase Bodega, deberá indicar a través de un mensaje que no existe stock suficiente
para reponer.
Se debe implementar la función super() para poder acceder a los atributos y métodos de clases
superiores.
Se deberá implementar una clase OrdenCompra con los siguientes atributos:
a. Id_ordencompra
b. producto
c. despacho
El atributo producto, deberá ser una composición de la clase Producto y el atributo despacho, solo
almacenará valores booleanos. En el caso de que el despacho sea True ( Verdadero ), se deberá agregar al
valor del producto 5.000 CLP por recargo de despacho y mostrar por consola el total final con el detalle (
valor neto, impuesto, despacho, valor total ) el valor final del producto, cuando se utilice la función vender
de la clase Vendedor.

Resumido:
-Usando super(), Chequeo automático en clase Sucursal de stock en 50<, print y descontar 300 de stock y sumarlos a Sucursal en item correspondiente
-Crear Clase OrdenCompra con los atributos dados.
-Que producto se componga de la cls Producto y que despacho solo almacene valores booleanos.
-Que Vendedor en su metodo vender()(?) modifique el valor de la orden de compra por recargo de despacho en base al bool de la OrdenCompra. Debe entregar mensaje con la glosa.
"""

#Se solicita que los atributos __saldo (Cliente), __Impuesto (Producto) y __Comision (Bodeguero) se
#encuentren encapsulados. (hecho ok)
productos = []
clientes = []

class Cliente:
    def __init__(self, id_cliente, nombre, apellido, correo, fecha_Registro, saldo, edad = None):

        #tomo saldo como parametro porque en la tarea no le dan un valor por defecto
        self.id_cliente = id_cliente
        self.nombre = nombre
        self.apellido = apellido
        self.correo = correo
        self.fecha_registro = fecha_Registro
        self.__saldo = saldo #la encapsulacion la hago asi, con __ antes de la definicion del atributo de clase
        self.edad = edad
    
    def saldo(self, *cambio):
        if len(cambio) == 0:
            return self.__saldo
        else:
            suma = sum(cambio)
            if (suma)+self.__saldo>=0: #si la suma (considerando un negativo posiblemente) es mayor a 0
                self.__saldo += suma #entonces hace la suma (o resta) de stock.
                #if cambio_saldo>=0: print(f"Saldo de {self.nombre} {self.apellido} actualizado, se agregó ${cambio_saldo} de saldo, nuevo saldo: {self.__saldo}")
                #if cambio_saldo<0: print(f"Saldo de {self.nombre} {self.apellido} actualizado, se descontó ${abs(cambio_saldo)} de saldo, nuevo saldo: {self.__saldo}")
            else: 
                print("Operación no realizada: no hay saldo suficiente para ejecutar la transacción")
#============================FIN CLASE CLIENTE==================================

class Vendedor:
    def __init__(self, run, nombre, apellido, seccion, porcentaje_comision, edad = None, __comision = 0):
        self.run = run
        self.nombre = nombre
        self.apellido = apellido
        self.seccion = seccion
        self.__comision_acumulativa = __comision
        self.edad = edad
        self.__porcentaje_comision = porcentaje_comision
    
    def set_comision_acumulativa(self, comision):
        self.__comision_acumulativa += comision

    def get_comision_acumulativa(self):
        return self.__comision_acumulativa    
    
    def porcentaje_comision(self, run=None, porcentaje=None):
        if run is None or porcentaje is None:
            return self.__porcentaje_comision
        if run == self.run:
            self.__porcentaje_comision = porcentaje
            print(f"El vendedor RUT {run} tiene ahora un porcentaje de comisión del {self.__porcentaje_comision}%")
        else:
            print("Vendedor no existe, intente con otro RUT.")
#============================FIN CLASE VENDEDOR==================================

class Producto:
    
    def __init__(self, sku, nombre, categoria, proveedor, stock, valor_neto, color = None):
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
    @property
    def impuesto(self):
        return self.__impuesto

    def mostrar_impuesto(self, sku):
        print(f"El impuesto del producto SKU {sku} es {self.__impuesto}%")
    
    def stock(self, *valor):
            if len(valor) == 0:
                return self._stock
            else:
                suma = sum(valor)
                if self._stock+int(suma)>=0: #si la suma (considerando un negativo posiblemente) es mayor a 0
                    self._stock += suma
                else: 
                    print("No hay stock suficiente para ejecutar la transacción")
#============================FIN CLASE PRODUCTO==================================
class Proveedor:
    def __init__(self, rut, nombre, razon_social, pais, tipo_persona):
        self.rut = rut
        self.nombre = nombre
        self.razon_social = razon_social
        self.pais = pais
        self.tipo_persona = tipo_persona
#============================FIN CLASE PROVEEDOR==================================

##se agrega la clase compra
class Compra:
    def __init__(self, cliente, producto, vendedor, cantidad):
        self.cliente = cliente
        self.producto = producto
        self.vendedor = vendedor
        self.cantidad = cantidad
    
    def procesar_compra(self):
        gasto = self.cantidad*self.producto.valor_total #el gasto del cliente debe incluir el impuesto
        print("Detalle de la transacción:")
        print(f"Valor bruto:  {self.cantidad}*${self.producto.valor_neto} = {self.cantidad*self.producto.valor_neto}")
        print(f"Valor neto:   {self.cantidad}*${self.producto.valor_total} = ${gasto}")

        if (self.producto.stock()>=self.cantidad and self.cliente.saldo()>=gasto)==True:
            
            print("N°s originales")
            print(f"saldo de cliente es {self.cliente.saldo()}")
            print(f"stock de producto es {self.producto.stock()}")
            print(f"comision acumulativa de vendedor es {self.vendedor.get_comision_acumulativa()}")
            print(f"Se realizó una compra por ${gasto}")
            #la comision incluirá el impuesto como parte del monto gastado
            #realizamos deducciones y adicion de comision ganada
            self.cliente.saldo(-gasto) 
            self.producto.stock(-self.cantidad)
            print(f"comision es de {self.vendedor.porcentaje_comision()}%")
            self.vendedor.set_comision_acumulativa(gasto * self.vendedor.porcentaje_comision()/100) 
            #porcentaje comision te devuelve un numero entero representando su cut y multiplicamos por el 
            #valor total para sacar la comision que se va al trabajador, que en los ejemplos es del 5%
            #prints para testear cambios internos
            print("Post transacción:")
            print(f"saldo de cliente es {self.cliente.saldo()}")
            print(f"stock de producto es {self.producto.stock()}")
            print(f"comision de vendedor es {self.vendedor.get_comision_acumulativa()}")
            print("Compra realizada con éxito.")
            #return nuevo_saldo
        elif(self.producto.stock()<self.cantidad):
            print("No hay suficientes unidades para concretar la transacción")
        elif(self.cliente.saldo()<gasto):
            print("No tiene saldo suficiente para concretar la transacción")

    
"""
Se deberá implementar una clase OrdenCompra con los siguientes atributos:
a. Id_ordencompra
b. producto
c. despacho
El atributo producto, deberá ser una composición de la clase Producto y el atributo despacho, solo
almacenará valores booleanos. En el caso de que el despacho sea True ( Verdadero ), se deberá agregar al
valor del producto 5.000 CLP por recargo de despacho y mostrar por consola el total final con el detalle (
valor neto, impuesto, despacho, valor total ) el valor final del producto, cuando se utilice la función vender
de la clase Vendedor.
"""

class OrdenCompra:
    
    def __init__(self, Id_ordencompra, Producto, despacho):
        self.Id_ordencompra = Id_ordencompra
        self.Producto = Producto
        if isinstance(despacho, bool): 
            self.despacho = despacho
            if despacho: self.Producto.valor_total+=5000
        #esta se mi interpretación:
        #bajo la idea de que cada producto con despacho TRUE aportará al 5000 al subtotal, incluso si son varias cantidades del mismo, lo hará por instancia
        #al más puro estilo de Ripley Marketplace.
        
        


#===================================FIN CLASE COMPRA=====================================
#===================================INSTANCIACIONES DE EJEMPLO=====================================
proveedor1 = Proveedor("111111111", "Proveedor1", "Falabella", "Mexico", "Persona Juridica")
proveedor2 = Proveedor("222222222", "Proveedor2", "Ripley", "Chile", "Persona Juridica")
proveedor3 = Proveedor("333333333", "Proveedor3", "CAT", "USA", "Persona Juridica")
proveedor4 = Proveedor("444444444", "Proveedor4", "Doite", "USA", "Persona Juridica")
proveedor5 = Proveedor("555555555", "Proveedor5", "Samsung", "Corea", "Persona Juridica")

producto1 = Producto("001", "Producto 1", "Menaje", proveedor1, 5, 19990)
producto2 = Producto("002", "Producto 2", "Menaje", proveedor2, 100, 9990)
producto3 = Producto("003", "Producto 3", "Zapatería", proveedor3, 100, 8990)
producto4 = Producto("004", "Producto 4", "Deportes", proveedor4, 100, 5990)
producto5 = Producto("005", "Producto 5", "Electro", proveedor5, 100, 29990)

vendedor1 = Vendedor("12345677-1", "Hugo", "Araya", "Zapatería",  5, 50)
vendedor2 = Vendedor("12345688-2", "Paco", "Iriarte", "Deportes", 5, 51)
vendedor3 = Vendedor("12345699-3", "Luis", "Gómez", "Juguetería", 5, 52)
vendedor4 = Vendedor("12345655-4", "Ana", "Rodríguez", "Electro", 5, 53)
vendedor5 = Vendedor("12345622-5", "María", "González", "Menaje", 5, 54)

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

