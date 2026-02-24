def new_list():
    newlist ={
        "elements": [],
        "size": 0,
    }
    return newlist

"""
corregir la forma en que se llaman las funciones
corregir los return 
corregir add firsr y last
añadir casos base
revisar el nombre de las funciones (posible causante de falla)
corregir funcion exchange
quitar los prints de las funciones
"""

def get_element(my_list, index):
    return my_list["elements"][index]

def is_present(my_list, element, comparation_function):
    
    size = my_list["size"]
    if size> 0:
        keyexist= False 
        for keypos in range (0, size):
            info= my_list["elements"][keypos]
            if comparation_function(element,info)== 0:
                keyexist=True
                break
        if keyexist:
            return keypos
    return -1

def add_first(lista, element):
    elementos = lista["elements"]
    elementos.insert(0, element)
    
    lista["size"] += 1
    
    return lista

def add_last(lista, element):
    
    lista["elements"].append(element)
    lista["size"] += 1
    
    return lista 
       
def size(lista):
    
    return lista["size"]

def first_element(lista):
    
    if lista["size"]>0:
        return lista["elements"][0]
    else:
        return None
    
def is_empty(lista):
    
    if lista["size"]==0:
        return True
    else:
        return False
    
def remove_first(lista):
    if lista["size"]>0:
        remove=lista["elements"][0]
        lista["elements"]=lista["elements"][1:]
        lista["size"]-= 1
        return remove

def remove_last(lista):
    if lista["size"]>0:
        remove= lista["elements"][-1]
        lista["elements"]= lista["elements"][:-1]
        lista["size"]-= 1
        return remove
    
def insert_element(lista, element,pos):
    lista["elements"].insert(pos,element)
    lista["size"]+= 1
    return lista

def delete_element(lista,pos):
    
    lista["elements"]=lista["elements"][:pos] + lista["elements"][pos+1:]
    
    lista["size"]-=1
    return lista

def change_info(lista,pos,new_info):
    lista["elements"][pos]= new_info
    return lista["elements"]

def exchange (lista,pos_1,pos_2):
    intercambio= lista["elements"][pos_1],lista["elements"][pos_2]= lista["elements"][pos_2],lista["elements"][pos_1]
    return intercambio

def sub_list(lista, pos_i, num_elements):
    result = {"size": 0, "elements": []}
    for i in range (pos_i, pos_i + num_elements):
        if i < lista["size"]:
            result["elements"].append(lista["elements"][i])
            result["size"] += 1
    return result

