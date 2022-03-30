''' NAME
      dna_fasta

VERSION
        1.0

AUTHOR
        Victor Ulises Plascencia Perez

DESCRIPTION
       Convierte una archivo de texto plano con una secuencia de DNA en un archivo tipo fasta.

USAGE  

ARGUMENTS

SEE ALSO

GitHub link
       
'''
## Se le solicita al usuario la ruta y nombre del archivo
print("Ingrese la ruta y el nombre del archivo que contiene la secuencia de DNA")
my_file_name=input()
## Se abre el archivo y se lee
my_file=open(my_file_name)
my_file_contents = my_file.read()

## Se quita el caracter de salto de linea y se guarda la secuencia
## en una nueva variable.
my_dna = my_file_contents.rstrip("\n")

## Se abre (crea) un archivo llamado dna.fasta
my_file = open("../results/dna.fasta","w")
## Se escribe en el archivo el encabezado y la secuencia.
my_file.write(f">Seq_name {my_dna}")
## se cierra el archivo.
my_file.close()