import csv
from logging import info
from logging import info
import os
import time
from DataStructures.List import array_list as lt
from DataStructures.Queue import queue as q
from DataStructures.Stack import stack as st
from DataStructures.List import single_linked_list as sl
csv.field_size_limit(2147483647)

def maximo(actual, nuevo):
    if nuevo > actual:
        return nuevo
    return actual


def minimo(actual, nuevo):
    if nuevo < actual:
        return nuevo
    return actual



def new_logic():
    catalog= {
        'computadores':None}
        
    catalog['computadores'] = lt.new_list()
    
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
            max_ram = maximo(max_ram, comp_act["ram_gb"])
            min_ram = minimo(min_ram, comp_act["ram_gb"])
            max_vram = maximo(max_vram, comp_act["vram_gb"])
            min_vram = minimo(min_vram, comp_act["vram_gb"])
            max_cores = maximo(max_cores, comp_act["cpu_cores"])
            min_cores = minimo(min_cores, comp_act["cpu_cores"])
            max_anio = maximo(max_anio, comp_act["release_year"])
            min_anio = minimo(min_anio, comp_act["release_year"])
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
    
    if cantidad == 0:
        tiempo_final = get_time()
        tiempo = delta_time(tiempo_inicio, tiempo_final)
        return [["Mensaje", "No se encontraron computadores para la marca: " + marca],
                ["Tiempo ejecución (ms)", tiempo]]
    prom_precio = suma_precio/cantidad
    prom_ram = suma_ram/cantidad
    prom_vram = suma_vram/cantidad
    prom_cores= suma_cores/cantidad
    prom_anio = suma_anio/cantidad
    tiempo_final = get_time()
    tiempo = delta_time(tiempo_inicio, tiempo_final)
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
    menor_precio=None
    mayor_precio=None
    moderno=None
    cumplen=0
    suma_ram=0
    suma_vram=0
    suma_precios=0
    min = float(min)
    max = float(max)
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
            
            if moderno is None:
                moderno = element
            
            else:
                if element["release_year"] > moderno["release_year"]:
                    moderno=element
            
                elif element["release_year"] == moderno["release_year"] and element["price"] > moderno["price"]:
                    moderno=element
                
            if mayor_precio is None:
                mayor_precio=element
            else:
                if element["price"] > mayor_precio["price"]:
                    mayor_precio=element
                    
            if menor_precio is None:
                menor_precio=element
            else:
                if element["price"] < menor_precio["price"]:
                    menor_precio=element
    if cumplen == 0:
        final = get_time()
        tiempo = delta_time(inicio, final)

        return [
            ["Mensaje", f"No se encontraron computadores en el rango {min} - {max}"],
            ["Tiempo ejecución (ms)", tiempo]
        ]

    promedio_ram = suma_ram / cumplen
    promedio_vram = suma_vram / cumplen
    promedio_precios = suma_precios / cumplen

    final = get_time()
    tiempo = delta_time(inicio, final)

    info = [
        ["Tiempo ejecución (ms)", tiempo],
        ["Cantidad", cumplen],
        ["Precio promedio", round(promedio_precios, 2)],
        ["RAM promedio", round(promedio_ram)],
        ["VRAM promedio", round(promedio_vram)],
    ]

    if moderno:
        info.append(["Más moderno",
                 f"{moderno['model']} | {moderno['brand']} | "
                 f"{moderno['release_year']} | "
                 f"CPU: {moderno['cpu_brand']} | GPU: {moderno['gpu_brand']} | "
                 f"${moderno['price']}"])

    if mayor_precio:
        info.append(["Más caro",
                 f"{mayor_precio['model']} | {mayor_precio['brand']} | "
                 f"CPU: {mayor_precio['cpu_brand']} | GPU: {mayor_precio['gpu_brand']} | "
                 f"${mayor_precio['price']}"])

    if menor_precio:
        info.append(["Más barato",
                 f"{menor_precio['model']} | {menor_precio['brand']} | "
                 f"CPU: {menor_precio['cpu_brand']} | GPU: {menor_precio['gpu_brand']} | "
                 f"${menor_precio['price']}"])

    return info
                

