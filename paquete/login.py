import os
import json


DB = { 
    'Aibn': 'Cerrado'
}

ruta_archivo = "mi_archivo.txt"

# Abrir el archivo en modo de escritura

# ---------------- Functions 
def validarUser(user, DB):
    while user in DB:
        print("El Nombre de usuario ya existe")
        user = input("Escriba otro nombre de usuario")
    return user

    #Regustro de usuario
def registrarUsuario(DB):
    os.system('cls')
    print("Para registrarse ingrese un nombre de usuario:")
    new_user = input()
    new_user = validarUser(new_user, DB) # verifico que el usuario no exista, si no existe, lo creo.
    print("Ingrese una contraseña")
    new_pass = input()
    DB[new_user] = new_pass
    print("Usuario Registrado")
    menuPrincipal(DB)

    #verificar contraseña
def comprobarContraseña(user,DB):
    print("Usuario: ", user, " ingrese su contraseña")
    password = input()
    while DB[user] != password:
        print("Contraseña incorrecta, vuelva a intentarlo")
        password = input()
    
def ingresarAlPrograma(user, DB):    
    comprobarContraseña(user, DB)
    os.system('cls')
    print("Bienvenido: ", user)
    print("Sesion iniciada")
    menuDelPrograma()

def imprimirDatos():
    with open(ruta_archivo, 'w') as archivo:
        json.dump(DB, archivo)


# Menu del programa para ver o crear un txt con los datos de DB
def menuDelPrograma():
    print("Menu del programa: Ver datos: 1 Imprimir datos: 2 Volver al menu principal: 3")

    opcion = int(input())

    if opcion == 1:
        print(DB)
        menuDelPrograma()

    elif opcion == 2:
        imprimirDatos()
        print("Datos guardados en : ", ruta_archivo)
        menuDelPrograma()
    else:
        menuPrincipal(DB)


def menuPrincipal(DB):

    print("Que desea hacer? Ingresar: 1 Registrar Nuevo Usuario: 2 Salir: 3")

    opcion = int(input("Seleccione una opcion: "))

    while opcion not in [1, 2, 3]:
        os.system('cls')
        print("Error, opcion no valida...")
        print("Ingrese una opcion valida: -Ingresar: 1 -Registrarse: 2 -Salir: 3")
        opcion = int(input("Seleccione una opcion: "))

    if opcion == 1:
        print("Por favor ingrese su Usuario:")
        user = input()
        while user not in DB:
            print("El usuario: ", user, " no existe. Vuelva a intentarlo.")
            user = input(": ")
    
        os.system('cls')
        ingresarAlPrograma(user, DB)
        

    elif opcion == 2:
        registrarUsuario(DB)    
        print("Usuario registrado correctamente")
        menuPrincipal(DB)

    else:
        print("Gracias por utilizar el programa, adios")
        exit()

#---------------- Program


os.system('cls')
print("Hola, bienvenido.")

menuPrincipal(DB)


# Notas: quise modularizar pero al final me quedo todo en un solo modulo. Tengo que checkear eso disculpas! 
# No hice que el txt se guarde en el drive porq me parecio mucho usar la Api de google, o por lo menos es la manera que creo que se puede hacer, no lo comprobe 
# Para poder ver los datos de DB o imprimirlos en un txt es necesario ingresar, para ingresar es necesario tener un usuario registrado!
