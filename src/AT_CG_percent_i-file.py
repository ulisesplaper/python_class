''' NAME
      AT_CG percent

VERSION
        1.0

AUTHOR
        Victor Ulises Plascencia Perez

DESCRIPTION
       Este programa calcula el porcentaje de los nucleotidos AT y GC, por separado, de una secuencia de DNA tomada de un archivo .txt

USAGE
         
ARGUMENTS

SEE ALSO

GitHub link
        
       
'''

## Se le solicita al usuario la ruta y nombre del archivo.
print("Ingrese la ruta y el nombre del archivo que contiene la secuencia de DNA")
my_file_name=input()
## Se abre el archivo y se almacena en una variable
my_file=open(my_file_name)
## Se lee el contenido del archivo y se guarda en una variable.
my_file_contents = my_file.read()
## Se imprime la variable que contiene la secuencia (visualizacion de datos)
print(f"La secuencia proporcionada es {my_file_contents}\n")

# Se quita el caracter de salto de linea y el output se almacena en una
## nueva variable.
my_dna = my_file_contents.rstrip("\n")

# Se realizan las operaciones para calcular el % de AT y GC.
total_count = len(my_dna)
t_count = my_dna.count("T")
a_count = my_dna.count("A")
g_count = my_dna.count("G")
c_count = my_dna.count("C")

## Se imprime el resultado obtenido.
print(f"Porcentaje de AT es: {((t_count+a_count)/total_count)*100} %\nPorcentaje de GC es: {((g_count+c_count)/total_count)*100} % ")
