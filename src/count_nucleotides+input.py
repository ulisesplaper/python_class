''' 
Name
        count_nucleotides+input
      
VERSION
        1.0

AUTHOR
        Victor Ulises Plascencia Perez

DESCRIPTION
       Este script toma una secuencia de DNA dada por el usuario y calcula su longitud y la cantidad de cada tipo de nucleotidos
       que contiene.

USAGE

ARGUMENTS

SEE ALSO

GitHub link
       https://github.com/ulisesplaper/python_class/blob/master/src/count_nucleotides%2Binput.py
'''

## Se solicita la secuencia y se almacena en una variable
print("Introduzca la secuencia de DNA")
dna=input()

# Se calcula e impre la longitud de la secuencia.
print(f'La cantidad de nucleotidos que contiene la secuencia es:\n{len(dna)}')

# Se calcula e imprime la cantidad de cada tipo de nucleotido de la 
# la secuencia.
print(f"A = {dna.count('A')}\tT = {dna.count('T')}\tG = {dna.count('G')}\tC = {dna.count('C')}")
