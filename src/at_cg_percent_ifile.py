''' NAME
      at_cg_percent_ifile.py

VERSION
        2.0

AUTHOR
        Victor Ulises Plascencia Perez

DESCRIPTION
       Calcula el porcentaje de AT y GC de una secuencia de DNA

USAGE

        at_cg_percent_ifile.py
         
ARGUMENTS
        ninguno

SEE ALSO

GitHub link
        https://github.com/ulisesplaper/python_class/blob/master/src/AT_CG_percent_i-file.py
       
'''
# Intentar realizar las acciones
try:
    # Solicitar al usuario el archivo de datos
    print("Ingrese la ruta y el nombre del archivo que contiene la secuencia de DNA")
    file_name = input()

    # Abrir y leer todo el contenido del archivo de datos y cerrarlo
    my_file = open(file_name)
    my_dna = my_file.read()
    my_file.close()

    # Eliminar caracteres que no son secuencia
    my_dna = my_dna.rstrip("\n")

    # Verificar que el texto contenga solo secuencia
    # Regresar el error correspondiente en caso de que no
    for base in my_dna:
        if base not in ["A", "G", "C", "T"]:
            raise ValueError(
                f"La secuencia contiene caracteres que no son bases")

    # Conteos de A, T, G, C
    t_count = my_dna.count("T")
    a_count = my_dna.count("A")
    g_count = my_dna.count("G")
    c_count = my_dna.count("C")

    # Calcular el % de AT y GC
    total_count = len(my_dna)
    at_content = round(((t_count + a_count) / total_count) * 100)
    gc_content = round(((g_count + c_count) / total_count) * 100)

    # Imprimir resultados.
    print(f"La secuencia proporcionada es {my_dna}\n")
    print(
        f"Porcentaje de AT es: {at_content}%\nPorcentaje de GC es: {gc_content}%\n")

# Informar si no se encontro el archivo
except IOError:
    print("El nombre y/o ruta del archivo es incorrecto o no existe")
# Informar si el contenido del archivo no es secuencia
except ValueError as ex:
    print("La secuencia del archivo es invalida\n" + ex.args[0])
# Informar si el archivo no tiene contenido
except ZeroDivisionError:
    print("\nEl archivo introducido esta vacio\n")
