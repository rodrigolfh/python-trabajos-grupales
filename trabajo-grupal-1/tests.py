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