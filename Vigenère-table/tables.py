def read_tabels(table):
    
    vtable_list = []
    
    with open(table, "r") as vtable:
        for line in vtable:
            line = line.rstrip('\n')
            vtable_list.append(line)
    
    return vtable_list