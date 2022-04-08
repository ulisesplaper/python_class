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

# Abrir el archivo, guardar cada linea en una lista y cerrar el archivo

file = open("data/dna_sequences.txt")
sequences = file.readlines()
file.close()


# Crear un archivo vacio fasta

file = open("results/dna_sequences.fasta", "w")


# Recorrer cada uno de los elementos de la lista
# Eliminar caracteres que no son secuencia
# Anadir el caracter ">" y cambiar el tabulador por salto de linea
# Escribir cada secuencia en el archivo de destino

for sequence in sequences:
    id = '>' + sequence
    file.write(id.replace('-', '').upper().replace('\t', '\n'))


# Cerrar el archivo fasta

file.close()


# Imprimir informacion para el usuario

print('Archivo generado: /results/dna_sequences.fasta')
