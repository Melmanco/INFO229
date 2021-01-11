#!/usr/bin/env python
import pika
import time
import os


time.sleep(30)

MALLA = [['1', 'BAIN065-14', 'ÁLGEBRA PARA INGENIERÍA'], ['1', 'BAIN067-14', 'GEOMETRÍA PARA INGENIERÍA'], ['1', 'BAIN071-14', 'COMUNICACIÓN IDIOMA ESPAÑOL'], ['1', 'INFO063-17', 'INTRODUCCIÓN A LA PROGRAMACION'], ['1', 'INFO073-17', 'TALLER DE INGENIERÍA: INTRODUCCION A LA INGENIERIA'], ['2', 'BAIN069-14', 'QUÍMICA PARA INGENIERÍA'], ['2', 'BAIN073-14', 'ÁLGEBRA LINEAL PARA INGENIERIA'], ['2', 'BAIN075-14', 'CÁLCULO EN UNA VARIABLE'], ['2', 'BAIN079-14', 'COMUNICACIÓN IDIOMA INGLÉS'], ['2', 'DYRE070-14', 'EDUCACIÓN FÍSICA Y SALUD'], ['2', 'INFO081-17', 'PROGRAMACIÓN'], ['2', 'INFO083-17', 'TALLER DE INGENIERÍA: PROGRAMACION'], ['3', 'BAIN077-14', 'FÍSICA: MECÁNICA'], ['3', 'BAIN081-14', 'ECUACIONES DIFERENCIALES'], ['3', 'BAIN083-14', 'CÁLCULO EN VARIAS VARIABLES'], ['3', 'ELECT12   ', 'OFG 1'], ['3', 'INFO085-17', 'ESTRUCTURA DE DATOS Y ALGORITMO'], ['3', 'INFO088-17', 'TALLER DE INGENIERÍA: ESTRUCTURA DE DATOS Y ALGORITMO'], ['4', 'BAIN085-14', 'FÍSICA: ONDAS Y ELECTROMAGNETISMO'], ['4', 'BAIN087-14', 'MÉTODOS NUMÉRICOS PARA INGENIERIA'], ['4', 'BAIN091-14', 'ESTADÍSTICA Y PROBABILIDADES'], ['4', 'INFO090-17', 'PROGRAMACIÓN ORIENTADA A OBJETOS'], ['4', 'INFO099-17', 'ESTRUCTURAS DISCRETAS'], ['4', 'INFO104-17', 'TALLER DE CONSTRUCCIÓN DE SOFTWARE'], ['5', 'BAIN140-17', 'INGLÉS INSTRUMENTAL'], ['5', 'EICI146-17', 'PRÁCTICA INICIAL'], ['5', 'ELECT100  ', 'OPTATIVO DE ESPECIALIZACION'], ['5', 'INFO128-17', 'ARQUITECTURA DE COMPUTADOR'], ['5', 'INFO133-17', 'BASE DE DATOS'], ['5', 'INFO139-17', 'TEORÍA DE AUTÓMATAS'], ['5', 'INFO145-17', 'DISEÑO Y ANÁLISIS DE ALGO'], ['6', 'BAIN150-17', 'INGLÉS FUNCIONAL'], ['6', 'INFO188-17', 'PROGRAMACIÓN EN PARADIGMA'], ['6', 'INFO198-17', 'SISTEMAS OPERATIVOS'], ['6', 'INFO200-17', 'INVESTIGACIÓN OPERATIVA'], ['6', 'INFO208-17', 'INGENIERÍA DE REQUISITOS'], ['6', 'INFO229-17', 'ARQUITECTURA DE SOFTWARE'], ['7', 'ELECT101  ', 'OPTATIVO DE ESPECIALIZACION'], ['7', 'INFO221-20', 'GESTIÓN ORGANIZACIONAL'], ['7', 'INFO239-17', 'COMUNICACIONES'], ['7', 'INFO245-17', 'INTERACCIÓN HUMANO-COMPUTADOR'], ['7', 'INFO248-17', 'INGENIERÍA DE SOFTWARE'], ['7', 'INFO257-17', 'INTELIGENCIA ARTIFICIAL'], ['8', 'ELECT111  ', 'OPTATIVO DE ESPECIALIZACION'], ['8', 'INFO270-17', 'EVALUACIÓN DE PROYECTOS I'], ['8', 'INFO276-17', 'REDES'], ['8', 'INFO278-17', 'SISTEMAS DE INFORMACIÓN'], ['8', 'INFO280-17', 'SEMINARIO DE ÉTICA PROFES'], ['8', 'INFO282-17', 'TALLER DE INGENIERÍA DE SOFTWARE'], ['9', 'EICI270-17', 'TALLER DE EMPRENDIMIENTO'], ['9', 'ELECT112  ', 'OPTATIVO DE PROFUNDIZACIÓN'], ['9', 'INFO286-17', 'SISTEMAS DE GESTIÓN'], ['9', 'INFO288-17', 'SISTEMAS DISTRIBUIDOS'], ['9', 'INFO289-17', 'TALLER DE INTEGRACIÓN DE...'], ['9', 'INFO290-17', 'MÉTODOS Y MODELOS DE INGE'], ['10', 'ELECT116  ', 'OPTATIVO DE PROFUNDIZACIÓN'], ['10', 'INFO293-17', 'TECNOLOGÍA DE LA INFORMACION'], ['10', 'INFO297-17', 'TALLER DE TÍTULO'], ['10', 'INFO294-17', 'REALIDAD TECNOLÓGICA NACI'], ['11', 'INFO295-17', 'PRÁCTICA PROFESIONAL (a)'], ['11', 'INFO298-17', 'PROYECTO DE TÍTULO: ARTÍC'], ['11', 'INFO299-17', 'PROYECTO DE TÍTULO: MEMOR']]

HOST = os.environ['RABBITMQ_HOST']

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host=HOST))
channel = connection.channel()

channel.exchange_declare(exchange='nestor', exchange_type='topic', durable=True)

result = channel.queue_declare(queue="malla", exclusive=True, durable=True)
queue_name = result.method.queue

channel.queue_bind(exchange='nestor', queue=queue_name, routing_key="malla")

print(' [*] Waiting for messages. To exit press CTRL+C')


def callback(ch, method, properties, body):
    print(body)
    if str(body).startswith("b'[malla]"):
        print(result)
        ########## PUBLICA EL RESULTADO COMO EVENTO EN RABBITMQ ##########
        for j in range (11):
            channel.basic_publish(exchange='nestor', routing_key="publicar_slack", body="semestre: "+str(j+1))
            channel.basic_publish(exchange='nestor', routing_key="publicar_slack", body="Codigo      |               Nombre")
            for x in range ((len(MALLA))):
                niv = MALLA[x][0]
                print (niv)
                if (str(j+1) ==niv):
                    code = MALLA[x][1]
                    name = MALLA[x][2]
                    text = code+"     "+name
                    print(text)
                    channel.basic_publish(exchange='nestor', routing_key="publicar_slack", body=text)


channel.basic_consume(
    queue=queue_name, on_message_callback=callback, auto_ack=True)

channel.start_consuming()