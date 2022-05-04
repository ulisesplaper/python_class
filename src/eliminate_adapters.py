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
# Declarar una excepcion para documentos vacios


class EmptyDocError(Exception):
    pass


# Intentar realizar las siguientes acciones
try:

    # Abrir el archivo, guardar cada linea en una lista y cerrar el archivo

    file = open("../data/4_input_adapters.txt")
    seqs_adapters = file.readlines()
    file.close()

    # Determinar si la lista esta vacia y regresar el error si lo esta
    if len(seqs_adapters) == 0:
        raise EmptyDocError("\n El archivo input esta vacio\n")

    # Crear un archivo destino para almacenar las secuencias sin adaptadores
    file = open('../results/sequences_woadpters.txt', 'w')

    # Recorrer la lista y eliminar los primeros 14 elementos de cada string
    # Agregar cada secuencia al archivo destino
    for seq_adapter in seqs_adapters:
        sequence = seq_adapter[14:-1]
        file.write(f"{sequence}\n")

    # Cerrar el archivo destin
    file.close()

    # Imprimir informacion del archivo para el usuario
    print('Archivo generado: /results/sequences_woadpters.txt')

# Indicar al usuario cuando no se encuentre el archivo
except IOError:
    print("\nLa ruta y/o el nombre del archivo no se encuentran o no existen\n")
# Indicar al usuario cuando el archivo este vacio
except EmptyDocError as ex:
    print(ex.args[0])
