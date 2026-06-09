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


def borrar_historial():
    if os.path.exists(ARCHIVO_HISTORIAL):
        os.remove(ARCHIVO_HISTORIAL)
        print("Historial borrado.")
    else:
        print("No habia historial que borrar.")


def mostrar_menu():
    print("\n--- Calculadora ---")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. Potencia")
    print("6. Ver historial")
    print("7. Borrar historial")
    print("8. Salir")


# Diccionario que mapea cada opcion del menu con su funcion correspondiente
operaciones = {
    "1": ("Suma",        sumar),
    "2": ("Resta",       restar),
    "3": ("Multiplicacion", multiplicar),
    "4": ("Division",    dividir),
    "5": ("Potencia",    potencia),
}


def main():
    print("Bienvenido a la calculadora con historial.")

    while True:
        mostrar_menu()
        opcion = input("\nElige una opcion: ").strip()

        if opcion in operaciones:
            nombre, funcion = operaciones[opcion]

            a = pedir_numero("Primer numero: ")
            b = pedir_numero("Segundo numero: ")

            try:
                resultado = funcion(a, b)
                # Se arma el string de la operacion para mostrarlo y guardarlo
                expresion = f"{a} {nombre} {b}"
                print(f"Resultado: {resultado}")
                guardar_en_historial(expresion, resultado)

            except ValueError as e:
                # Esto atrapa el error de division entre cero que lanzamos arriba
                print(f"Error: {e}")

        elif opcion == "6":
            ver_historial()

        elif opcion == "7":
            borrar_historial()

        elif opcion == "8":
            print("Hasta luego.")
            break

        else:
            print("Opcion no valida, elige un numero del 1 al 8.")


main()