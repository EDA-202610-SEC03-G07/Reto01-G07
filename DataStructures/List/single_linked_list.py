def new_list():
    newlist = {
        "first": None,
        "last": None,
        "size" : 0,
    }
    
    return newlist

"""
falla remove first, remove last e insert_element
corregir rangos de la funcion insert
faltta restar 1 en la funcion de remove
"""

def get_element(my_list,pos):
    searchpos= 0
    node= my_list["first"]
    while searchpos< pos:
        node= node["next"]
        searchpos+= 1
    return node["info"]

def is_present(my_list, element, cmp_function ):
    is_in_array= False
    temp= my_list["first"]
    count= 0 
    while not is_in_array and temp != None:
        if cmp_function(element, temp["info"])== 0:
            is_in_array=True
        else:
            temp = temp["next"]
            count += 1
    if not is_in_array:
        count= -1
    return count 

def size(my_list):
    
     return my_list['size']
 
def add_first(my_list, element):
    new_node = {"info": element, "next": None}

    if my_list["size"] == 0:
        # Si la lista está vaci el nuevo nodo es el primero y el último
        my_list["first"] = new_node
        my_list["last"] = new_node
    else:
        # Si la lista NO está vacía el nuevo nodo apunta al primer nodo actual
        new_node["next"] = my_list["first"]
        # Y ahora se convierte en el nuevo "first"
        my_list["first"] = new_node

    my_list["size"] += 1

    return my_list

def add_last(my_list, element):
    new_node = {"info": element, "next": None}
    
    if my_list['size'] == 0:
        my_list['first'] = new_node
        my_list['last'] = new_node
    else:
        my_list['last']['next'] = new_node
        my_list['last'] = new_node
    
    my_list['size'] += 1
    return my_list

def first_element(my_list):
    if my_list["size"] == 0:
        return None
    return my_list['first']['info']

def size(my_list):
    
     return my_list['size']

def is_empty(my_list):
    if my_list["size"]==0:
        return True
    else:
        return False
    
def last_element(my_list):
    if my_list["size"]==0:
        return None
    else:
        return my_list["last"]

def delete_element(my_list,pos):
    if pos < 0 or pos >= my_list['size']:
        return None
    
    if pos == 0:
        my_list['first'] = my_list['first']['next']
        if my_list['size'] == 1:
            my_list['last'] = None
    else:
        current = my_list['first']
        i = 0
        while i < pos - 1:
            current = current['next']
            i += 1
        current['next'] = current['next']['next']
        if pos == my_list['size'] - 1:
            my_list['last'] = current
    
    my_list['size'] -= 1
    return my_list

def remove_first(my_list):
    info_primero_eliminado=my_list["first"]["info"]
    if my_list["size"]==0:
        return None
    elif my_list["size"]==1:
        my_list["first"]=None
        my_list["last"]=None
        
    else:
        primero=my_list["first"]
        my_list["first"]=primero["next"]
    my_list["size"]-=1
    return info_primero_eliminado

def remove_last(my_list):
    info_ultimo_eliminado=my_list["last"]["info"]
    if my_list["size"]==0:
        return None
    elif my_list["size"]==1:
        my_list["first"]=None
        my_list["last"]=None
    elif my_list["size"]==2:
        my_list["last"]=my_list["first"]
    else:
        current = my_list['first']
        while current['next'] != my_list['last']:
            current = current['next']
        current['next'] = None
        my_list['last'] = current
    
    my_list['size'] -= 1
    return info_ultimo_eliminado

def insert_element(my_list, pos, element):
    if pos < 0:
        return None

    if pos == 0:
        
        return add_first(my_list, element)

    if pos >= my_list['size']:
        return add_last(my_list, element)

    new_node = {"info": element, "next": None}
    current = my_list['first']
    i = 0

    while i < pos - 1:
        current = current['next']
        i += 1

    new_node['next'] = current['next']
    current['next'] = new_node
    my_list['size'] += 1

    return my_list
 
def change_info(my_list, pos, new_info):
    if pos < 0 or pos >= my_list['size']:
        return None
    
    current = my_list['first']
    i = 0
    while i < pos:
        current = current['next']
        i += 1
    
    current['info'] = new_info
    return my_list

    
def exchange(my_list, pos_1, pos_2):
    size = my_list["size"]

    if pos_1 < 0 or pos_2 < 0 or pos_1 >= size or pos_2 >= size:
        return None
    if pos_1 == pos_2:
        return my_list
    
    actual = my_list["first"]
    contador = 0
    nodo_1 = None
    nodo_2 = None

    while actual != None:
        if contador == pos_1:
            nodo_1 = actual
        if contador == pos_2:
            nodo_2 = actual
        actual = actual["next"]
        contador += 1

    aux = nodo_1["info"]
    nodo_1["info"] = nodo_2["info"]
    nodo_2["info"] = aux

    return my_list
    
    
    

def sub_list(my_list, pos, num_elements):
    if pos < 0 or pos >= size(my_list):
        return None
    
    sub = new_list()
    current = my_list['first']
    
    for i in range(pos):
        current = current['next']
    
    count = 0
    while current is not None and count < num_elements:
        add_last(sub, current["info"])
        current = current['next']
        count += 1
    
    return sub
        