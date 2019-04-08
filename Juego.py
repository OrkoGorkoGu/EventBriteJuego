import random

def get_user_feedback():
    # Obtener 
    print("¿Tengo razón?")
    print("\ts\tSí, adiviné el número")
    print("\tg\tNo, mi adivinanza fue demasiado grande.")
    print("\tc\tNo, mi adivinanza fue demasiado chico.")
    res = input().lower()

    if not res in ("sgc") or len(res) != 1:
        return "Invalid Response"

    return res

def give_user_feedback(ans, guess):
    if guess == ans:
        str = "¡Felicidades! Has adivinado mi número."
    else:
        str = "Necesitas un número más %s." %('chico' if guess > ans else 'grande')

    return str

def user_guess_turn():
    

def increase_min(guess):
    return guess + 1

def decrease_max(guess):
    return guess - 1

def get_user_number():
    try:
        num = int(input())
        return num
    except ValueError:
        return "Invalid Input"

def generate_number(min, max):
    try:
        return random.randint(min,max)
    except ValueError:
        # Error
        return "Invalid Range"

def computer_guess():
    # Iniciar el alcance para adivinar
    min = 1
    max = 100

    while True:  
        # Adivinar el número del usario
        adiv = generate_number(min, max)
        
        print("\nMi adivinanza es %s" %adiv)

        res = get_user_feedback()
        if res == "Invalid Response":
            # Usario dio algo inválido
            print("Has apuntado algo inválido. Adivino otra vez.")
            continue

        # PC ha adivinado el número
        if res == "s":
            # El juego se acabó
            break
        
        # Adivinanza de la PC es demasiado grande
        else:
            decrease_max(adiv) if res == 'g' else increase_min(adiv)            

def player_guess():
    # Iniciar el alcance para adivinar
    min = 1
    max = 100

    # Generar un numero
    num = generate_number(min, max)

    while True:
        # Pedirle al usario un número
        print("Qué es tu adivinanza?")
        adiv = get_user_number()
        if adiv == "Invalid Input":
           print("Has apuntado algo inválido. Volvé a intentar otra vez.")
           continue
        print(give_user_feedback(num, guess))
            

    while not (adiv == num):
        # Decirle al usario como fue su adivinanza
        print(give_user_feedback(num, guess))
        print("Qué es tu adivinanza?")
        adiv = get_user_number()
        if adiv == "Invalid Input":
           print("Has apuntado algo inválido. Volvé a intentar otra vez.")
    
    # ha llegado al número
    print("¡Felicidades! Has adivinado mi número.")

def main():
    # Preguntarle al usario si querés jugar
    res = input("Hola! Bienvenido al juego! ¿Listo para jugar (s/n)?")

    # Usario no está list@
    if res.lower() == "n":
        # dejar del programa
        return
    elif res.lower() != "s":
        print("No sé que querés, así continuaremos.")
    
    # Mandarle un mensaje al usario
    print("\nBueno, vamos a jugar un juego de adivinanzas. Alguien eligirá un número, y el otro va a adivinar hasta llegar al número.\n")
    print("¿Querés elegir primero?")
    print("Si es así, pulse <enter> y pensá en un número entre 1 y 100.")
    res = input("Si no, dime 'no' y yo empezaré. ")

    if res.lower() == 'no':
        player_guess()
    else:
        computer_guess()
                
    print("¡Gracias por jugar conmigo! Chau.")

    return
    
if __name__ == "__main__":
    main()

