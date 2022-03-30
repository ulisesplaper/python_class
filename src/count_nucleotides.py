''' NAME
        Count_nucleotides

VERSION
        1.0

AUTHOR
        Victor Ulises Plascencia Perez

DESCRIPTION
        Contador de nucleotidos en una secuencia dada

USAGE
        ramdom motif [OPTIONS] 

ARGUMENTS

SEE ALSO
       
'''

dna='AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC'

print(f'La cantidad de nucleotidos que contiene la secuencia es:\n{len(dna)}')

print(f"A = {dna.count('A')}\tT = {dna.count('T')}\tG = {dna.count('G')}\tC = {dna.count('C')}")
