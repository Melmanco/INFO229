## Tutorial 5 TDD Docker

# Ejercicio 1.

Por tiempo preferí no hacer este ejercicio, pero tengo una buena idea de como sería ya que no es muy diferente a lo que ya hemos hecho.

# Ejercicio 2.

No habría que cambiar mucho la arquitectura del bot.

- Hay que agregar una función en nestor_events para que pueda procesar el nuevo comando

- Hay que cambiar la relación entre nestor_events y nestor_persistence para que sea de request_reply

- Hay que agregar una función en nestor_persistence obtener y filtrar los mensajes de nestor_mongo