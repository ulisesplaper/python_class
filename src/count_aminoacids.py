''' NAME
      count_aminoacids.py

VERSION
        3.0

AUTHOR
        Victor Ulises Plascencia Perez

DESCRIPTION
       Calcula el porcentaje de un aminoacido dado en una secuencia proteica
       obtenida de un archivo fasta

USAGE

        count_aminoacids.py [-h] [-a AMINOACID_LIST] path

ARGUMENTS
        positional arguments:
            path                  path of the fasta protein file

        options:
          -h, --help            show this help message and exit
          -a AMINOACID_LIST, --aminoacid_list AMINOACID_LIST
                aminoacid list without comas, spaces, or special characters
SEE ALSO

GitHub link
        https://github.com/ulisesplaper/python_class/blob/master/src/count_aminoacids.py

'''
# Importar librerias necesarias
import argparse
import protein_tools as pt
import re
import fasta_tools as ft


# Declarar las excepciones para aminoacido y proteina incorrecta


class NotAminoacidFoundError(Exception):
    pass


class NotCorrectProteinError(Exception):
    pass


# Definir los argumentos posicionales y opcionales
# Si el usuario no indica la lista de aminoacidos, indicar una por default
parser = argparse.ArgumentParser(
    description="Determine the aminoacids listed percentaje\
 of a protein sequence")
parser.add_argument('-a', '--aminoacid_list',
                    type=list, help='aminoacid list without comas, \
spaces, or special characters', required=False, default='ailmfwyv')
parser.add_argument(
    "path", help='path of the fasta protein file', metavar='path', type=str)

# Leer los argumentos de la terminal
args = parser.parse_args()


# Intentar realizar las acciones
try:
    # Obter la secuencia del archivo fasta
    peptide_sequence = ft.get_sequence(args.path)
    peptide_sequence = peptide_sequence.upper()

    # Verificar que la secuencia proteica ingresada sea correcta
    # Regresar el error correspondiente cuando no sea
    if re.search("[^ACDEFGHIKLMNPQRSTVWY]", peptide_sequence):
        raise NotCorrectProteinError(
            'NotCorrectProteinError <A correct protein sequence\
 was not entered>')

    # Convertir la lista de aminoacidos a string (para emplear regexp)
    # Si algun caracter no corresponde con un aminoacido, regresar el error.

    aminoacid_list = "".join(args.aminoacid_list)
    aminoacid_list = aminoacid_list.upper()
    if re.search("[^ACDEFGHIKLMNPQRSTVWY]", aminoacid_list):
        raise NotAminoacidFoundError(
            'NotAminoacidFoundError <A correct aminoacid was not entered>')

    # Calcular e informar al usuario el porcentaje de aminoacido
    # en la secuencia proteica que ingreso o, en su caso, la lista default
    print(
        f"El porcentaje de {args.aminoacid_list} en la secuencia dada es:\
\n{pt.get_aa_percentage(peptide_sequence, aminoacid_list)}")

 # Informarle al usuario el numero de peptidos generados
 # tras el tratamiento con tripsina
    print(
        f"El tratamiento con tripsina producira\
 {pt.tripsin_treatment(peptide_sequence)} peptidos\n")


# Informar si la letra ingresada no corresponde con un aminoacido
except NotAminoacidFoundError as ex:
    print('\n El aminoacido ingresado es incorrecto\n' + ex.args[0])

# Informar si la secuencia ingresada contiene letras que no son aminoacidos
except NotCorrectProteinError as ex:
    print('\n la secuencia proteica ingresada es incorrecta\n' + ex.args[0])

# Informar si el path del archivo es incorrecto
except FileNotFoundError:
    print('\n El nombre o ruta del archivo son incorrectos\n')
