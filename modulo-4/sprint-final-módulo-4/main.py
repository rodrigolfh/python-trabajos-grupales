from datetime import datetime
from excepciones import NoSeraMuchoException
import json
import os

class InventarioMixin(): 
    
    #Esta clase es un "Mixin", una clase sin constructor, que toma los atributos desde donde se llama
    
    #la función .línea(*) crea una entrada de diccionario con el saldo actualizado y más información relevante,  y la agrega al json stocks.json.
    def línea(self, tipo_movimiento = None, producto= None, documento_asociado = None, responsable= None, desde = None, hacia = None, movimiento = 0, saldo = 0):
        """Agrega una línea al registro de stocks.json"""
        timestamp = datetime.now().timestamp() #timestamp en formato UNIX, ej: 1669123919.331225, más fácil para ordenar y da un valor único que sirve de ID
        tipo_lugar = self.tipo_lugar #Sucursal o Bodega, lo saca de la clase
        nombre_lugar = self._id #nombre instancia
        self.tipo_movimiento = tipo_movimiento
        tipo_movimiento = tipo_movimiento #por ejemplo reposición, venta, override (override con define_stock de Empresa)
        documento_asociado = documento_asociado #ej: orden de compra
        desde = desde # ej: desde sucursal
        hacia = hacia # hacia rut cliente
        if not movimiento:
            movimiento = 0
        
        ruta_archivo = "stocks.json"
        #buscar último saldo
        if os.path.isfile(ruta_archivo) and os.path.getsize(ruta_archivo) > 0: #si el archivo existe y no está vacío:
                
            with open('stocks.json', 'r') as archivo: #abrir el archivo en modo lectura
                json_data = archivo.read()

            # Des-serializar el contenido del archivo
            datos_json = json.loads(json_data)
            último_timestamp = 0
            último_saldo = 0

            #buscar último saldo de nombre_lugar 
            for item in datos_json:
                if datos_json[item]["nombre_lugar"] == nombre_lugar and datos_json[item]["producto"] == producto and float(item) > float(último_timestamp):
                    último_timestamp = item
                    último_saldo = datos_json[último_timestamp]["saldo"] 
            if tipo_movimiento != "override": #si el movimiento NO es override, se puede calcular el saldo.
                nuevo_saldo = último_saldo + movimiento
                
            elif tipo_movimiento == "override": #si el movimiento SI es un override de define_stock, el saldo nuevo será el definido por el override
                nuevo_saldo = saldo

        #se crea nueva línea para luego agregarla a stocks.json        
        nueva_línea =  {"tipo_lugar": tipo_lugar, "nombre_lugar": nombre_lugar, "tipo_movimiento": tipo_movimiento, "producto": producto, "documento_asociado": documento_asociado, "responsable": responsable, "desde": desde, "hacia": hacia, "movimiento": movimiento, "saldo": nuevo_saldo}

        if os.path.isfile(ruta_archivo) and os.path.getsize(ruta_archivo) > 0: #si el archivo existe y no está vacío:
                
            with open('stocks.json', 'r') as archivo: #abrir el archivo en modo lectura
                json_data = archivo.read()

            # Des-serializar el contenido del archivo
            datos_json = json.loads(json_data)
            datos_json[timestamp] = nueva_línea
        else:
            datos_json = {} 
            datos_json[timestamp] = nueva_línea
        
        actualizado_json = json.dumps(datos_json, indent=4)
        # Sobreescribe el json con actualizado_json
        with open('stocks.json', 'w') as file:
            file.write(actualizado_json)

    def stock(self, sku): #como es un mixin, el self es el de la clase que llama a esta.
        """Devuelve stock"""
        nombre_lugar = self._id
        producto = sku
        with open('stocks.json', 'r') as archivo: #abrir el archivo en modo lectura
            json_data = archivo.read()
               # Des-serializar el contenido del archivo
            datos_json = json.loads(json_data)
            último_timestamp = 0
           
            try:
                for item in datos_json: #buscar el último timestamp
                    if datos_json[item]["nombre_lugar"] == nombre_lugar and datos_json[item]["producto"] == producto and float(item) > float(último_timestamp):
                        último_timestamp = item
                return(datos_json[último_timestamp]["saldo"])
            except KeyError: # cuando último_timestamp = 0, por lo tanto devolvemos 0 porque NO existe registro de dicho producto.
                return 0
