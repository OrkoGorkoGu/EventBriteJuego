import random

def main():
    # Le preguntar al usario si querés jugar
    res = input("Hola! Bienvenido al juego! ¿Listo para jugar (s/n)?")
    if res == "n":
        return
    
    # Le Mandar un mensaje al usario
    print("\nBueno, vamos a jugar un juego de adivinanzas. Alguien eligirá un número, y el otro va a adivinar hasta llegar al número.\n")
    print("¿Querés empezar?")
    print("Si es así, pulse <enter> y pensá en un número entre 1 y 100.")
    res = input("Si no, dime 'no' y yo empezaré. ")

    if res.lower() == 'no':
        # Generar un numero
        num = random.randint(1,100)

        userGuess = int(input("Qué es tu adivinanza?"))

        while not (userGuess == num):
            if userGuess > num:
                print("Necesitas un número más chico.")
            elif userGuess < num:
                print("Necesitas un número más grande.")
            
            userGuess = int(input("Qué es tu adivinanza?"))
        
        # ha llegado al número
        print("¡Felicidades! Has adivinado mi número.")

    else:
        min = 1
        max = 100
        # Adivinar el número del usario
        compGuess = random.randint(1,100)

        print("\nMi adivinanza es %s" %compGuess)
        print("¿Tengo razón?")
        print("\ts\tSí, adiviné el número")
        print("\tg\tNo, mi adivinanza fue demasiado grande.")
        print("\tc\tNo, mi adivinanza fue demasiado chico.")
        res = input()
        
        while not (res.lower() == "s"):
            
            if res.lower() == "g":
                max = compGuess
                compGuess -= int((compGuess - min)/2)
            elif res.lower() == "c":
                min = compGuess
                compGuess += int((max - compGuess)/2)
            
            print("\nMi adivinanza es %s" %compGuess)
            print("¿Tengo razón?")
            print("\ts\tSí, adiviné el número")
            print("\tg\tNo, mi adivinanza fue demasiado grande.")
            print("\tc\tNo, mi adivinanza fue demasiado chico.")
            res = input()  

    print("¡Gracias por jugar conmigo! Chau.")
    return

if __name__ == "__main__":
    main()

