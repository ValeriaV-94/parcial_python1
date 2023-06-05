import json
from pathlib import Path

##almacenamiento

def almacenar_registro(usuario, contrasenia):
    archivo = Path("BDregistros.json")
    if archivo.exists():
        with archivo.open("r") as f:
            registros = json.load(f)
    else:
        registros = {}

    registros[usuario] = contrasenia

    with archivo.open("w") as f:
        json.dump(registros, f)

    print("Registro guardado")

##mostrar datos almacenados

def mostrar_registros():
    archivo = Path("BDregistros.json")
    if archivo.exists():
        with archivo.open("r") as f:
            registros = json.load(f)
        for usuario, contrasenia in registros.items():
            print(f"{usuario}: {contrasenia}")
    else:
        print("No hay registros")


##inicio de sesion

def login():
    archivo = Path("BDregistros.json")
    if archivo.exists():
        with archivo.open("r") as f:
            registros = json.load(f)
    else:
        registros = {}

    usuario = input("Ingrese su usuario: ")
    if usuario not in registros:
        print("Usuario no encontrado")
        return

    intentos = 3
    while intentos > 0:
        contrasenia = input("Ingrese su contrasenia: ")
        if contrasenia == registros[usuario]:
            print("Inicio de sesión exitoso")
            break
        else:
            intentos -= 1
            print(f"contrasenia incorrecta. Intentos restantes {intentos}")
    else:
        print("No quedan mas intentos, se ha bloqueados la sesion")


##prueba

def main():
    while True:
        accion = input("¿Que desea hacer? [nuevo_registro/mostrar_registros/login/salir]: ")
        if accion.lower() == "nuevo_registro":
            usuario = input("Ingrese nuevo usuario: ")
            contrasenia = input("Ingrese nueva contrasenia: ")
            almacenar_registro(usuario, contrasenia)
        elif accion.lower() == "mostrar_registros":
            mostrar_registros()
        elif accion.lower() == "login":
            login()
        elif accion.lower() == "salir":
            break
        else:
            print("Opcion no valida")

if __name__ == "__main__":
    main()

