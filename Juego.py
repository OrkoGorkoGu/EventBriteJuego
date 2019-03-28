import random

def main():
    # Le preguntar al usario si querés jugar
    res = input("Hola! Bienvenido al juego! ¿Listo para jugar (s/n)?")

    # Usario no está list@
    if res.lower() == "n":
        # dejar del programa
        return
    
    # Le Mandar un mensaje al usario
    print("\nBueno, vamos a jugar un juego de adivinanzas. Alguien eligirá un número, y el otro va a adivinar hasta llegar al número.\n")
    print("¿Querés elegir primero?")
    print("Si es así, pulse <enter> y pensá en un número entre 1 y 100.")
    res = input("Si no, dime 'no' y yo empezaré. ")

    if res.lower() == 'no':
        # Generar un numero
        num = random.randint(1,100)

        while True:
            try:
                userGuess = int(input("Qué es tu adivinanza?"))
                break
            except:
                print("Has apuntado algo inválido. Volvé a intentar otra vez.")

        while not (userGuess == num):
            print("Necesitas un número más %s." %('chico' if userGuess > num else 'grande'))
            
            try:
                userGuess = int(input("Qué es tu adivinanza?"))
            except:
                print("Has apuntado algo inválido. Volvé a intentar otra vez.")
        
        # ha llegado al número
        print("¡Felicidades! Has adivinado mi número.")

    else:
        # Iniciar el alcance para adivinar
        min = 1
        max = 100

        while True:  
            # Adivinar el número del usario
            try:
                compGuess = random.randint(min,max)
            except:
                # el alcance de los números ya está agotado
                print("Me parece que me has mintirado...ya no quiero jugar.")

                # dejar del programa
                return

            print("\nMi adivinanza es %s" %compGuess)
            print("¿Tengo razón?")
            print("\ts\tSí, adiviné el número")
            print("\tg\tNo, mi adivinanza fue demasiado grande.")
            print("\tc\tNo, mi adivinanza fue demasiado chico.")
            res = input()  

            # PC ha adivinado el número
            if res == "s":
                # Juego se acabó
                break
            
            # Adivinanza de la PC es demasiado grande
            elif res.lower() == "g":
                # Cambiar el máximo
                max = compGuess - 1
            
            # Adivinanza de la PC es demasiado chico
            elif res.lower() == "c":
                # Cambiar el mínimo
                min = compGuess + 1
            
            # Usario dio algo inválido
            else:
                print("Has apuntado algo inválido. Adivino otra vez.")
                

    print("¡Gracias por jugar conmigo! Chau.")
    return

if __name__ == "__main__":
    main()

