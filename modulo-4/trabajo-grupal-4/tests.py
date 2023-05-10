import main
from main import *

#cliente1 = Cliente("id1", "Ignacio", "Fuentealba", "correo@gmail.com", "25-enero", 25000000)
#producto1 = Producto("001", "Producto 1", "Menaje", proveedor1, 100, 19990)

clientes.append(cliente1)

#print(f"Saldo de {cliente1.nombre} es {cliente1.saldo}")
#cliente1.saldo -= 5
#print(f"Saldo de {cliente1.nombre} es {cliente1.saldo}")
#print("==================================================")
print(f"stock de {producto1.nombre} es {producto1.stock()}")
producto1.stock(-5, 10, 5)
print(f"stock de {producto1.nombre} es {producto1.stock()}")
producto1.stock(-5)
producto1.stock()
print(f"stock de {producto1.nombre} es {producto1.stock()}")
print("==================================================")
print("=========================pruebas de transacciones=========================")
compra1 = Compra(cliente1, producto1, vendedor1, 10)#para probar desbordado de stock
compra1 = Compra(cliente1, producto1, vendedor1, 4)
compra1.procesar_compra()
print(vendedor1.porcentaje_comision())
vendedor1.porcentaje_comision("12345677-1", 50)

print("pruebas nuevas clases Sucursal y Bodega")
print("sucursal", sucursal_mall_plaza.stocks)
sucursal_mall_plaza.set_stock("002", 49)
sucursal_mall_plaza.set_stock("003", 47)
sucursal_mall_plaza.set_stock("005", 46)
bodega_principal.set_stock("003", 0)
bodega_principal.set_stock("005", 199)
print("sucursal", sucursal_mall_plaza.stocks)
print("bodega", bodega_principal.stocks)
sucursal_mall_plaza.revisar_stocks(50, 300, bodega_principal)
print("bodega", bodega_principal.stocks)
print("sucursal", sucursal_mall_plaza.stocks)