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