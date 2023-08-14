# acii tábla tartalmazza a karakterek számozását. A chr() metodussal átkonvertálom a számot
# a megfelelő karakterre. Utána a slice() metodussal hozom létre a kódolandó eggyel eltólt táblát. 

ascii_list = ['á', 'Á', 'é', 'É', 'í','Í', 'ó', 'Ó', 'ö', 'Ö', 'ő', 'Ő',
              'ú', 'Ú', 'ű', 'Ű', 'ü', 'Ü']

for i in range(32, 127):
     
    ascii_list.append(chr(i))

with open("table_hu.txt", "w") as line: 

    for i in range(len(ascii_list)):
     
        final_str = "".join(ascii_list[i:] + ascii_list[:i])

        line.write(f"{final_str}\n")
