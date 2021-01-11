Nestor_Malla es un bot que es capaz de presentar la malla ordenada por semestres de la carrera Ingenieria Civil Informatica de la UACH en la plataforma Slack.

Este tiene implementada la malla dentro de su codificacion enviando esta malla en forma de mensaje en Slack , dividiendo los ramos por su semestre con su nombre y su codigo.

Se utilizaron las herramientas que se construyeron en el tutorial 3 de rabittmq, nestor_reader_2 y nestor_writer para la construccion del bot , estás solo fueron cambiadas para que sean capaces de recibir el routing_key con el comando [malla], que al colocarlo en slack te imprime la malla completa de la carrera.

**Problematicas**

Las problematicas que tuvimos al crear a Nestor_Malla fue que al intentar imprimir no dejaba imprimir  más de 500 caracteres en slack, y que al momento de llamar una función solo se imprimieron los primeros elementos de esta. por eso optamos por una lista y que obtuvieramos sus elementos con un ciclo for

**Mejoras**

En cuanto a mejoras futuras, habría que investigar la forma de poder imprimir más de una sola línea a la vez, además poder agregar más funcionalidades como solo imprimir un semestre en específico o también guardar en una base de datos los ramos del usuario y entregarle solo los ramos que sea capaces de dar.