def req_3(catalog, cpu_brand, cpu_tier):
    """
    Retorna el resultado del requerimiento 3
    """
    inicio = get_time()
    lista_nueva = lt.new_list()
    años_lista = lt.new_list()
    conteos_años = lt.new_list()
    gpus_lista = lt.new_list()
    conteos_gpus = lt.new_list()
    suma_precio = 0
    suma_ram = 0
    suma_vram = 0
    suma_hilos = 0
    contador = 0
    año_frecuente = 0
    max_frecuencia = 0
    gpu_frecuente = None
    max_frecuencia_gpu = 0
    año_actual = 0
    gpu_actual = None
    numero_computadores = 0
    prom_precio = 0
    prom_ram = 0
    prom_vram = 0
    prom_hilos = 0
    encontrado = False
    nuevo_conteo = 0

    tamaño = lt.size(catalog["computadores"])
    for i in range(tamaño):
        computador = lt.get_element(catalog["computadores"], i)
        if (computador["cpu_brand"].lower() == cpu_brand.lower() and
           computador["cpu_tier"] == int(cpu_tier)):
            lt.add_last(lista_nueva, computador)
            suma_precio += computador["price"]
            suma_ram += computador["ram_gb"]
            suma_vram += computador["vram_gb"]
            suma_hilos += computador["cpu_threads"]
            contador += 1

    

    if contador == 0:
        final = get_time()
        tiempo = delta_time(inicio, final)
        return [["Mensaje", "No se encontraron computadores para la marca: " + cpu_brand + " y el tier: " + cpu_tier],
                ["Tiempo ejecución (ms)", tiempo]]

    prom_precio = suma_precio / contador
    prom_ram = suma_ram / contador
    prom_vram = suma_vram / contador
    prom_hilos = suma_hilos / contador
    numero_computadores = lt.size(lista_nueva)

    for i in range(numero_computadores):
        computador = lt.get_element(lista_nueva, i)
        año_actual = computador["release_year"]
        encontrado = False
        for j in range(lt.size(años_lista)):
            if lt.get_element(años_lista, j) == año_actual:
                nuevo_conteo = lt.get_element(conteos_años, j) + 1
                lt.change_info(conteos_años, j, nuevo_conteo)
                if nuevo_conteo > max_frecuencia:
                    max_frecuencia = nuevo_conteo
                    año_frecuente = año_actual
                encontrado = True
                break
        if not encontrado:
            lt.add_last(años_lista, año_actual)
            lt.add_last(conteos_años, 1)
            if 1 > max_frecuencia:
                max_frecuencia = 1
                año_frecuente = año_actual

   
    for i in range(numero_computadores):
        computador = lt.get_element(lista_nueva, i)
        gpu_actual = computador["gpu_brand"]
        encontrado = False
        for j in range(lt.size(gpus_lista)):
            if lt.get_element(gpus_lista, j) == gpu_actual:
                nuevo_conteo = lt.get_element(conteos_gpus, j) + 1
                lt.change_info(conteos_gpus, j, nuevo_conteo)
                if nuevo_conteo > max_frecuencia_gpu:
                    max_frecuencia_gpu = nuevo_conteo
                    gpu_frecuente = gpu_actual
                encontrado = True
                break
        if not encontrado:
            lt.add_last(gpus_lista, gpu_actual)
            lt.add_last(conteos_gpus, 1)
            if 1 > max_frecuencia_gpu:
                max_frecuencia_gpu = 1
                gpu_frecuente = gpu_actual
    final = get_time()
    tiempo = delta_time(inicio, final)
    info = [
        ["Tiempo ejecución (ms)", round(tiempo, 2)],
        ["Computadores encontrados", contador],
        ["Precio promedio", round(prom_precio, 2)],
        ["RAM promedio (GB)", round(prom_ram, 2)],
        ["VRAM promedio (GB)", round(prom_vram, 2)],
        ["Hilos promedio CPU", round(prom_hilos, 2)],
        ["Año más frecuente", año_frecuente],
        ["GPU más frecuente", gpu_frecuente],
    ]
    return info

