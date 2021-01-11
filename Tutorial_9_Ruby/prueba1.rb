puts "Escribe una frase: "
frase = gets
lista_palabras = frase.split(" ")
lista_palabras.sort!

for palabra in lista_palabras
    puts palabra
end