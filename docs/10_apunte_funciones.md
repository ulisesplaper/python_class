# Funciones
__Nombre:__ Victor Plascencia

Bloque de codigo reutilizable que se puede ejecutar muchas veces dentro de un programa

* Sintaxis *

 ```python
def function_name:
	Instructions
	Return(value)

	
```
**nota:**
Es importante primero definir una funcion y luego llamarla (lenguaje interpretado).
Las variables solo son reconocidas en el ambito de la funcion. Son variables locales

#### Argumentos
Si ocupamos el nombre del argumento, ya no importa el orden en que pasemos los argumentos.
```python
get_at_content(dna="ATCGTGACTCG", sig_figs=2)

get_at_content(sig_figs=2, dna="ATCGTGACTCG")
```
#### Testing
`assert get_at_content("ATGC") == 0.5`
Si no es igual, produce el error AssertionError