def req_4(catalog, cpu_brand, gpu_model):
    """
    Retorna el resultado del requerimiento 4
    """
    # TODO: Modificar el requerimiento 4
    tiempo_inicio = get_time()
    
    cantidad, suma_precio, suma_vram, suma_ram, suma_boost = 0,0,0,0,0
    prom_precio, prom_vram, prom_ram, prob_boost_cpu = 0,0,0,0
    mas_caro1 = None
    mas_caro2 = None
    lista_filtrada = filtrar_por_cpubrand_gpumodel(catalog,gpu_model, cpu_brand)
    actual = lista_filtrada["first"]
    cantidad = sl.size(lista_filtrada)
    if cantidad == 0:
        tiempo_final = get_time()
        tiempo = delta_time(tiempo_inicio, tiempo_final)
        return [["Mensaje", "No se encontraron computadores que cumplan el filtro de cpu: "+ cpu_brand+" y gpu: " + gpu_model],
                ["Tiempo ejecución (ms)", tiempo]]
    while actual != None:
        comp_act = actual["info"]
        suma_precio += comp_act["price"]
        suma_vram += comp_act["vram_gb"]
        suma_ram += comp_act["ram_gb"]
        suma_boost += comp_act["cpu_boost_ghz"]
        
        if mas_caro1 is None:
            mas_caro1 = comp_act

        elif (comp_act["price"] > mas_caro1["price"] or
              (comp_act["price"] == mas_caro1["price"] and
              comp_act["weight_kg"] < mas_caro1["weight_kg"])):

            mas_caro2 = mas_caro1
            mas_caro1 = comp_act

        elif mas_caro2 is None:

            mas_caro2 = comp_act

        elif (comp_act["price"] > mas_caro2["price"] or
              (comp_act["price"] == mas_caro2["price"] and
              comp_act["weight_kg"] < mas_caro2["weight_kg"])):
            mas_caro2 = comp_act

        actual = actual["next"]
    prom_precio = suma_precio/cantidad
    prom_vram = suma_vram/cantidad
    prom_ram = suma_ram/cantidad
    prob_boost_cpu = suma_boost/cantidad
    tiempo_final = get_time()
    tiempo = delta_time(tiempo_inicio, tiempo_final)
    
    info = [
        ["Tiempo ejecución (ms)", tiempo],
        ["Cantidad", cantidad],
        ["Precio promedio", round(prom_precio, 2)],
        ["VRAM promedio (GB)", round(prom_vram)],
        ["RAM promedio (GB)", round(prom_ram)],
        ["Boost promedio (GHz)", round(prob_boost_cpu, 2)],
    ]

    if mas_caro1:
        info.append(["Computadora mas costosa 1:",
                     f"{mas_caro1['model']} | {mas_caro1['brand']} | "
                     f"{mas_caro1['release_year']} | "
                     f"{mas_caro1['cpu_model']} | "
                     f"${mas_caro1['price']}"])

    if mas_caro2:
        info.append(["Computadora mas costosa 2:",
                     f"{mas_caro2['model']} | {mas_caro2['brand']} | "
                     f"{mas_caro2['release_year']} | "
                     f"{mas_caro2['cpu_model']} | "
                     f"${mas_caro2['price']}"])

    return info


