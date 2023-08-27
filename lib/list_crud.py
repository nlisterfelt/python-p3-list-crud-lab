def create_an_empty_list():
    return []

def create_a_list():
    return [1,2,3,4]

def add_element_to_end_of_list(l, element):
    list=l
    list.append(element)
    return list

def add_element_to_start_of_list(l, element):
    list=l
    list.insert(element,0)
    return l

def remove_element_from_end_of_list(l):
    list=l
    list.pop()
    return list

def remove_element_from_start_of_list(l):
    list=l
    list.pop(0)
    return list

def retrieve_first_element_from_list(l):
    return l[0]

def retrieve_element_from_index(l, index):
    return l[index]

def retrieve_last_element_from_list(l):
    return l[-1]
