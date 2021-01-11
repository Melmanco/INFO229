#Uso:

Se debe buildear con:

`docker build . -t jamesbot --build-arg SLACK_TOKEN=$SLACK_TOKEN`

El argumento de "--build-arg" nos permite pasar el token de slack desde las variables de entorno del host,
así es más fácil de usar en otros pcs y además es seguro, ya que en ningún momento se usan estos importantes tokens dentro del código.

Luego, se ejecuta con:

`docker run jamesbot`