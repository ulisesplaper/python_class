# Apunte clase 10

### Operadores logico

Orden de prioridad:

1.  Not
2.  And
3.  Or

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