def req_5(catalog,min,max,resolucion,solicitud):
    """
    Retorna el resultado del requerimiento 5
    """
    # TODO: Modificar el requerimiento 5
    filtrados=lt.new_list()
    inicio=get_time()
    barato=None
    caro=None
    cumplieron=0
    precio_suma=0
    resolucion_suma=0
    gpu_tier_suma=0
    min = int(min)
    max = int(max)
     
    n=lt.size(catalog["computadores"])
    
    for i in range(n):
        element=lt.get_element(catalog["computadores"],i)
        
        if min < element["release_year"] < max and resolucion == element["resolution"]:
            cumplieron+=1
            precio_suma+=element["price"]
            resolucion_suma+=element["display_size_in"]
            gpu_tier_suma+=element["gpu_tier"]
            lt.add_last(filtrados,element)

            if barato is None:
                barato = element
            else:
                if element["price"] < barato["price"]:
                    barato=element
                elif element["price"] == barato["price"]:
                    if element["weight_kg"] < barato["weight_kg"]:
                        barato=element
                    
            if caro is None:
                caro=element
            else:
                if element["price"] > caro["price"]:
                    caro=element
                elif element["price"] == caro["price"]:
                    if element["weight_kg"] < caro["weight_kg"]:
                        caro=element
            
    if cumplieron > 0:
        precio_promedio=precio_suma/cumplieron
        promedio_resolucion=resolucion_suma/cumplieron
        promedio_gpu_tier=gpu_tier_suma/cumplieron
    else:
        
        promedio_gpu_tier = promedio_resolucion = precio_promedio =0    
        
    if barato is not None:   
        barato_info={"brand":caro["brand"],"model":caro["model"],
                  "price":barato["price"],
                  "display_size_in":barato["display_size_in"],
                  "gpu_tier":barato["gpu_tier"],
                  "display_type":barato["display_type"],
                  "release_year":barato["release_year"],
                  "weight_kg":barato["weight_kg"]}
    else: 
        barato_info=None    
        
    if caro is not None:   
        caro_info={"brand":caro["brand"],"model":caro["model"],
                  "price":caro["price"],
                  "display_size_in":caro["display_size_in"],
                  "gpu_tier":caro["gpu_tier"],
                  "display_type":caro["display_type"],
                  "release_year":caro["release_year"],
                  "weight_kg":caro["weight_kg"]}
    else: 
        caro_info=None   
    info = None
    
    if solicitud.lower() == "barato":
        info=barato_info
        
    if solicitud.lower() =="caro":
        info=caro_info

    final=get_time()
    tiempo=final-inicio
    resultado = [
        ["Tiempo ejecución (ms)", tiempo],
        ["Filtro de selección", solicitud.upper()],
        ["Cantidad", cumplieron],
        ["Precio promedio", round(precio_promedio, 2)],
        ["GPU tier promedio", round(promedio_gpu_tier, 2)],
        ["Tamaño pantalla promedio", round(promedio_resolucion, 2)],
    ]

    if info:
        resultado.append([
            f"Más {solicitud.lower()}:",
            f"{info['brand']} | "
            f"{info['model']} | "
            f"${info['price']} | "
            f"{info['display_size_in']} in | "
            f"GPU Tier {info['gpu_tier']} | "
            f"Tipo {info['display_type']} | "
            f"Año {info['release_year']} | "
            f"Peso {info['weight_kg']} kg"
        ])

    return resultado


