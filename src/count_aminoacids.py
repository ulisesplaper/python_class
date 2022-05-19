''' NAME
      count_aminoacids.py

VERSION
        1.0

AUTHOR
        Victor Ulises Plascencia Perez

DESCRIPTION
       Calcula el porcentaje de un aminoacido dado en una secuencia proteica

USAGE

        count_aminoacids.py [-h] aminoacid protein
         
ARGUMENTS
        positional arguments:
            aminoacid   aminoacid to count
            protein     protein sequence
        options:
            -h, --help  show this help message and exit
SEE ALSO

GitHub link
        https://github.com/ulisesplaper/python_class/blob/master/src/count_aminoacids.py
       
'''
# Importar librerias necesarias
import argparse
import string

# Declarar las excepciones para aminoacido y proteina incorrecta


class NotAminoacidFoundError(Exception):
    pass


class NotCorrectProteinError(Exception):
    pass


# Definir los argumentos posicionales
parser = argparse.ArgumentParser()
parser.add_argument('aminoacid', help='aminoacid to count')
parser.add_argument("protein", help='protein sequence')

# Leer los argumentos de la terminal
args = parser.parse_args()

# Definir la funcion que calcula el porcentaje de aminoacido
# Indicar los parametros que recibe la funcion


def get_aa_percentage(peptide_sequence, aminoacid):
    peptide_sequence = peptide_sequence.upper()
    aminoacid = aminoacid.upper()
    # Verificar que el aminoacido y la secuencia ingresada sean correctas
    # Regresar el error correspondiente cuando no sean correctas
    aminoacids = ['A', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'K',
                  'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'V', 'W', 'Y']
    if aminoacid not in aminoacids:
        raise NotAminoacidFoundError(
            'NotAminoacidFoundError <A correct aminoacid was not entered>')
    for block in peptide_sequence:
        if block not in aminoacids:
            raise NotCorrectProteinError(
                'NotCorrectProteinError <A correct protein sequence\
 was not entered>')
    # Contar las ocurrencias del aminoacido en la proteina
    # Contar el numero de aminoacidos de la proteina.
    # Calcular el porcentaje del aminoacido y regresar el valor
    peptide_count = peptide_sequence.count(aminoacid)
    peptide_percent = round(peptide_count / len(peptide_sequence) * 100, 3)
    return peptide_percent


# Intentar realizar las acciones
try:

    # Informar al usuario el porcentaje de aminoacido en la secuencia proteica
    print(
        f"El porcentaje de {args.aminoacid} en la secuencia dada es:\
\n {get_aa_percentage(args.protein, args.aminoacid)}")
# Informar si la letra ingresada no corresponde con un aminoacido
except NotAminoacidFoundError as ex:
    print('\n El aminoacido ingresado es incorrecto\n' + ex.args[0])
# Informar si la secuencia ingresada contiene letras que no son aminoacidos
except NotCorrectProteinError as ex:
    print('\n la secuencia proteica ingresada es incorrecta\n' + ex.args[0])