#
#
#
#
#vestigio de trabajos anteriores   EVALUAR QUITAR
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
    def __str__(self):
        return self.nombre

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
    
    def __str__(self):
        return self.nombre

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
    def __str__(self):
        return ("OC" + self.Id_ordencompra)
        
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
    
    def __str__(self):
        return self.sku
    
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



class Empresa(InventarioMixin):

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
     
    
    def define_stock(self, sku, nuevo_stock): #override stock
        
        self.stocks[sku] = nuevo_stock
        self.línea(tipo_movimiento = "override", producto=sku, saldo=nuevo_stock)

    def stock(self, sku, modificación_stock = None, tipo_movimiento = None,  documento_asociado = None, responsable = None, desde = None, hacia = None): #obtiene la cantidad de unidades de un sku dado, o redefine si se le entrega además una cantidad
        #mantiene funcionalidad del método stock que tenía la clase Producto
        self.modificación_stock = modificación_stock
        self.tipo_movimiento = tipo_movimiento
        self.producto = sku
        self.documento_asociado = documento_asociado
        self.responsable = responsable
        self.desde = desde
        self.hacia = hacia
        if modificación_stock == None:
            return super().stock(sku) 
        
        
        elif modificación_stock:
            self.stocks[sku] += modificación_stock
            print(f"El producto SKU:{sku} se modificó así: {modificación_stock:+}.") #:+ muestra el signo, sino cuando es positivo no se ve
            self.línea(tipo_movimiento = self.tipo_movimiento, documento_asociado = self.documento_asociado, producto = self.producto, responsable = self.responsable, desde = self.desde, hacia = self.hacia , movimiento = self.modificación_stock)

    def revisar_stocks(self, límite, pedido, bodega): #revisa si stocks bajan de cierto número para pedir más a bodega.
        self.límite = límite  #si baja de esto, se pide a bodega
        self.pedido = pedido  #tamaño estándar de pedido a bodega
        self.bodega = bodega  #bodega de la que se sacaría reposición

        for key, value in self.stocks.items():
            if self.stocks[key] < self.límite and self.bodega.stock(key) >= self.pedido: #si baja del límite y = o + del límite
                print(f"Stock del producto SKU {key} ha bajado de {self.límite}. Pidiendo {self.pedido} a {self.bodega}")
                self.bodega.stock(key, -self.pedido) #descuenta de bodega                    
                self.línea(tipo_movimiento = "revisa_stock", documento_asociado = None, desde = self.bodega, hacia = "sucursal", movimiento = -self.pedido, saldo=None)
                self.stock(key, +self.pedido) #agrega a sucursal
                print(f"Se ha repuesto {self.pedido} al stock del producto SKU: {key}")
                self.línea(tipo_movimiento = "revisa_stock", documento_asociado = None, desde = self.bodega, hacia = "sucursal", movimiento = self.pedido, saldo=None)
            
            elif self.stocks[key] < self.límite and self.bodega.stock(key) == 0:
                print(f"El producto SKU: {key} tiene sólo {value} unidades y se agotó en bodega")
            
            elif (self.stocks[key] < self.límite) and (self.bodega.stock(key) < self.pedido): #sino, se pide todo lo que quede en la bodega de ese sku
                lo_que_queda = self.bodega.stock(key)
                self.bodega.stock(key, -lo_que_queda)
                self.línea(tipo_movimiento = "revisa_stock", documento_asociado = None, desde = self.bodega, hacia = "sucursal", movimiento = -lo_que_queda, saldo=None)
                self.stock(key, +lo_que_queda) #agrega a sucursal lo que quedaba en bodega
                self.línea(tipo_movimiento = "revisa_stock", documento_asociado = None, desde = self.bodega, hacia = "sucursal", movimiento = lo_que_queda, saldo=None)
                
                print(f"Solo quedaban {lo_que_queda} unidades del producto SKU:{key}, se repusieron todas")
 




class Bodega(Empresa):
    """funcionarios es un dict con key ruts y value "activo" o "inactivo", stocks es un dict con key asociado a SKU y value la cantidad"""
    def __init__(self, nombre, dirección, colaboradores, stocks): 
        super().__init__(nombre, dirección)           
        self.colaboradores = list(colaboradores)
        self.stocks = stocks #se debe cambiar por llamado a función setter JSON
        self.tipo_lugar = "Bodega"
        
    def __str__(self):
        return "Bodega" + self.nombre 



