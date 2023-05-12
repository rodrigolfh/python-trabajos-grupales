from main import *

#cliente1 = Cliente("id1", "Ignacio", "Fuentealba", "correo@gmail.com", "25-enero", 25000000)
#producto1 = Producto("001", "Producto 1", "Menaje", proveedor1, 100, 19990)

clientes.append(cliente1)

#print(f"Saldo de {cliente1.nombre} es {cliente1.saldo}")
#cliente1.saldo -= 5
#print(f"Saldo de {cliente1.nombre} es {cliente1.saldo}")
#print("==================================================")
print(f"stock de producto SKU:{producto1.sku} es de {sucursal_mall_plaza.stock('001')}")
sucursal_mall_plaza.stock("001", +5)
print(f"stock de producto SKU:{producto1.sku} es de {sucursal_mall_plaza.stock('001')}")
sucursal_mall_plaza.stock("001", -5)
print(f"stock de producto SKU:{producto1.sku} es de {sucursal_mall_plaza.stock('001')}")

print("==================================================")
print("=========================pruebas de transacciones=========================")
#compra1 = Compra(cliente1, producto1, sucursal_mall_plaza, vendedor1, 1001)#para probar desbordado de stock
#compra1 = Compra(cliente1, producto1, sucursal_mall_plaza, vendedor1, 4)

ocv20231 = OrdenCompra(producto1, True)
ocv20232 = OrdenCompra(producto2, False)
compra1 = Compra(cliente2, producto1, sucursal_mall_plaza, vendedor3, 10, True) 
compra1 = Compra(cliente2, producto1, sucursal_mall_plaza, vendedor3, 10, True)

vendedor3.vender(compra1)
compra2 = Compra(cliente1, producto3, sucursal_mall_plaza, vendedor1, 10, False)
vendedor1.vender(compra2)
compra1.procesar_compra()
compra2.procesar_compra()
print(vendedor1.porcentaje_comision())
vendedor1.porcentaje_comision("12345677-1", 50)

compra1 = Compra(cliente1, ocv20231, sucursal_mall_plaza, 10)
#vendedor3.vender(compra1)
compra2 = Compra(cliente1, ocv20232, sucursal_mall_plaza, 10)
vendedor1.vender(compra1)
#compra1.procesar_compra()
#compra2.procesar_compra()
#vendedor1.porcentaje_comision("12345677-1", 50)
print("==================================================")
print("pruebas nuevas clases Sucursal y Bodega")
print("sucursal", sucursal_mall_plaza.stocks)
sucursal_mall_plaza.stock("001", 49) #agrega stock
sucursal_mall_plaza.stock("002", -47) #quita stock
sucursal_mall_plaza.stock("004", 46) #agrega stock
bodega_principal.define_stock("003", 0) #probando quiebre stock
bodega_principal.define_stock("005", 199) #probando stock menor a límite
print("sucursal", sucursal_mall_plaza.stocks)
print("bodega", bodega_principal.stocks)
sucursal_mall_plaza.revisar_stocks(50, 300, bodega_principal)
print("bodega", bodega_principal.stocks)
print("sucursal", sucursal_mall_plaza.stocks)


#Pruebas de try-except:

#TypeError:
cliente5 = Cliente("id5", "Luis", "Gonzalez", "XXXXXXXXXXXXXXX", "20-febrero", "cuarenta")

bodega_principal.define_stock(3, 0) #probando quiebre stock

#pruebas de try-except:

#TypeError por formato de edad:
cliente6 = Cliente("id5", "Luis", "Gonzalez", "XXXXXXXXXXXXXXX", "20-febrero", 0, "cuarenta")

#Excepción personalizada

compra3 = Compra(cliente1, producto3, sucursal_mall_plaza, vendedor1, 11, False)

#Excepción promedio compras:

cliente3.promedio_compras() #cliente sin compras
cliente1.promedio_compras() #cliente con compras

#probar ValueError en función revisar_stocks:
#bodega_principal.define_stock(3, 0) #probando quiebre stock


