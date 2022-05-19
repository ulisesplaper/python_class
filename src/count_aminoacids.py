''' NAME
      count_aminoacids.py

VERSION
        1.0

AUTHOR
        Victor Ulises Plascencia Perez

DESCRIPTION
       Calcula el porcentaje de un aminoacido dado en una secuencia proteica

USAGE

        count_aminoacids.py
         
ARGUMENTS
        
SEE ALSO

GitHub link
        https://github.com/ulisesplaper/python_class/blob/master/src/count_aminoacids.py
       
'''
# Definir la funcion que calcula el porcentaje de aminoacido
# Indicar los parametros que recibe la funcion


def get_aa_percentage(peptide_sequence, aminoacid):
    # Contar las ocurrencias del aminoacido en la proteina
    # Contar el numero de aminoacidos de la proteina.
    # Calcular el porcentaje del aminoacido y regresar el valor
    peptide_sequence = peptide_sequence.upper()
    aminoacid = aminoacid.upper()
    peptide_count = peptide_sequence.count(aminoacid)
    peptide_percent = peptide_count / len(peptide_sequence) * 100
    return peptide_percent

# Evaluar que la funcion regrese valores esperados