## clase sucursal
class Sucursal(Empresa):
    def __init__(self, nombre, dirección, colaboradores, stocks): 
        super().__init__(nombre, dirección)  
        self.colaboradores = list(colaboradores)
        self.stocks = stocks #se debe cambiar por llamado a función setter JSON
        self.tipo_lugar = "sucursal"
        

    def __str__(self):        
        return "Sucursal" + self.nombre
#============================FIN CLASE SUCURSAL==================================

        ##se agrega la clase compra. funciona sin agregar como herencia Sucursal, Bodega, Vendedor, Cliente, y OrdenCompra,
        #pero si no se agregan Compra no accede a los __str__ de estas.
class Compra(Sucursal, Bodega, Vendedor, Cliente, OrdenCompra, InventarioMixin): 

    def __init__(self, cliente, ordencompra, sucursal, cantidad):
        
        self.cliente = cliente
        self.producto = ordencompra.producto #SKU
        self.sucursal = sucursal
        self.orden_de_compra = ordencompra
        self.tipo_lugar = "sucursal"
        self._id = sucursal
        
        self.cantidad = cantidad
        super().__str__
       
        try:
            if self.cantidad > 10:
                raise NoSeraMuchoException("No se pueden comprar más de 10 unidades")
        except NoSeraMuchoException:
            print(f"No se puede comprar más de 10 unidades, usted intentó comprar {cantidad}")
     
       
        self.con_despacho = ordencompra.despacho

        def __str__(self):
            return self.orden_de_compra
    #logica:
    #hice los minimos cambios posibles para que vendedor pueda ejecutar la venta mediante los recursos que le pase OrdenCompra en vez de acceder a los productos directamente.
    #a futuro presumo que la logica podría ser que la orden de compra incluya la sucursal de origen para determinar de donde descontar el stock y tal.
    def procesar_compra(self, vendedor):
        self.vendedor = vendedor
        self.tipo_movimiento = "compra" #para usar en InventarioMixin
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
            self.desde = self.sucursal._id
            self.hacia = self.cliente.id_cliente
           
            self.sucursal.stock(self.producto.sku, modificación_stock = -self.cantidad, tipo_movimiento = "compra", documento_asociado = self.orden_de_compra.Id_ordencompra, responsable = self.vendedor.run, desde = self.desde, hacia = self.hacia)
            
            #descuento a través de InventarioMixin:
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
bodega_principal = Bodega("Bodega Principal", "Calle 1 sin número", {"12345677-1": True, "12345688-2": True, "12345655-4": True}, {"001": 10000,"002": 10000,"003": 10000,"004": 10000,"005": 10000})
sucursal_mall_plaza = Sucursal("Sucursal Mall Plaza", "Calle 2 sin número", {"12345677-1": True, "12345688-2": True, "12345655-4": True}, {"001": 1000,"002": 1000,"003": 1000,"004": 1000,"005": 1000})

vendedor1 = Vendedor("12345677-1", "Hugo", "Araya", "Zapatería",  5, 50)
vendedor2 = Vendedor("12345688-2", "Paco", "Iriarte", "Deportes", 5, 51)
vendedor3 = Vendedor("12345699-3", "Luis", "Gómez", "Juguetería", 5, 52)
vendedor4 = Vendedor("12345655-4", "Ana", "Rodríguez", "Electro", 5, 53)
vendedor5 = Vendedor("12345622-5", "María", "González", "Menaje", 5, 54)

#Se debe crear métodos en la clase Cliente, lo cual puedan agregar y mostrar saldo.
#Como se encuentra trabajando en el desarrollo del módulo de Python Básico, se solicita integrar
#correctamente los métodos de las clases en las opciones del menú desarrollado.
cliente1 = Cliente("14566333-2", "Ignacio", "Fuentealba", "correo@gmail.com", "25-enero", 25000000)
cliente2 = Cliente("14563533-4", "Juan", "Perez", "pepo@hotmail.com", "15-enero", 0)
cliente3 = Cliente("14521433-5", "Pedro", "Gomez", "XXXXXXXXXXXXXXX", "20-enero", 100000)
cliente4 = Cliente("14566643-k", "Maria", "Lopez", "XXXXXXXXXXXXXXX", "20-marzo", 0)
cliente5 = Cliente("14566133-3", "Luis", "Gonzalez", "XXXXXXXXXXXXXXX", "20-febrero", 0)
