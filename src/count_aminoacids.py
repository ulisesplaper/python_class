''' NAME
      count_aminoacids.py

VERSION
        2.0

AUTHOR
        Victor Ulises Plascencia Perez

DESCRIPTION
       Calcula el porcentaje de un aminoacido dado en una secuencia proteica

USAGE

        count_aminoacids.py [-h] [-a AMINOACID_LIST] protein

ARGUMENTS
        positional arguments:
            protein               protein sequence

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
import string


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
parser.add_argument("protein", help='protein sequence')

# Leer los argumentos de la terminal
args = parser.parse_args()

# Definir la funcion que calcula el porcentaje de aminoacido
# Indicar los parametros que recibe la funcion


def get_aa_percentage(peptide_sequence, aminoacid_list):
    '''
    Returns the porcentaje of aminoacids list in a protein sequence 
        Parameters
            peptide_sequence (str): a protein sequence
            aminoacid_list (str): aminoacid list
        Returns:
            get_aa_percentage(float): porcentaje of a amionacids list of protein sequence


    '''
    peptide_sequence = peptide_sequence.upper()

    # Verificar que la secuencia proteica ingresada sea correcta
    # Regresar el error correspondiente cuando no sea correcta
    aminoacids = ['A', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'K',
                  'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'V', 'W', 'Y']
    for block in peptide_sequence:
        if block not in aminoacids:
            raise NotCorrectProteinError(
                'NotCorrectProteinError <A correct protein sequence\
 was not entered>')
    # Inicializar una variable para llevar la cuenta de las ocurrencias
    # de los aminoacidos de la lista
    # Recorrer la lista de aminoacidos
    # contar las ocurrencia en la secuencia proteica y almacenar el resultado
    # Si algun caracter no corresponde con un aminoacido, regresar el error.
    peptide_count = 0
    for aminoacid in aminoacid_list:
        aminoacid = aminoacid.upper()
        if aminoacid not in aminoacids:
            raise NotAminoacidFoundError(
                'NotAminoacidFoundError <A correct aminoacid was not entered>')
        peptide_count += peptide_sequence.count(aminoacid)

     # Calcular el porcentaje de la lista de aminoacidos y regresar el valor
    peptide_percent = round(peptide_count / len(peptide_sequence) * 100, 3)
    return peptide_percent


# Intentar realizar las acciones
try:

    # Informar al usuario el porcentaje de aminoacido en la secuencia proteica
    # que ingreso o, en su caso, la lista default
    print(
        f"El porcentaje de {args.aminoacid_list} en la secuencia dada es:\
\n {get_aa_percentage(args.protein, args.aminoacid_list)}")

# Informar si la letra ingresada no corresponde con un aminoacido
except NotAminoacidFoundError as ex:
    print('\n El aminoacido ingresado es incorrecto\n' + ex.args[0])

# Informar si la secuencia ingresada contiene letras que no son aminoacidos
except NotCorrectProteinError as ex:
    print('\n la secuencia proteica ingresada es incorrecta\n' + ex.args[0])
