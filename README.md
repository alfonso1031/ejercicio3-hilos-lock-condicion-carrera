# Ejercicio 3: Hilos, Lock y condición de carrera

El ejemplo representa a dos personas que comparten un presupuesto familiar de
20 USD. Cada una intenta pagar una compra de 15 USD al mismo tiempo.

El programa muestra dos casos:

1. Sin Lock, ambos hilos leen el saldo de 20 USD antes de descontar. Las dos
   compras se aprueban, aunque el presupuesto no alcanza. El saldo registrado
   no coincide con el saldo que deberían dejar esas compras.
2. Con threading.Lock, la consulta y el descuento se protegen juntos. Una
   compra se aprueba y la otra se rechaza, dejando el saldo correcto de 5 USD.

La barrera del primer caso coordina los hilos para que la condición de carrera
se pueda observar al ejecutar el ejemplo.

## Requisitos

- Docker

## Ejecutar con Docker

Desde la carpeta raíz del repositorio, construye la imagen:

    docker build -t ejercicio3-hilos-lock .

Luego ejecuta el contenedor:

    docker run --rm ejercicio3-hilos-lock

## Archivos

- main.py: compara dos hilos que actualizan un presupuesto compartido, con y
  sin Lock.
- Dockerfile: construye y ejecuta el programa con Python.
