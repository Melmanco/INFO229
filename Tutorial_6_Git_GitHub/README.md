## Tutorial 6 Git Github

Para este tutorial haré un resumen de qué es git, github y sus usos:

Git es un sistema de control de versiones que fue creado por la necesidad de un sistema de control de versiones libre y distribuido.
Al ser distribuido, facilita enormemente el trabajo en equipo, sobre todo en proyectos muy grandes, donde es casi imposible de mantener
con un sistema de control de versiones centralizado.

GitHub es un servicio de hosting para repositorios almacenados en la nube, agregando funcionalidades extras a git para un trabajo en equipo mejor aún,
y otras funcionalidades sociales, github actualmente es tan usado que hasta se usa fuera del mundo de la programación, por ejemplo para escribir libros.

Desde que descubrí Git, más o menos en segundo semestre de la carrera, siempre lo he usado porque facilita mucho programar, permite implementar funcionalidades
complemante diferentes muy fácil con el uso de las ramas, además no hay miedo de equivocarse al programar, ya que todo queda guardado en cada commit y puede revertirse o cambiarse
sin mayores complicaciones.

Uso básico de Git y GitHub:

Para descargar un repositorio entero se usa:
`git clone <URL del repositorio>`, con esto el repositorio se descarga completo y queda listo para su uso.

Para crear un repositorio desde 0:
`git init` dentro de una carpeta, creará un repositorio dentro de esa carpeta.

Cuando se hacen cambios dentro del repositorio, se pueden visualizar con:
`git status`, esto es muy bueno para mantener el control del repositorio.

Cuando estos cambios se quieren añadir al staging area, que es donde se encuentra los archivos que se quieren guardar en el repositorio y su historial:
`git add <archivos>`

Cuando existen archivos que no se quieren subir, como archivos de testeo que sólo estarían de sobra en el repositorio,
se dejan sus nombres dentro del archivo `.gitignore`, estos archivos se ignorarán completamente en el repositorio.

Cuando ya hay archivos en el staging area, se deben guardar en el repositorio, antes de esto el repositorio en sí no ha sufrido ninguno cambio:
`git commit -m "descripción"`, guarda los archivos del staging area con la descripción que se desee.

Cuando se quiere conectar un repositorio local creado por `git init` con un repositorio en GitHub, se debe usar el comando:
`git remote add origin <URL>`

Ahora que ya tenemos commits y un repositorio remoto, se deben 'pushear' los cambios realizados:
cuando se pushea un repositorio por primera vez, se debe usar `git push -u origin master`
cuando ya se ha pusheado el repositorio, basta con usar `git push`

Cuando se quiere actualizar un repositorio local conectado a un repositorio remoto, se debe usar:
`git pull`

Cuando se quiere ver el historial de un repositorio, se debe usar el comando:
`git log`, pero esto muestra mucha información y es difícil de leer.
con `git log --oneline` se puede ver lo mismo pero en una línea por commit, mucho más legible.

Una de las funcionalidades más llamativas de git son las ramas, todo este tiempo hemos estado usando sólo master,
la rama principal del repositorio.

Para crear una rama se debe usar:
`git branch <nombre de la rama>`

Para moverse entre ramas o commits se debe usar:
`git checkout <nombre de la rama>`

Para eliminar una rama:
`git branch -d <nombre de la rama>`

Otra funcionalidad muy importante de las ramas, es la capacidad de combinar ramas, para ésto se usa el comando:
`git merge <rama>`, combina la rama actual con la especificada en el comando.

Esto las combina si no hay problemas, o si los hay, nos lleva al editor por defecto en git y hace que nosotros mismo
podamos decidir los cambios que tienen conflictos, algo muy útil.

Para ver las diferencias entre ramas, se debe usar:
`git diff <rama1> <rama2>`
