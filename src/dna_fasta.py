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
# Declarar una excepcion para documentos vacios


class EmptyDocError(Exception):
    pass


# Intentar realizar las acciones
try:
    # Solicitar al usuario el archivo de datos
    print("Ingrese la ruta y el nombre del archivo que contiene la secuencia de DNA")
    my_file_name = input()

    # Abrir, leer  y cerrar el archivo de datos
    my_file = open(my_file_name)
    my_file_contents = my_file.read()
    my_file.close()

    # Eliminar caracteres que no son secuencia
    my_dna = my_file_contents.rstrip("\n")

    # Evualuar si la variable no esta vacia
    # Regresar el error correspondiente si lo esta
    if (len(my_dna) == 0):
        raise EmptyDocError("\nEl documento esta vacio\n")

    # Verificar que el texto contenga solo secuencia
    # Regresar el error correspondiente en caso de que no
    for base in my_dna:
        if base not in ["A", "G", "C", "T"]:
            raise ValueError(
                f"La secuencia contiene caracteres que no son bases\n")

    # Guardar secuencia en formato fastA en un archivo
    my_file = open("../results/dna.fasta", "w")
    my_file.write(f">Seq_name\n{my_dna}")
    my_file.close()

# Informar si no se encontro el archivo
except IOError:
    print("\nEl nombre y/o ruta del archivo es incorrecto o no existe\n")
# Informar si el contenido del archivo no es secuencia
except ValueError as ex:
    print("\nLa secuencia del archivo es invalida\n" + ex.args[0])
# Informar si el archivo no tiene contenido
except EmptyDocError as ex:
    print(ex.args[0])
