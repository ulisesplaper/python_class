''' NAME
        eliminate_adapters
    
VERSION
        1.0

AUTHOR
        Victor Ulises Plascencia Perez

DESCRIPTION
    Elimina los primeros 14 nucleotidos (adapatadores) de secuencias de DNA
       

USAGE
    py eliminate_adapters.py
         
ARGUMENTS
    none
    
SEE ALSO
    none

GitHub link
    https://github.com/ulisesplaper/python_class/blob/master/src/eliminate_adapters.py
       
'''

# Abrir el archivo, guardar cada linea en una lista y cerrar el archivo

file = open("docs/4_input_adapters.txt")
seqs_adapters = file.readlines()
file.close()


# Crear un archivo destino para almacenar las secuencias sin adaptadores

file = open('results/sequences_woadpters.txt', 'w')


# Recorrer la lista y eliminar los primeros 14 elementos de cada string
# Agregar cada secuencia al archivo destino

for seq_adapter in seqs_adapters:
    file.write(f"{seq_adapter[14:-1]}\n")


# Cerrar el archivo destino

file.close()


# Imprimir informacion del archivo para el usuario

print('Archivo generado: /results/sequences_woadpters.txt')
