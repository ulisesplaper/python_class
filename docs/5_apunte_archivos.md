# Archivos
__Nombre:__ Victor Plascencia

### Input()
pedir el dato al usuario
```python
var = input("mensaje")
```

### open()
```python
file = open("name.txt")

# Leer el archivo
my_file_contents = my_file.read()
```
**Nota: metodo rstrip**
```python
my_dna = my_file_contents.rstrip("\n")
```
Tambien podemos hacer mas cosas con open
`r`- **Read** - Valor _default_. Abre y lee un archivo. _Error si no existe_

`a`- **Append** - Abre un archivo por apendice (agregar al final) y crea un archive si no existe

`w`- **Write** - Abre un archivo para escribir y crea un archive si no exite

`x`- **Create** - Crea un archivo específico y regresa error si ya existe

### close()
Es importante cerrar el archivo cuando hayamos terminado de leer o escribir