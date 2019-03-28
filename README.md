# Juego.py - Ejercicio 1
### Hecho por: Adam Lathan
### Esto es un juego para mi primer tarea de Eventbrite

## __Como usarlo__:
* Para empezar, la PC va a preguntarle al usario quien debe adivinar primero
* Si el usario quiere adivinar primero:
  * La PC elige un número entre 1 y 100, y le pedi al usario adivinar hasta que adivine el numero
* Si el usario quiere elegir primero:
  * La PC adivina el número del usario hasta que el número haya sido elegido

## __Manejando Errores__
* Cuando el usario está adivinando, si apunta algo inválido (cualquier cosa que no es número), el programa volverá a pedirle otra vez

* Cuando la PC está adivinando, si el usario apunte algo inválido (cualquier cosa que no es una de las cosas en la lista de opciones), el programa volverá a pedirle otra vez

* Cuando la PC está adivinando, si el lógico de lo que el usario dijo (por ejemplo, el usario ha dicho que 79 es demasiado chico, y ahora dice que 80 es demasiado grande), el programa va a terminar.