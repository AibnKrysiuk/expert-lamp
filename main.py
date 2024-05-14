from paquete.cliente import cliente
from paquete.tienda import Tienda

#from paquete.login import *


cliente1 = cliente("Pedro","Cordera","45", 38456985,"0116558496","pedro_cordera@gmail.com")
cliente1.info_cliente

print(cliente1.comprar(3, "Alfajores", "Lo de Armando"))
cliente1.add_elementos_deseado("Golosinas")
cliente1.add_elementos_deseado("Bebidas")
cliente1.add_elementos_deseado("Comics")
print(cliente1.comprar(2, "Coca-Cola", "Ypf-Confiteria"))
print(cliente1.mostrar_puntos())
print(cliente1.comprar(2, "Chicles", "Ypf-Confiteria"))

cliente1.ver_lista_elementos_deseados()
cliente1.ver_elemento_en_mochila()
cliente1.vaciar_mochila()
print(cliente1.comprar(2, "Chicles", "Ypf-Confiteria"))
cliente1.ver_elemento_en_mochila()

cliente1.info_cliente()
print(cliente1)