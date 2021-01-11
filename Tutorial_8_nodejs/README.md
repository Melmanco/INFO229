### Tutorial 8 nodejs\
\
## Instalación (en archlinux)\
\
`sudo pacman -S nodejs`\
\
Y para el `node package manager`:\
`sudo pacman -S npm`\
\
# Hello World\
\
Hay que crear una carpeta vacía\
`mkdir hello`\
`cd hello`\
\
Y crear nuestro archivo .js\
`touch app.js`\
\
En nuestro archivo escribimos:\
```
var msg = 'Hello World!';
console.log(msg);
```
\

Express es un framework muy útil para crear y ejecutar applicaciones de nodejs\
\
## Instalación de Express\
\
`sudo npm install -g express-generator`\
\
## Uso básico\
\
Ahora creamos una app básica con express\
\
`express myExpressApp --view pug`\
\
Esto crea la estructura de una aplicación básica dentro de la carpeta `myExpressApp`\
\
`cd myExpressApp`\
\
Instalamos las dependencias con npm\
\
`npm install`\
\
La aplicación Express creada contiene un `package.json`, que tiene un script `start` para correr `node ./bin/ww`\
\
Ejecutamos nuestra aplicación\
\
`npm start`\
\
Ahora tenemos nuestra aplicación básica corriendo en `http://localhost:3000`