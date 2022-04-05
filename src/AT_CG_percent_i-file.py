''' NAME
      AT_G_percent_i-file.py

VERSION
        1.0

AUTHOR
        Victor Ulises Plascencia Perez

DESCRIPTION
       Calcula el porcentaje de AT y GC de una secuencia de DNA

USAGE

        python AT_G_percent_i-file.py
         
ARGUMENTS
        ninguno

SEE ALSO

GitHub link
        https://github.com/ulisesplaper/python_class/blob/master/src/AT_CG_percent_i-file.py
       
'''

## Solicitar al usuario el archivo de datos
print("Ingrese la ruta y el nombre del archivo que contiene la secuencia de DNA")
file_name = input()

## Abrir y leer todo el contenido del archivo de datos y cerrarlo
my_file = open(file_name)
my_dna = my_file.read()
my_file.close()

# Eliminar caracteres que no son secuencia
my_dna = my_dna.rstrip("\n")

# Conteos de A, T, G, C
t_count = my_dna.count("T")
a_count = my_dna.count("A")
g_count = my_dna.count("G")
c_count = my_dna.count("C")

# Calcular el % de AT y GC 
total_count = len(my_dna)
at_content =round(((t_count + a_count) / total_count)*100)
gc_content =round(((g_count + c_count) / total_count)*100)

## Imprimir resultados.
print(f"La secuencia proporcionada es {my_dna}\n")
print(f"Porcentaje de AT es: {at_content}%\nPorcentaje de GC es: {gc_content}%\n")
