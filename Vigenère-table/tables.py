def read_tabels(table):
    
    vtable_list = []
    
    with open(table, "r") as vtable:
        for line in vtable:
            line = line.rstrip('\n')
            vtable_list.append(line)
    
    return vtable_list

def default_table():
    ascii_list = ['á', 'Á', 'é', 'É', 'í','Í', 'ó', 'Ó', 'ö', 'Ö', 'ő',
                   'Ő','ú', 'Ú', 'ű', 'Ű', 'ü', 'Ü']
    
    for i in range(32, 127):
        ascii_list.append(chr(i))
    
    vtable_list = []
    
    for i in range(len(ascii_list)):
        final_str = "".join(ascii_list[i:] + ascii_list[:i])

        vtable_list.append(final_str)
    
    return vtable_list