def req_6(catalog, año_inicial, año_final):
    """
    Retorna el resultado del requerimiento 6
    """
    tiempo_inicio = get_time()
    lista_filtrada = sl.new_list()
    os_unicos = sl.new_list()
    resultados_por_os = sl.new_list()
    cantidad_total = 0
    os_mas_usado = None
    os_mayor_recaudo = None
    max_cantidad = 0
    max_recaudo = 0
    max_cantidad_recaudo = 0
    cantidad_os = 0
    suma_precio = 0
    suma_peso = 0
    mas_caro = None
    mas_barato = None
    precio = 0
    peso = 0
    info_os = None
    encontrado = False
    os_actual = None
    
    for i in range(lt.size(catalog["computadores"])):
        comp = lt.get_element(catalog["computadores"], i)
        if año_inicial <= comp["release_year"] <= año_final:
            sl.add_last(lista_filtrada, comp)

    cantidad_total = sl.size(lista_filtrada)

    if cantidad_total == 0:
        tiempo_final = get_time()
        tiempo = delta_time(tiempo_inicio, tiempo_final)
        return [["Mensaje", f"No se encontraron computadores entre {año_inicial} y {año_final}"],
                ["Tiempo ejecución (ms)", tiempo]]

    actual = lista_filtrada["first"]
    while actual is not None:
        os_actual = actual["info"]["os"]
        encontrado = False
        nodo_os = os_unicos["first"]
        while nodo_os is not None:
            if nodo_os["info"] == os_actual:
                encontrado = True
                break
            nodo_os = nodo_os["next"]
        if not encontrado:
            sl.add_last(os_unicos, os_actual)
        actual = actual["next"]

 
    nodo_os = os_unicos["first"]
    while nodo_os is not None:
        os_actual = nodo_os["info"]
        cantidad_os = 0
        suma_precio = 0
        suma_peso = 0
        mas_caro = None
        mas_barato = None

        actual = lista_filtrada["first"]
        while actual is not None:
            comp = actual["info"]
            if comp["os"] == os_actual:
                cantidad_os += 1
                precio = comp["price"]
                peso = comp["weight_kg"]
                suma_precio += precio
                suma_peso += peso

                if mas_caro is None or precio > mas_caro["price"] or \
                   (precio == mas_caro["price"] and peso < mas_caro["weight_kg"]):
                    mas_caro = comp
                if mas_barato is None or precio < mas_barato["price"] or \
                   (precio == mas_barato["price"] and peso < mas_barato["weight_kg"]):
                    mas_barato = comp
            actual = actual["next"]

        if cantidad_os > max_cantidad:
            max_cantidad = cantidad_os
            os_mas_usado = os_actual
        if suma_precio > max_recaudo:
            max_recaudo = suma_precio
            os_mayor_recaudo = os_actual
            max_cantidad_recaudo = cantidad_os

        info_os = {
            "os": os_actual,
            "cantidad": cantidad_os,
            "recaudo": round(suma_precio, 2),
            "precio_promedio": round(suma_precio / cantidad_os, 2),
            "peso_promedio": round(suma_peso / cantidad_os, 2),
            "mas_caro": mas_caro,
            "mas_barato": mas_barato
        }
        sl.add_last(resultados_por_os, info_os)
        nodo_os = nodo_os["next"]

    tiempo_final = get_time()
    tiempo = delta_time(tiempo_inicio, tiempo_final)

    info = [
        ["Tiempo ejecución (ms)", round(tiempo, 2)],
        ["Total computadores en rango", cantidad_total],
        ["OS más usado", os_mas_usado],
        ["  Cantidad de registros", max_cantidad],
        ["  Recaudo total", round(max_recaudo, 2)],
        ["OS mayor recaudo", os_mayor_recaudo],
        ["  Cantidad de registros", max_cantidad_recaudo],
        ["  Recaudo total", round(max_recaudo, 2)],
    ]

    nodo = resultados_por_os["first"]
    while nodo is not None:
        datos = nodo["info"]
        info.append([f"--- OS: {datos['os']} ---", ""])
        info.append(["  Precio promedio", datos["precio_promedio"]])
        info.append(["  Peso promedio (kg)", datos["peso_promedio"]])
        if datos["mas_caro"]:
            c = datos["mas_caro"]
            info.append(["  Más costoso",
                         f"{c['model']} | {c['brand']} | {c['release_year']} | "
                         f"{c['cpu_model']} | {c['gpu_model']} | ${c['price']}"])
        if datos["mas_barato"]:
            b = datos["mas_barato"]
            info.append(["  Más barato",
                         f"{b['model']} | {b['brand']} | {b['release_year']} | "
                         f"{b['cpu_model']} | {b['gpu_model']} | ${b['price']}"])
        nodo = nodo["next"]

    return info
    
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


def filtrar_por_cpubrand_gpumodel(lista, criterio1, criterio2):
    lista_filtrada = sl.new_list()
    tamanio = lt.size(lista["computadores"])
    
    for i in range(tamanio):
        comp_act = lt.get_element(lista["computadores"], i)
        if (comp_act['gpu_model'].lower() == criterio1 and
        comp_act["cpu_brand"].lower() == criterio2.lower()):
            sl.add_last(lista_filtrada, comp_act)
    return lista_filtrada