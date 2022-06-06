# Argumentos
__Nombre:__ Victor Plascencia

Usar la linea de comandos para pasar argumentos tiene una serie de ventajas, como la productividad y la automatizacion
#### Formas de manejar argumentos
##### Modulos sys
```python
# Los elementos se guardan en sys.arg
import sys

print (f"The script has the name {(sys.argv[0])} ")

arguments = sys.argv

print (arguments)
```
##### argparse
* Iniciar parser* 
Esto es para darle un tipo objeto parser a una variable.
`parser = argparse.ArgumentParser()`


** Recuerda->En python todo es un objeto**
 ### Name space
 Colleccion aislada de nombres que referencian a objetos.
 Hay de dos tipos: de variables locales y variables globales
 Se construye un NameSpace a partir de la linea de comandos con el metodo a
 
 - Argumentos opcionales: con guion
 - Argumentos posicionales: sin guion
 **Add_argument
```python
my_parser.add_argument('Path',metavar='path',type=str,
					   help='the path to list')

# Asi leemos desde la terminal

args = my_parser.parse_args()
``` 




