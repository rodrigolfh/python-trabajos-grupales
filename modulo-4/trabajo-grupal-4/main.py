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
            
    def vender(self, compra):
        if compra.con_despacho == True:
            total_compra = compra.producto.valor_total * compra.cantidad 
            total_compra*= 1.1  # Aplicar un recargo del 10%
            print(f"Se aplicó un recargo por despacho. Nuevo valor de compra: ${round(total_compra)}")
            self.total_final_compra = total_compra
        else:
            total_compra = compra.producto.valor_total * compra.cantidad 
            print("No se aplicó recargo por despacho.")
        
   
#============================FIN CLASE VENDEDOR==================================


class Producto:
    
    def __init__(self, sku, nombre, categoria, proveedor, valor_neto, color = None):
        self.sku = sku
        self.nombre = nombre
        self.categoria = categoria
        self.proveedor = proveedor
        self.valor_neto = valor_neto
        self.__impuesto = 19
        self.valor_total = valor_neto + int(round(valor_neto * (self.__impuesto/100)))
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
    
#============================FIN CLASE PRODUCTO==================================
class Proveedor:
    def __init__(self, rut, nombre, razon_social, pais, tipo_persona):
        self.rut = rut
        self.nombre = nombre
        self.razon_social = razon_social
        self.pais = pais
        self.tipo_persona = tipo_persona
        
#============================FIN CLASE PROVEEDOR==================================
##clase Casa_Matriz

class Empresa:

    def __init__(self, nombre_empresa, rut, dirección):
        self._nombre_empresa = nombre_empresa
        self._rut = rut
        self.dirección = dirección
        #diccionarios vacíos, solo para poder crear métodos que serán heredados por las clases hijas
        
    def __str__(self):
        return(f"{self._nombre_empresa}, {self._rut}, {self.dirección}")
    
    def get_colaboradores(self):
            print(self.colaboradores)
            
    def set_colaborador(self, rut, estado): #pasarle instancia (ej:vendedor.rut) y estado ('activo' o 'inactivo')
        self.colaboradores[rut] = estado
     
    def  mostrar_stock(self): #pasarle argumento con método.imprime un dict con los stocks
        for key, value in self.stocks.items():
            print(f"SKU: {key}, STOCK: {value} unidades")

    def define_stock(self, sku, nuevo_stock):
        try:
            self.stocks[sku] = nuevo_stock
        except TypeError:
            print("Debe ingresar todos los argumentos")
    def stock(self, sku, modificación_stock = None): #obtiene la cantidad de unidades de un sku dado, o redefine si se le entrega además una cantidad
        #mantiene funcionalidad del método stock que tenía la clase Producto
        
        if modificación_stock == None:
            return(self.stocks[sku])
        
        elif modificación_stock:
            self.stocks[sku] += modificación_stock
            print(f"El producto SKU:{sku} tiene se modificó así: {modificación_stock:+}.") #:+ muestra el signo, sino cuando es positivo no se ve

    def revisar_stocks(self, límite, pedido, bodega): #revisa si stocks bajan de cierto número para pedir más a bodega.
        self.límite = límite  #si baja de esto, se pide a bodega
        self.pedido = pedido  #tamaño estándar de pedido a bodega
        self.bodega = bodega  #bodega de la que se sacaría reposición
        
        for key, value in self.stocks.items():
            if self.stocks[key] < self.límite and self.bodega.stock(key) >= self.pedido: #si baja del límite y = o + del límite
                print(f"Stock del producto SKU {key} ha bajado de {self.límite}. Pidiendo {self.pedido} a {self.bodega}")
                self.bodega.stock(key, -self.pedido) #descuenta de bodega                    
                self.stock(key, +self.pedido) #agrega a sucursal
                print(f"Se ha repuesto {self.pedido} al stock del producto SKU: {key}")
            
            elif self.stocks[key] < self.límite and self.bodega.stock(key) == 0:
                print(f"El producto SKU: {key} tiene sólo {value} unidades y se agotó en bodega")
            
            elif (self.stocks[key] < self.límite) and (self.bodega.stock(key) < self.pedido): #sino, se pide todo lo que quede en la bodega de ese sku
                lo_que_queda = self.bodega.stock(key)
                self.bodega.stock(key, -lo_que_queda)
                self.stock(key, +lo_que_queda) #agrega a sucursal lo que quedaba en bodega
                
                print(f"Solo quedaban {lo_que_queda} unidades del producto SKU:{key}, se repusieron todas")
 




class Bodega(Empresa):
    """funcionarios es un dict con key ruts y value "activo" o "inactivo", stocks es un dict con key asociado a SKU y value la cantidad"""
    def __init__(self, nombre, dirección, colaboradores, stocks): 
        self._id= nombre 
        self._dirección = dirección
        self.colaboradores = list(colaboradores)
        self.stocks = stocks

    def __str__(self):
        return(f"Bodega {self._id}")
        

