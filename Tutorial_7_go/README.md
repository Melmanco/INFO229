### Tutorial 7 Go\

¿Qué es go?\

Go es un lenguaje de código abierto, compilado y tipificado estáticamente según la tradición de Algol y C. Cuenta con características como recolección de basura, tipificación estructural limitada, funciones de seguridad de la memoria y programación concurrente de estilo CSP fácil de usar.  
(wikipedia)

### instalar (en archlinux)\

# Instalar go compiler\
`sudo pacman -S`\
\
# Paquete adicional que contiene herramientas importante\
`sudo pacman -S go-tools`\
\
\
## primer codigo en go\
nombramos un archivo como hello.go\
```
package main

import "fmt"

func main() {
    fmt.Println("Hello world!")
}
 
```
\
para ejecutarlo debemos usar\
\
`go run <nombre archivo>`\
\
> tambien es posible compilarlo y luego ejecutarlo
> par ello debemos usar `go build <nombre_archivo>`
> y lo ejecutamos `./nombre_archiivo`
\
en go para importar bibliotecas tenemos que agregarlas a import("biblioteca"), ejemplo:\
```
import (
	"fmt"
	"time"
        )
```
\
es necesario en cada código definir el paquete en el que trabajamos, en hello.go definimos que estabamos en `package main`
\
un ejemplo un poco mas avanzando y enfocado en el lado fuerte de go:  \
el siguente código crea un pequeño servidor que atenderá peticiones HTTP\
lo nombraremos ht.go
```
package main
import (
  "fmt"
  "net/http"
)
func manejador(w http.ResponseWriter, r *http.Request){
  fmt.Fprintf(w,"Hola, %s, ¡este es el servidor!", r.URL.Path)
}
func main(){
  http.HandleFunc("/", manejador)
  fmt.Println("El servidor se encuentra en ejecución")
  http.ListenAndServe(":8080", nil)}

```
\
para compilar y ejecutarlos\
```
go build ht.go
./ht
```
\
ahora podemos comprobar el servidor con\
\
`http://localhost:8080/go`\
\
nos entregara el siguente mensaje\ 
`Hola, /go, ¡este es el servidor!`\