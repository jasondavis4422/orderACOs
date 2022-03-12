atypes = []
data = []
def count(id_list, data):
    id_index = 0
    data_index = 0
    count = 0
    number_list = []
    id_length = len(id_list)
    data_length = len(data)
    while id_index < id_length:
        while data_index < data_length:
            if data[data_index] == id_list[id_index]:
                count += 1
            data_index += 1
        number_list.append(count)
        count = 0
        data_index = 0
        id_index += 1
    return number_list

def chopandconvert(strings):
    ints_chopped = []
    for string in strings:
        str = string [1:]
        int_chopped = int(str)
        ints_chopped.append(int_chopped)
    return ints_chopped
    
def sort (number_list, type_list):
    id_list = chopandconvert(type_list)
    end = len(number_list)
    number_index = 0
    highest_index = 0
    ordered = []
    stringordered = []
    while number_index < end:
        highest = 0
        if len (number_list) == 0:
            break
        for number in number_list:
            if number > highest:
                highest = number
        ordered.append(highest)
        number_index = number_list.index(highest)
        number_list.pop(number_index)
        idtype = id_list[number_index]
        stringordered.append("A" +str(idtype))
        id_list.pop(number_index)
    return stringordered

