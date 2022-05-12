''' NAME
      at_cg_percent_ifile.py

VERSION
        3.0

AUTHOR
        Victor Ulises Plascencia Perez

DESCRIPTION
       Calcula el porcentaje de AT y GC de una secuencia de DNA

USAGE

        at_cg_percent_ifile.py
         
ARGUMENTS
        -h, --help            show this help message and exit
        -i path/to/file, --input path/to/file
                        File with gene sequences
        -o OUTPUT, --output OUTPUT
                        Path for the output file
        -r ROUND, --round ROUND
                        Number of digits to round
SEE ALSO

GitHub link
        https://github.com/ulisesplaper/python_class/blob/master/src/AT_CG_percent_i-file.py
       
'''
# Importar la libreria argparse
import argparse

# Intentar realizar las acciones
try:
    # Definir los argumentos opcionales y posicionales del programa
    arg_parse = argparse.ArgumentParser(description="Determine the AT content")
    arg_parse.add_argument("-i", "--input",
                           metavar="path/to/file",
                           help="File with gene sequences",
                           required=True)
    arg_parse.add_argument("-o", "--output",
                           help="Path for the output file",
                           required=False)
    arg_parse.add_argument("-r", "--round",
                           help="Number of digits to round",
                           type=int,
                           required=False)

    # Leer los argumentos desde la terminal
    args = arg_parse.parse_args()

    # Abrir y leer todo el contenido del archivo de datos y cerrarlo
    with open(args.input, "r") as seq_file:
        my_dna = seq_file.read()

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
    # Si el usuario especifico el redondeo, llevarlo a cabo
    if args.round:
        at_content = round(
            ((t_count + a_count) / total_count) * 100, args.round)
        gc_content = round(
            ((g_count + c_count) / total_count) * 100, args.round)
    # Si no se especifico, redondear a 2 cifras decimales
    else:
        at_content = round(((t_count + a_count) / total_count) * 100, 2)
        gc_content = round(((g_count + c_count) / total_count) * 100, 2)

    # Generar el output del programa
    # Si el usuario indico el path de un archivo, escribir el output en este
    if args.output:
        file = open(f"{args.output}", "w")
        file.write(f"El contenido de AT es {at_content}\n\
El contenido de GC es: {gc_content}")
        file.close()
        print(f"El archivo {args.output} ha sido generado exitosamente\n")
    # Si no se indico, imprimir el output a pantalla
    else:
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
