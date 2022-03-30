''' NAME
      dna_fasta

VERSION
        1.0

AUTHOR
        Victor Ulises Plascencia Perez

DESCRIPTION
       Convierte una secuencia de DNA en formato raw a formato FastA

USAGE  
        dna_fasta.py 

ARGUMENTS
        ninguno

SEE ALSO
        ninguno

GitHub link
        https://github.com/ulisesplaper/python_class/blob/master/src/dna_fasta.py
       
'''
## Solicitar al usuario el archivo de datos
print("Ingrese la ruta y el nombre del archivo que contiene la secuencia de DNA")
my_file_name = input()

## Abrir, leer  y cerrar el archivo de datos
my_file = open(my_file_name)
my_file_contents = my_file.read()
my_file.close()

# Eliminar caracteres que no son secuencia
my_dna = my_file_contents.rstrip("\n")

# Guardar secuencia en formato fastA en un archivo
my_file = open("../results/dna.fasta","w")
my_file.write(f">Seq_name\n{my_dna}")
my_file.close()


