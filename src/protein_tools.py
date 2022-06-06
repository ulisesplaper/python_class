
''' NAME
        protein_tools.py
VERSION
        1.0
AUTHOR
        Victor Ulises Plascencia Perez
DESCRIPTION
    Este modulo contiene dos funciones que:
    1. Calculan el porcentaje de una lista de aminoacidos en una secuencia
    proteica.
    2. Determinan el numero de peptidos producidos tras el tratamiento de la
    secuencia proteica con tripsina.
    
USAGE
    import protein_tools
    
ARGUMENTS
    none
SEE ALSO
    none
GitHub link
        https://github.com/ulisesplaper/python_class/blob/master/src/protein_tools.py
'''
# Importar la libreria para usar regexp
import re

# Funcion porcentaje de aminoacidos


def get_aa_percentage(peptide_sequence, aminoacid_list):
    '''
    Returns the porcentage of aminoacids list in a protein sequence 
        Parameters
            peptide_sequence (str): a protein sequence
            aminoacid_list (str): aminoacid list
        Returns:
            peptide_percent(float): percentage of a amionacids list of protein sequence


    '''

    # Inicializar una variable para llevar la cuenta de las ocurrencias
    # de los aminoacidos de la lista
    # Recorrer la lista de aminoacidos
    # contar las ocurrencia en la secuencia proteica y almacenar el resultado
    peptide_count = 0
    for aminoacid in aminoacid_list:
        peptide_count += peptide_sequence.count(aminoacid)

     # Calcular el porcentaje de la lista de aminoacidos y regresar el valor
    peptide_percent = round(peptide_count / len(peptide_sequence) * 100, 3)
    return peptide_percent


# Funcion tripsin treatment
def tripsin_treatment(peptide_sequence):
    '''
    Returns the number of peptides generated after trypsin treatment
    Parameters
            peptide_sequence (str): a protein sequence
        Returns:
            peptides_generated(int): number of peptides generated
    '''

    # Determinar el numero de fragmentos en el peptido
    # Tripsina corta en Arginina y Lisina

    cleavege_sites = len(re.findall(
        "[rk]", peptide_sequence, re.IGNORECASE)) + 1

    # Tripsina solo corta en el lado carboxilo (aa al final no se cortan)
    # Descartar aminoacidos R y L al final de la cadena
    if re.search("r|k$", peptide_sequence):
        cleavege_sites -= 1
    # Regresar el numero de fragmentos
    return cleavege_sites