## clase sucursal
class Sucursal(Empresa):
    def __init__(self, nombre, dirección, colaboradores, stocks): 
        self._id = nombre
        self._dirección = dirección
        self.colaboradores = list(colaboradores)
        self.stocks = stocks

    def __str__(self):
        return(f"Sucursal {self._nombre}")
#============================FIN CLASE SUCURSAL==================================

        ##se agrega la clase compra
class Compra:
    def __init__(self, cliente, producto, sucursal, vendedor, cantidad, con_despacho):
        self.cliente = cliente
        self.producto = producto #SKU
        self.sucursal = sucursal
        self.vendedor = vendedor
        self.cantidad = cantidad
        self.con_despacho = con_despacho
        
    def procesar_compra(self):
        gasto = self.cantidad*self.producto.valor_total #el gasto del cliente debe incluir el impuesto
        
        print("Detalle de la transacción:")
        print(f"Valor bruto:  {self.cantidad}*${self.producto.valor_neto} = {self.cantidad*self.producto.valor_neto}")
        print(f"Valor neto:   {self.cantidad}*${self.producto.valor_total} = ${gasto}")

####################cambiar referencia a la de stock dentro de sucursal.... agregar agumento de sucursal y bodega asociada?


        if (self.sucursal.stock(self.producto.sku)>=self.cantidad and self.cliente.saldo()>=gasto)==True:
            
            print("N°s originales")
            print(f"saldo de cliente es {self.cliente.saldo()}")
            print(f"stock de producto es {self.sucursal.stock(self.producto.sku)}")
            print(f"comision acumulativa de vendedor es {self.vendedor.get_comision_acumulativa()}")
            print(f"Se realizó una compra por ${gasto}")
            #la comision incluirá el impuesto como parte del monto gastado
            #realizamos deducciones y adicion de comision ganada
            self.cliente.saldo(-gasto) 
            self.sucursal.stock(self.producto.sku, -self.cantidad)
            print(f"comision es de {self.vendedor.porcentaje_comision()}%")
            self.vendedor.set_comision_acumulativa(gasto * self.vendedor.porcentaje_comision()/100) 
            #porcentaje comision te devuelve un numero entero representando su cut y multiplicamos por el 
            #valor total para sacar la comision que se va al trabajador, que en los ejemplos es del 5%
            #prints para testear cambios internos
            print("Post transacción:")
            print(f"saldo de cliente es {self.cliente.saldo()}")
            print(f"stock de producto es {self.sucursal.stock(self.producto.sku)}")
            print(f"comision de vendedor es {self.vendedor.get_comision_acumulativa()}")
            print("Compra realizada con éxito.")
            #return nuevo_saldo
        elif(self.sucursal.stock(self.producto.sku)<self.cantidad):
            print("No hay suficientes unidades para concretar la transacción")
        elif(self.cliente.saldo()<gasto):
            print("No tiene saldo suficiente para concretar la transacción")
            

             
#===================================FIN CLASE COMPRA=====================================
#===================================INSTANCIACIONES DE EJEMPLO=====================================
proveedor1 = Proveedor("111111111", "Proveedor1", "Falabella", "Mexico", "Persona Juridica")
proveedor2 = Proveedor("222222222", "Proveedor2", "Ripley", "Chile", "Persona Juridica")
proveedor3 = Proveedor("333333333", "Proveedor3", "CAT", "USA", "Persona Juridica")
proveedor4 = Proveedor("444444444", "Proveedor4", "Doite", "USA", "Persona Juridica")
proveedor5 = Proveedor("555555555", "Proveedor5", "Samsung", "Corea", "Persona Juridica")

producto1 = Producto("001", "Producto 1", "Menaje", proveedor1, 19990)
producto2 = Producto("002", "Producto 2", "Menaje", proveedor2, 9990)
producto3 = Producto("003", "Producto 3", "Zapatería", proveedor3, 8990)
producto4 = Producto("004", "Producto 4", "Deportes", proveedor4, 5990)
producto5 = Producto("005", "Producto 5", "Electro", proveedor5, 29990)


telovendo = Empresa("Te Lo Vendo", "1234567-9", "La Punta del Cerro s/n")
bodega_principal = Bodega("001", "Calle 1 sin número", {"12345677-1": True, "12345688-2": True, "12345655-4": True}, {"001": 10000,"002": 10000,"003": 10000,"004": 10000,"005": 10000})
sucursal_mall_plaza = Sucursal("001", "Calle 2 sin número", {"12345677-1": True, "12345688-2": True, "12345655-4": True}, {"001": 1000,"002": 1000,"003": 1000,"004": 1000,"005": 1000})

    

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

#probar método vender
compra1 = Compra(cliente2, producto1, sucursal_mall_plaza, vendedor3, 10, True)
vendedor3.vender(compra1)

compra2 = Compra(cliente1, producto3, sucursal_mall_plaza, vendedor1, 10, False)
vendedor1.vender(compra2)


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

