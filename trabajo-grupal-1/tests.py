import main
from main import *

clientes.append(cliente1)
clientes.append(cliente2)
clientes.append(cliente3)
clientes.append(cliente4)
clientes.append(cliente5)

print(f"Saldo de {cliente1.nombre} es {cliente1.get_saldo()}")
cliente1.set_saldo(-500)
print(f"Saldo de {cliente1.nombre} es {cliente1.get_saldo()}")
#producto1.stock(-500)
#producto3.stock(50)
print(f"stock de {producto1.nombre} es {producto1.stock}")
producto1.stock -= 500
#producto1.stock = producto1.stock - 500
print(f"stock de {producto1.nombre} es {producto1.stock}")
