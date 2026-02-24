import csv
import os
import time
from DataStructures.List import array_list as lt
from DataStructures.Queue import queue as q
from DataStructures.Stack import stack as st

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

def load_data(catalog, filename):
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
    pass

# Funciones de consulta sobre el catálogo


def req_1(catalog):
    """
    Retorna el resultado del requerimiento 1
    """
    # TODO: Modificar el requerimiento 1
    pass


def req_2(catalog,min,max):
    inicio=get_time()
    moderno=None
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
           
        if moderno == None or element["release_year"] >= moderno["release_year"]:
            moderno=element
            
        if element["release_year"] == moderno["release_year"] and element["price"]>moderno["price"]:
            moderno=element


    if cumplen > 0:
        promedio_ram=suma_ram/cumplen
        promedio_vram=suma_vram/cumplen
        promedio_precios=suma_precios/cumplen
    else:
        promedio_precios = promedio_ram = promedio_vram =0
        
    final= get_time
    tiempo=final-inicio
    
    return cumplen, promedio_ram, promedio_vram, promedio_precios, moderno, filtrados, tiempo
        
    
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
