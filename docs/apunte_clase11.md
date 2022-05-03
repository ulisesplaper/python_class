# Iniciamos con repaso
* Cuando un listas, cadenas o numeros son falsos o verdaderos
* Operadores logicos


## Operadores logicos (CONTINUACION)

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

