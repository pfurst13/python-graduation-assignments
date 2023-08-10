ascii_list = []

with open("ascii.txt", "r") as ascii_table:
    for line in ascii_table:
        line = line.strip('ascii code')
        line = line.strip('\n')
        line = line.strip('\t')
        line = line.replace("\t", " ")
        act_line = line.split(" ")
        ascii_list.append(act_line[1])

# print(ascii_list)

idx = 0

while idx <= len(ascii_list):
     act_line = []
     counter = 0
     
     while counter <= len(ascii_list):
        if idx <= counter:
             act_line.append(ascii_list[counter - 1])
        
        counter += 1
     idx += 1
     final = "".join(act_line)
     print(final)
         

# vtable_list = []
    
# with open("Vtabla.dat", "r") as vtable:
#     for line in vtable:
#         line = line.rstrip('\n')
#         vtable_list.append(line)

# formated_table = []

# for i, line in enumerate(vtable_list):
#     nums = '0123456789'
#     act_line = list(line)
#     new_line = act_line.insert((len(line))-1,nums)

#     formated_table.append(new_line)

# print(formated_table)