### Tutorial 9 Ruby\
\
## Instalar Ruby (en archlinux)\
\
`sudo pacman -S ruby`\
\
 Además, se puede instalar un cliente interactivo de ruby\
 \
 `sudo pacman -S ruby-irb`\
 \
 Ruby es un lenguaje muy simple de escribir. parecido a python\
 \
 Creamos y ejecutamos nuestro primer código\
 \
 `echo "puts \"Hello World\!\"" > helloworld.rb`\
 `ruby helloworld.rb`\
 \
 `Hello World!`\
 \
 Ahora crearemos un programa que pide palabras a un usuario y luego las imprime alfabéticamente\
 \
 ```
puts "Escribe una frase: "
frase = gets
lista_palabras = frase.split(" ")
lista_palabras.sort!

for palabra in lista_palabras
    puts palabra
end
```
\
Input: 'Ruby es muy entretenido'
Output:\
```
Ruby
entretenido
es
muy
```