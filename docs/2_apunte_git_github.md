# Git

__Nombre:__ Victor Plascencia

``` python
git init # Iicializar un repositorio
git add # Empezar a controlar un archivo con git
```



Hacer permanente una version

`git commit -m "mensaje" archivo`



Modificar el mensaje del commit

`git commit --amend -m "Mensaje"` 

Buen mensaje para el commit
- menos de 50 caract.
- Para profundizar se puede usar
`git commit -a`

Modificar el mensaje de un commit anterior.

 `git commit --amend -m "mensaje"`

Ver los mensajes que han sido modificados

`git diff `



**Clase del 17/02/22**

``git diff --staged``

Compara lo que hay en el area de preparacion con lo que hicimos en el ultimo commit.

**Siempre se compara con el documento que queda hasta el tope del repositorio**

*Identificador* -> 40 caracteres (hay versiones cortas)

``git log`` Entrega en orden inverso la lista de todos los commits que hemos realizado. Asi como datos 

``git log -n`` Yo indico el numero de commits que quiero que haga.

 ``git status `` Indica los documentos a los que no se les ha hecho un commit.

``git log --oneline`` Muestra el identificador en su forma corta y el mensaje que fue asociado al commit.

**Ramas en git**

Master: Rama principal (tronco)

* develop

* feature x

* hotfix-X

  *Se puede hacer un commit en general y todos los archivos en fase de prep se van al repositorio*

  **Mas sobre git status**

``git status -u`` Nos dice si hay un archivo en un directorio y no solo si el directorio se modifico, por ejemplo.

**Cambiar el mensaje  de un commit que no es el inmediato al anterior**

Ver grabacion de las 12:20 a 12: 28. Esto no es algo muy recomendable

``git checkout`` 

``git diff HEAD(~1,2,3)`` Comparar contra las diferentes cabeceras.

``git diff ID`` Comparar contra un archivo usando su id.

``git show``

**Restaurar una version en git**

1. Identificar a que version queremos regresar.

   1.  ``git checkout `` Toma como ref el id del commit anterior.

   
   
   ### Clase 24/04/22
   

![image-20220224110544337](C:\Users\ulise\AppData\Roaming\Typora\typora-user-images\image-20220224110544337.png)

```bash
# Comit realizado por determinado usuario.
git log --author="Ulises Plascencia" --oneline

#Obtener el usuario que esta trabajando
git config --list

```



#### Archivo borrado

Si creo un archivo, tengo que agregarlo a git con add y luego aplicar el commit.

Que pasa cuando borro archivos?  

Le decimos a git que lo borre, pero... como?
```bash
git rm [nombre del archivo] 
git commit -m "[mensaje]"

```



#### Archivos que no se desea controlar

```bash
archivo.gitignore
# Crear un archivo llamado .gitignore
nano .gitingnore

#Colocar los nombres de los archivos y directorios.

*.dar
/results

# ver archivos que se estan ignorando
git status --ignored

# Ignorar todos los archvivos, excepto uno
*.data
!final.data

```


#### Servicios de hosting
- Github: alojar proyectos basados en git
**Que hicimos en la clases?**
- Crear cuenta y repo
- Conectar mi repo local con el remoto
```bash
git remote add origin [URL]
git remote -v
```
- Actualizar cambios en el repo remoto
```bash
git push origin master
```
- Bajar cambios
`git pull origin master`

- Pull request: solicitud para realizar modificaciones en mis codigos en mi repositorio local
Yo decido si los acepto, pero cuando lo hago otra persona ya es autora de mi codigo