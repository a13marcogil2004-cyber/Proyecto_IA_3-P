# calculadora.py
import os

# Archivo donde se guarda el historial de operaciones
ARCHIVO_HISTORIAL = "historial.txt"


def sumar(a, b):
    return a + b

def restar(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    # La division por cero no esta permitida, hay que revisarlo antes
    if b == 0:
        raise ValueError("No se puede dividir entre cero")
    return a / b

def potencia(a, b):
    return a ** b


def pedir_numero(mensaje):
    # Se intenta leer el numero hasta que el usuario escriba algo valido
    while True:
        try:
            return float(input(mensaje))
        except ValueError:
            print("Eso no es un numero valido, intentalo de nuevo.")


def guardar_en_historial(operacion, resultado):
    # Se abre el archivo en modo append para no borrar lo anterior
    with open(ARCHIVO_HISTORIAL, "a") as f:
        f.write(f"{operacion} = {resultado}\n")


def ver_historial():
    # Si el archivo no existe todavia, se avisa al usuario
    if not os.path.exists(ARCHIVO_HISTORIAL):
        print("Todavia no hay historial guardado.")
        return

    with open(ARCHIVO_HISTORIAL, "r") as f:
        contenido = f.read()

    if not contenido:
        print("El historial esta vacio.")
    else:
        print("\n--- Historial de operaciones ---")
        print(contenido)
