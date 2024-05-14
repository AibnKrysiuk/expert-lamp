class cliente:

    def __init__(self, nombre, apellido, edad, dni, telefono, email):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.dni = dni
        self.telefono = telefono
        self.email = email
        self.lista_elementos_deseados = []
        self.mochila = []
        self.espacio_mochila = 5
        self.puntos = 0

    def info_cliente(self):
        print("Nombre: ", self.nombre)
        print("Apellido: ", self.apellido)
        print("Edad: ", self.edad)
        print("Dni: ",self.dni)
        print("Tel: ",self.telefono)
        print("E-mail: ",self.email)

# Compra
    def comprar(self, cantidad, producto, tienda):
        if self.espacio_mochila >= cantidad:
            self.puntos += 10
            self.mochila.append(producto)
            self.espacio_mochila -= cantidad
            return f"\nEl cliente {self.nombre} {self.apellido} compró {cantidad} {producto} en la tienda \"{tienda}\".\nLos detalles de la factura fueron enviados al mail {self.email}."
        else:
            return f"\n{self.nombre} no tienes espacio en la mochila para llevar el producto, no puedes realizar la compra."
    
    def ver_elemento_en_mochila(self):
        if self.mochila:
            print("Mochila: ")
            print(f"Espacio en la mochila: {self.espacio_mochila}")
            for elemento in self.mochila:                
                print("-", elemento)
        else:
            print(f"La lista de deseos de {self.nombre} {self.apellido} está vacía.")

    def vaciar_mochila(self):
        self.mochila = []
        self.espacio_mochila = 5
        print("Mochila vaciada con exito")

    def add_elementos_deseado(self, elemento):
        self.lista_elementos_deseados.append(elemento)
        return f"\n Se agrego: {elemento}, a la lista de intereses."
    
    def ver_lista_elementos_deseados(self):
        if self.lista_elementos_deseados:
            print("Lista de deseados: ")
            for elemento in self.lista_elementos_deseados:                
                print("-", elemento)
        else:
            print(f"La lista de deseos de {self.nombre} {self.apellido} está vacía.")

    def mostrar_puntos(self):
        return f"\nCantidad de puntos del cliente {self.nombre} es: {self.puntos}."

    def __str__(self):
        return f"\nHola, mi nombre es {self.nombre} {self.apellido}, tengo {self.edad} años, \nDNI: {self.dni}.\ntelefono: {self.telefono}.\n E-mail: {self.email}.\n."