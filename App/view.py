import sys
import App.logic as logic
from tabulate import tabulate
def new_logic():
    """
        Se crea una instancia del controlador
    """
    #TODO: Llamar la función de la lógica donde se crean las estructuras de datos
    control = logic.new_logic()
    return control

def print_menu():
    print("Bienvenido")
    print("0- Cargar información")
    print("1- Ejecutar Requerimiento 1")
    print("2- Ejecutar Requerimiento 2")
    print("3- Ejecutar Requerimiento 3")
    print("4- Ejecutar Requerimiento 4")
    print("5- Ejecutar Requerimiento 5")
    print("6- Ejecutar Requerimiento 6")
    print("7- Salir")

def load_data(control):
    """
    Carga los datos
    """
    #TODO: Realizar la carga de datos
    catalog, tiempo, tamaño, menor, mayor, primeros, ultimos = logic.load_data(control)
    info = [
        ["Tiempo de carga (ms)", tiempo],
        ["Total registros cargados", tamaño],
    ]

    if menor:
        info.append([
            "Computador más antiguo:",
            f"{menor['model']} | "
            f"{menor['brand']} | "
            f"{menor['release_year']} | "
            f"${menor['price']}"
        ])

    if mayor:
        info.append([
            "Computador más reciente:",
            f"{mayor['model']} | "
            f"{mayor['brand']} | "
            f"{mayor['release_year']} | "
            f"${mayor['price']}"
        ])

    if primeros:
        info.append(["Primeros registros cargados:", primeros])

    if ultimos:
        info.append(["Últimos registros cargados:", ultimos])

    return catalog, info


def print_data(control, id):
    """
        Función que imprime un dato dado su ID
    """
    #TODO: Realizar la función para imprimir un elemento
    pass

def print_req_1(control, marca):
    """
        Función que imprime la solución del Requerimiento 1 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 1
    info = logic.req_1(control, marca)
    print(tabulate(info))


def print_req_2(control, min, max):
    """
        Función que imprime la solución del Requerimiento 2 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 2
    info = logic.req_2(control, min, max)
    print(tabulate(info))


def print_req_3(control, cpu_brand, cpu_tier):
    """
        Función que imprime la solución del Requerimiento 3 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 3
    info = logic.req_3(control, cpu_brand, cpu_tier)
    print(tabulate(info))
    


def print_req_4(control, cpu_brand, gpu_model):
    """
        Función que imprime la solución del Requerimiento 4 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 4
    info = logic.req_4(control, cpu_brand, gpu_model)
    print(tabulate(info))


def print_req_5(control, min, max, resolucion,solicitud):
    """
        Función que imprime la solución del Requerimiento 5 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 5
    info = logic.req_5(control, min, max, resolucion,solicitud)
    print(tabulate(info))


def print_req_6(control, año_inicial, año_final):
    """
        Función que imprime la solución del Requerimiento 6 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 6
    info = logic.req_6(control, año_inicial, año_final)
    print(tabulate(info))

# Se crea la lógica asociado a la vista
control = new_logic()

# main del ejercicio
def main():
    """
    Menu principal
    """
    working = True
    #ciclo del menu
    while working:
        print_menu()
        inputs = input('Seleccione una opción para continuar\n')
        if int(inputs) == 0:
            print("Cargando información de los archivos ....\n")
            catalog, info= load_data(control)
            print(tabulate(info))
        elif int(inputs) == 1:
            marca = input('Indique la marca\n')
            print_req_1(control, marca)

        elif int(inputs) == 2:
            min = input("Ingrese el precio minimo\n")
            max = input("Ingrese el precio maximo\n")
            print_req_2(control, min, max)

        elif int(inputs) == 3:
            cpu_brand = input("Ingrese la marca del CPU: ")
            cpu_tier = input("Ingrese el tier del CPU: ")
            print_req_3(control, cpu_brand, cpu_tier)

        elif int(inputs) == 4:
            
            cpu_brand = input('Ingrese la marca de cpu\n')
            gpu_model = input("Ingrese el modelo de gpu\n")
            print_req_4(control,cpu_brand, gpu_model)

        elif int(inputs) == 5:
            min = input("Ingrese el anio minimo\n")
            max = input("Ingrese el anio maximo\n")
            resolucion = input("Ingrese la resolucion de pantalla(widthxheight)\n")
            solicitud = input("Deseea que sea BARATO o CARO\n")
            print_req_5(control, min,max,resolucion, solicitud)

        elif int(inputs) == 6:
            inicial = int(input("Ingrese el anio inicial\n"))
            final = int(input("Ingrese el anio final\n"))
            print_req_6(control, inicial,final)

        elif int(inputs) == 7:
            working = False
            print("\nGracias por utilizar el programa") 
        else:
            print("Opción errónea, vuelva a elegir.\n")
    sys.exit(0)
