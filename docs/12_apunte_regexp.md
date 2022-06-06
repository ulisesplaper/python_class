# Expresiones regulares
__Nombre:__ Victor Plascencia

Una regexp es una secuencia de caracteres que conforma un patrón de búsqueda

Sitio web para evaluar expresiones regulares :
[regex101: build, test, and debug regex](https://regex101.com/)

**En python:**
```python
# Modulo 
import re
# Buscar
re.search(pattern, string, flags)
# Posibilidades
	re.search("GG(A|T)CC", dna)
	re.search("GG[AT]CC", dna):
# Cualquiere caracter
re.search("GG.CC", dna)
# Negacion
re.search("[^ATGC]", dna)
```
**Cuantificadores**
- ? identifica 0 o una vez el caracter.
* + identifica una o mas veces el caracter
* `*` indica que es opcional pero también puede estar repetido.

**Posicion**
- inicio
`re.search("^AAA", dna)`
* Fin
`re.search("AAA$", dna)`

##### Metodos de re.Match
```python
# Regresa la posicion de inicio y fin del match
m.string
# Regresa el string que le pasamos a la funcion
m.span()
# Regresa la parte de la cadena donde esta el match
m.group()
```
##### finditer y findall
```python
# Finditer regresa un iterador de objetos match
dna = "CGCTCnTAGATGCGCrATGACTGCAyTGC"
matches = re.finditer(r"[^ATGC]", dna)
for m in matches:
	<code>

# Findall regresa una lista de strings o tuplas de los match
dna = "CGCTCnTAGATGCGCrATGACTGCAyTGC"
result = re.findall(r"[^ATGC]", dna)
print(result)
```
##### Dividir
Se puede dividir el string con una regexp
`result = re.split(r"[^ATGC]", dna
