import time

from excepciones import NoSeraMuchoException
import json

#si no hay un stocks.json, lo crea:
ruta_json_stocks = "" 
with open("stocks.json", "w") as escribir:
    json.dump("", escribir)
    
from excepciones import NoSeraMuchoException

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
        try:
            self.edad = int(edad)
        except ValueError:
            print("ValueError: EDAD debe ser un entero")
        except TypeError:
            print("TypeError: EDAD debe ser un entero")
        self._total_compras = 0
        self._total_gastado = 0
            

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

    def set_total_compras(self): #cada vez suma 1
        self._total_compras += 1

    def set_total_gastado(self, compra_actual):
        self._total_gastado += compra_actual
    

    def promedio_compras(self):
        try:
            promedio_compras = self._total_gastado / self._total_compras
            print(f"Promedio de compras del cliente {self.id_cliente} : {promedio_compras}")
            return(promedio_compras)
        except ZeroDivisionError:
            print(f"El cliente {self.id_cliente} aún no tiene compras, y no se puede dividir por cero")


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
        compra.procesar_compra(self)
        
""" 
class Compra:
    def __init__(self, cliente, ordencompra, sucursal, vendedor, cantidad):
        self.cliente = cliente
        self.producto = ordencompra.producto #SKU
        self.sucursal = sucursal
        self.vendedor = vendedor
        self.cantidad = cantidad
        self.con_despacho = ordencompra.despacho
    #logica:
    #hice los minimos cambios posibles para que vendedor pueda ejecutar la venta mediante los recursos que le pase OrdenCompra en vez de acceder a los productos directamente.
    #a futuro presumo que la logica podría ser que la orden de compra incluya la sucursal de origen para determinar de donde descontar el stock y tal.
    def procesar_compra(self): """
   
#============================FIN CLASE VENDEDOR==================================
correlativos_OC = []
class OrdenCompra:
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
    def __init__(self, producto, despacho):
        #Producto ha de ser un objeto producto. Despacho ha de ser bool.
        #id será un correlativo.
            if len(correlativos_OC) == 0: self.Id_ordencompra = 1
            else: 
                self.Id_ordencompra = correlativos_OC[-1]+1
            if type(producto) is Producto: self.producto = producto
            if type(despacho) is bool: self.despacho = despacho
        
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

#inicializar stocks.json



class Empresa:

    def __init__(self, nombre, dirección):
        self._id = nombre
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

    def define_stock(self, sku, nuevo_stock): #override stock
        
        self.stocks[sku] = nuevo_stock

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
        super().__init__(nombre, dirección)           
        self.colaboradores = list(colaboradores)
        self.stocks = stocks #se debe cambiar por llamado a función setter JSON

    def __str__(self):
        return(f"Bodega {self._id}")



## clase sucursal
class Sucursal(Empresa):
    def __init__(self, nombre, dirección, colaboradores, stocks): 
        super().__init__(nombre, dirección)  
        self.colaboradores = list(colaboradores)
        self.stocks = stocks #se debe cambiar por llamado a función setter JSON

    def __str__(self):
        return(f"Sucursal {self._nombre}")
#============================FIN CLASE SUCURSAL==================================

        ##se agrega la clase compra
class Compra:
    def __init__(self, cliente, ordencompra, sucursal, cantidad):
        
        self.cliente = cliente
        self.producto = ordencompra.producto #SKU
        self.sucursal = sucursal

        
        self.cantidad = cantidad
        try:
            if self.cantidad > 10:
                raise NoSeraMuchoException("No se pueden comprar más de 10 unidades")
        except NoSeraMuchoException:
            print(f"No se puede comprar más de 10 unidades, usted intentó comprar {cantidad}")
     
        self.cantidad = cantidad
        self.con_despacho = ordencompra.despacho
    #logica:
    #hice los minimos cambios posibles para que vendedor pueda ejecutar la venta mediante los recursos que le pase OrdenCompra en vez de acceder a los productos directamente.
    #a futuro presumo que la logica podría ser que la orden de compra incluya la sucursal de origen para determinar de donde descontar el stock y tal.
    def procesar_compra(self, vendedor):
        self.vendedor = vendedor
        print(f"Venta inicializada por {self.vendedor.nombre}:")
        gasto = self.cantidad*self.producto.valor_total #el gasto del cliente debe incluir el impuesto
        print("Detalle de la transacción a realizar:")
        print(f"Valor bruto: {self.cantidad}*${self.producto.valor_neto} = {self.cantidad*self.producto.valor_neto}")
        impuestos = int(round(self.producto.valor_neto * (self.producto.impuesto/100)))*self.cantidad #calculo el impuesto de la compra
        print(f"Impuestos: ({self.producto.impuesto}%) ${impuestos}")
        print(f"Valor neto: {self.cantidad}*${self.producto.valor_total} = ${gasto}")
        if self.con_despacho: 
            self.producto.valor_total+=5000 #aumento el valor total del producto por el costo del despacho, individualmente, textual según lo del ejercicio.
            gasto = self.cantidad*self.producto.valor_total #actualizo el gasto para reflejar el costo del despacho
            print(f"Despacho: ${self.cantidad * 5000}")
            print(f"Valor final a pagar:   {self.cantidad}*${self.producto.valor_total} = ${gasto}")

        #cambiar referencia a la de stock dentro de sucursal.... agregar agumento de sucursal y bodega asociada?
        #desde este punto en adelante los cálculos de gasto y comisiones son en base a "gasto" que refleja el monto total a pagar.
        if (self.sucursal.stock(self.producto.sku)>=self.cantidad and self.cliente.saldo()>=gasto)==True:
            
            print("===Saldo y stock antes de transacción==")
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

            #se actualiza total_compra y total_gastado en la respectiva instancia del cliente:
            self.cliente.set_total_compras()
            self.cliente.set_total_gastado(gasto)


            #prints para testear cambios internos
            print("Post transacción:")
            print(f"saldo de cliente es {self.cliente.saldo()}")
            print(f"stock de producto es {self.sucursal.stock(self.producto.sku)}")
            print(f"comision de vendedor {self.vendedor.nombre} es {self.vendedor.get_comision_acumulativa()}")
            print("Compra realizada con éxito.")
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

telovendo = Empresa("Te Lo Vendo", "La Punta del Cerro s/n")
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
cliente3 = Cliente("id3", "Pedro", "Gomez", "XXXXXXXXXXXXXXX", "20-enero", 100000)
cliente4 = Cliente("id4", "Maria", "Lopez", "XXXXXXXXXXXXXXX", "20-marzo", 0)
cliente5 = Cliente("id5", "Luis", "Gonzalez", "XXXXXXXXXXXXXXX", "20-febrero", 0)
