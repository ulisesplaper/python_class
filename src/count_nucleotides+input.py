''' 
Name
        count_nucleotides_input.py
      
VERSION
        1.0

AUTHOR
        Victor Ulises Plascencia Perez

DESCRIPTION
       Calcula la frecuencia de cada nucleotido de una secuencia de ADN

USAGE
        count_nucleotides_input.py

ARGUMENTS
        ninguno

SEE ALSO
        ninguno

GitHub link
       https://github.com/ulisesplaper/python_class/blob/master/src/count_nucleotides%2Binput.py
'''

## Solicitar al usuario la secuencia de DNA
print("Introduzca la secuencia de DNA")
dna = input().upper()

# Calcular e imprimir la longitud de la secuencia.
print(f'La cantidad de nucleotidos que contiene la secuencia es:\n{len(dna)}')

# Contar los nucleotidos
total_a = dna.count('A')
total_t = dna.count('T')
total_g = dna.count('G')
total_c = dna.count('C')

# Imprimir resultados
print(f"A = {total_a}\tT = {total_t}\tG = {total_g}\tC = {total_c}")
