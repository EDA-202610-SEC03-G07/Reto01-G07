import csv
import os
import time
from DataStructures.List import array_list as lt
from DataStructures.Queue import queue as q
from DataStructures.Stack import stack as st
from DataStructures.List import single_linked_list as sl
csv.field_size_limit(2147483647)

def new_logic():
    catalog= {
        'computadores':None,
        'Modelos':None,
        'Marcas':None,
        'Año':None,
        'Cpu':None,
        'Gpu':None,
        'Precio':None}
        
    catalog['computadores'] = lt.new_list()
    catalog['Modelos'] = lt.new_list()
    catalog['Marcas'] = lt.new_list()
    catalog['Año'] = lt.new_list()
    catalog['Cpu'] = lt.new_list()
    catalog['Gpu'] = lt.new_list()
    catalog["Precio"] = lt.new_list()
    
    return catalog
    """
    Crea el catalogo para almacenar las estructuras de datos
    """
    #TODO: Llama a las funciónes de creación de las estructuras de datos

# Funciones para la carga de datos

def load_data(catalog):
    incio=get_time()
    
    data_dir='Data/computer_prices_large.csv'
    with open(data_dir, encoding="utf-8") as file:
        archivo = csv.DictReader(file)
        for llave in archivo:
            llave["device_type"]=str(llave["device_type"])
            llave["brand"]=str(llave["brand"])
            llave["model"]=str(llave["model"])
            llave["release_year"]=int(llave["release_year"])
            llave["os"]=str(llave["os"])
            llave["form_factor"]=str(llave["form_factor"])
            llave["cpu_brand"]=str(llave["cpu_brand"])
            llave["cpu_model"]=str(llave["cpu_model"])
            llave["cpu_tier"]=int(llave["cpu_tier"])
            llave["cpu_cores"]=int(llave["cpu_cores"])
            llave["cpu_threads"]=int(llave["cpu_threads"])
            llave["cpu_base_ghz"]=float(llave["cpu_base_ghz"])
            llave["cpu_boost_ghz"]=float(llave["cpu_boost_ghz"])
            llave["gpu_brand"]=str(llave["gpu_brand"])
            llave["gpu_model"]=str(llave["gpu_model"])
            llave["gpu_tier"]=int(llave["gpu_tier"])
            llave["vram_gb"]=int(llave["vram_gb"])
            llave["ram_gb"]=int(llave["ram_gb"])
            llave["storage_type"]=str(llave["storage_type"])
            llave["storage_gb"]=int(llave["storage_gb"])
            llave["storage_drive_count"]=int(llave["storage_drive_count"])
            llave["display_type"]=str(llave["display_type"])
            llave["display_size_in"]=float(llave["display_size_in"])
            llave["resolution"]=str(llave["resolution"])
            llave["refresh_hz"]=int(llave["refresh_hz"])
            llave["battery_wh"]=float(llave["battery_wh"])
            llave["charger_watts"]=int(llave["charger_watts"])
            llave["psu_watts"]=int(llave["psu_watts"])
            llave["wifi"]=str(llave["wifi"])
            llave["bluetooth"]=float(llave["bluetooth"])
            llave["weight_kg"]=float(llave["weight_kg"])
            llave["warranty_months"]=int(llave["warranty_months"])
            llave["price"]=float(llave["price"])
            lt.add_last(catalog["computadores"],llave)
        menor=lt.get_element(catalog["computadores"],0)
        mayor=lt.get_element(catalog["computadores"],0)
        for i in range(1,lt.size(catalog["computadores"])):
            elemento=lt.get_element(catalog["computadores"],i)
            if elemento["price"]>=mayor["price"]:
                mayor=elemento
            if elemento["price"]<=menor["price"]:
                menor=elemento
                
        #primeros 5
        primeros=lt.new_list()
        tamaño=lt.size(catalog["computadores"])
        for i in range(5):
            elemento=lt.get_element(catalog["computadores"],i)
            info={"Modelo":elemento["model"],
                    "Marca":elemento["brand"],
                    "Año":elemento["release_year"],
                    "CPU":elemento["cpu_model"],
                    "GPU":elemento["gpu_model"],
                    "Precio":elemento["price"]}
                
            lt.add_last(primeros,info)
                
        ultimos=lt.new_list()
        for i in range(-1,-6,-1):
            elemento=lt.get_element(catalog["computadores"],i)
            info={"Modelo":elemento["model"],
                    "Marca":elemento["brand"],
                    "Año":elemento["release_year"],
                    "CPU":elemento["cpu_model"],
                    "GPU":elemento["gpu_model"],
                    "Precio":elemento["price"]}
            lt.add_last(ultimos,elemento)
    final=get_time()
    tiempo=final-incio
    return catalog, tiempo, tamaño, menor, mayor, primeros, ultimos
            
        
        

    # TODO: Realizar la carga de datos
    

# Funciones de consulta sobre el catálogo


