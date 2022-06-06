# Operadores booleanos y condicionales
__Nombre:__ Victor Plascencia

### Operadores logico
Solo se toman dos valores: True o False

```python
bool(objet)
# True o False
```

Orden de prioridad:

1.  Not (Da true si el arg es falso)
2.  And (Da True si los dos arg son True)
3.  Or(Da True si alguno es True)

Nota: a menos que haya un parentesis

**True y false no son cadenas, y se requiere poner (True) o (False)**

### Operadores para True y False

==

<>

! =

in→ prueba sin un valor esta en la lista.

is→ checa si dos objetos apuntan a la misma direccion de memoria.

-   Metodos que regresan valores de True o False

1.  .count
2.  .startswith
3.  endswith
4.  issupper
5.  islower

-   Diferencias entre is e ==
-   is se usa para saber si apuntan hacia el mismo objeto y el == para saber si los contenidos son iguales.

### Sentencia if

```python
## Sintaxis
if <exp>:
	<statement>
elif <exp>:
	<statement>
elif ...
#Hasta el final
else
```

**Else**
Si la expresion del if no se cumple, esta entra en accion

### While
```python
count = 0

while count <= 10:
	print(count)
	count = count + 1
```