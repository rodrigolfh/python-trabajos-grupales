import main
from main import *

clientes.append(cliente1)
clientes.append(cliente2)
clientes.append(cliente3)
clientes.append(cliente4)
clientes.append(cliente5)

print(cliente1.get_saldo())
#cliente1.set_saldo(-500, 5, 10)
cliente1.set_saldo(20, 5, -5)
producto1.set_stock(-500)
producto3.set_stock(50)
print(cliente1.get_saldo()) 