def req_1(catalog, marca):
    """
    Retorna el resultado del requerimiento 1
    """
    # TODO: Modificar el requerimiento 1
    tiempo_inicio = get_time()
    cantidad, suma_precio, suma_ram, suma_vram, suma_cores, suma_anio = 0,0,0,0,0,0
    prom_anio, prom_cores, prom_precio, prom_ram, prom_vram = 0,0,0,0,0
    min_ram, min_vram, min_cores, min_anio = 9999,9999,9999,9999
    max_ram, max_vram, max_cores, max_anio = -1,-1,-1,-1
    computador_caro = None
    computador_barato = None
    tamanio = lt.size(catalog["computadores"])
    for i in range(tamanio):
        comp_act = lt.get_element(catalog["computadores"],i)
        if marca.lower() == comp_act["brand"].lower():
            cantidad+=1
            suma_precio+=comp_act["price"]
            suma_ram+=comp_act["ram_gb"]
            suma_vram+=comp_act["vram_gb"]
            suma_cores+=comp_act["cpu_cores"]
            suma_anio+=comp_act["release_year"]
            max_ram = max(max_ram, comp_act["ram_gb"])
            min_ram = min(min_ram, comp_act["ram_gb"])
            max_vram = max(max_vram, comp_act["vram_gb"])
            min_vram = min(min_vram, comp_act["vram_gb"])
            max_cores = max(max_cores, comp_act["cpu_cores"])
            min_cores = min(min_cores, comp_act["cpu_cores"])
            max_anio = max(max_anio, comp_act["release_year"])
            min_anio = min(min_anio, comp_act["release_year"])
            if computador_caro is None:
                computador_caro = comp_act
            else:
                if comp_act["price"]>computador_caro["price"]:
                    computador_caro = comp_act
                elif comp_act["price"] == computador_caro["price"]:
                    if comp_act["weight_kg"] < computador_caro["weight_kg"]:
                        computador_caro = comp_act
            if computador_barato is None:
                computador_barato = comp_act   
            else:
                if comp_act["price"]<computador_barato["price"]:
                    computador_barato = comp_act
                elif comp_act["price"] == computador_barato["price"]:
                    if comp_act["weight_kg"] < computador_barato["weight_kg"]:
                        computador_barato = comp_act
    tiempo_final = get_time()
    tiempo = delta_time(tiempo_inicio, tiempo_final)
    if cantidad == 0:
        return [["Mensaje", "No se encontraron computadores para la marca: " + marca],
                ["Tiempo ejecución (ms)", tiempo]]
    prom_precio = suma_precio/cantidad
    prom_ram = suma_ram/cantidad
    prom_vram = suma_vram/cantidad
    prom_cores= suma_cores/cantidad
    prom_anio = suma_anio/cantidad
        
    info = [["Tiempo ejecucion (ms):", tiempo], 
            ["Cantidad de Computadores: ", cantidad],
            ["Precio (Promedio, Min, Max):", f"${round(prom_precio,2)} / ${computador_barato['price']} / ${computador_caro['price']}"], 
            ["GB RAM (Promedio, Min, Max):", f"{round(prom_ram)}GB / {min_ram}GB / {max_ram}GB"],
            ["GB VRAM (Promedio, Min, Max):", f"{round(prom_vram)}GB / {min_vram}GB / {max_vram}GB"], 
            ["Nucleos (Promedio, Min, Max):", f"{round(prom_cores)} / {min_cores} / {max_cores}"],
            ["Anio (Promedio, Min, Max):", f"{round(prom_anio)} / {min_anio} / {max_anio}"],
            ["Computador mas caro: ", computador_caro["model"]],
            ["Precio mas alto: ", f"${computador_caro["price"]}"],
            ["Computador mas barato", computador_barato["model"]],
            ["Precio mas bajo: ", f"${computador_barato["price"]}"]]
    return info

def req_2(catalog,min,max):
    inicio=get_time()
    moderno=lt.get_element(catalog["computadores"],0)
    cumplen=0
    suma_ram=0
    suma_vram=0
    suma_precios=0
    filtrados=lt.new_list()
    n=lt.size(catalog["computadores"])
    for i in range(n):
        element=lt.get_element(catalog["computadores"],i)
        if element["price"] <= max and element["price"] >= min:
            cumplen+=1
            suma_vram+=element["vram_gb"]
            suma_precios+=element["price"]
            suma_ram+=element["ram_gb"]
            lt.add_last(filtrados,element)
        if element["release_year"] == moderno["release_year"]:
            if element["price"]>moderno["price"]:
                moderno=element
            else:
                pass  

def req_3(catalog):
    """
    Retorna el resultado del requerimiento 3
    """
    # TODO: Modificar el requerimiento 3
    pass



def req_4(catalog):
    """
    Retorna el resultado del requerimiento 4
    """
    # TODO: Modificar el requerimiento 4
    pass


def req_5(catalog):
    """
    Retorna el resultado del requerimiento 5
    """
    # TODO: Modificar el requerimiento 5
    pass

def req_6(catalog):
    """
    Retorna el resultado del requerimiento 6
    """
    # TODO: Modificar el requerimiento 6
    pass


# Funciones para medir tiempos de ejecucion

def get_time():
    """
    devuelve el instante tiempo de procesamiento en milisegundos
    """
    return float(time.perf_counter()*1000)


def delta_time(start, end):
    """
    devuelve la diferencia entre tiempos de procesamiento muestreados
    """
    elapsed = float(end - start)
    return elapsed
