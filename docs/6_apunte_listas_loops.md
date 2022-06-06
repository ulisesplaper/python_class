# Listas y loops
__Nombre:__ Victor Plascencia


Parametros a evaluar de los programas:

1.  El primer commit debe contener el algoritmo, con pseudocódigo
2.  Poner comentarios por bloque y no por línea. Estos comentarios son de la lógica y no de la instruccion.
3.  Linea entre 60 y 40 caracteres (pep8).
4.  El readme no es por programa, sino por repositorios

## Listas

Son un objeto,

-   Se indican por [ , , ]
-   Acceder a los elementos: se requiere hacer uso de los indices list_name{
-   Acceder a rangos list_name[0:2]
-   Reescribir un elemento de la lista→ apes[3]= “name ape”
-   Concatenar dos listas → list_name + list_name2

### Metodos de la listas

-   Index: acceder al indice de un elemento → list_name.index(’element’)
-   Append: agrega un elemento al final de la lista. Si lo que se agrega es una lista, esta se aniade como un elemento nuevo. Puede agregar de uno a uno.
-   Extend: apes.extend(monkeys). Agrega los elementos

Nota: elemento iterable→ conjunto que tiene mas de un elemento y que pueden recorrerse por elemento

-   Reverse → revierte los elementos de la lista.
-   Sort → ordena alfabeticamente o numericamente

Si intentamos con concatenar

# Loops

### For

```python
# Uso
for <var> in <iterable>:
	<statement(s)>

for ape in apes
	print(ape + "is an ape")  
# Readlines
# Leer todas las lineas y guardarlas en una lista

all_lines = file.readlines()
	
	```