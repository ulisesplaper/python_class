# Manejo de excepciones
__Nombre:__ Victor Plascencia

* Cuando un listas, cadenas o numeros son falsos o verdaderos
* Operadores logicos

#### Operadores logicos (CONTINUACION)

### While loop
```python

while <cond>:
	...
	
```

### Expresiones complejas
-> Cuidar que no sean tan largas

## Desarrollo de software y errores
- Errores de sintaxis
Antes de que se ejecute el progrma. Lo identifica el interprete
* Errores logicos 
Son errores de acuerdo con la interpretacion del programa
```python
dna = 'agacta'
#Identificar 'A'
```
* Errores de tiempo de ejecucion 
Logica y sintacticamente correcto, pero equivocado
1. Division sobre 0.
2. No  such file or directory (io)

- Manejo de excepciones
```python
try:
	f = open ('missing.txt')
	## Actions
	
except <error kind>:
	print("sorry, could't find the file")
```
1. IO error -> No se encuentra el archivo
2. Value error -> querer convertir valores en otros incompatibles

Se pueden manejar varios tipos de errores y decidir la accion a realizar
```python
try:
	if =open('data/7-file_num.txt')
	my_number = int(f.read())
	print(my_number + 5)

except IOError:
	print("sorry, couldn't find the file")
except ValueError:
	print("sorry, couldn't parse the number")
```

**Else y finally**
Else sirvecuando necesitamos asegurarnos que no habrá ningún error 
* Finally: estas lineas se ejecutan aunque haya errores

##### raise
Permite generar nuestros errores
```python
e = ValueError("this is a description of the problem")

raise e
```
