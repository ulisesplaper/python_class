''' NAME
        fasta_converter
VERSION
        1.0
AUTHOR
        Victor Ulises Plascencia Perez
DESCRIPTION
    Convierte un archivo tabular de secuencias en un archivo fasta
USAGE
    py fasta_converter.py
ARGUMENTS
    none
SEE ALSO
    none
GitHub link
    https://github.com/ulisesplaper/python_class/blob/master/src/fasta_converter.py     
'''

# Declarar una excepcion para documentos vacios


class EmptyDocError(Exception):
    pass


# Intentar realizar las siguientes acciones
try:

    # Abrir el archivo, guardar cada linea en una lista y cerrar el archivo

    file = open("../data/dna_sequences.txt")
    sequences = file.readlines()
    file.close()

    # Determinar si la lista esta vacia y regresar el error si lo esta
    if len(sequences) == 0:
        raise EmptyDocError("\n El archivo input esta vacio\n")

    # Crear un archivo vacio fasta

    file = open("../results/dna_sequences.fasta", "w")

    # Recorrer cada uno de los elementos de la lista
    # Eliminar caracteres que no son secuencia
    # Anadir el caracter ">" y cambiar el tabulador por salto de linea
    # Escribir cada secuencia en el archivo de destino

    for sequence in sequences:
        id = '>' + sequence.split("\t")[0] + "\n" + sequence.split("\t")[1]
        file.write(id.replace('-', '').upper())

    # Cerrar el archivo fasta
    file.close()

    # Imprimir informacion para el usuario
    print('Archivo generado: /results/dna_sequences.fasta')

# Indicar al usuario cuando no se encuentre el path del archivo
except IOError:
    print("\nEl archivo y/o ruta son incorrectos o no existen\n")
# Indicar al usuario cuando el archivo este vacio
except EmptyDocError as ex:
    print(ex.args[0])
