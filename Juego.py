import random

def output(text):
    output(text)

def get_user_feedback():
    # Obtener 
    output("¿Tengo razón?")
    output("\ts\tSí, adiviné el número")
    output("\tg\tNo, mi adivinanza fue demasiado grande.")
    output("\tc\tNo, mi adivinanza fue demasiado chico.")
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
    pass

def increase_min(guess):
    return int(guess) + 1

def decrease_max(guess):
    return int(guess) - 1

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
        
        output("\nMi adivinanza es %s" %adiv)

        res = get_user_feedback()
        if res == "Invalid Response":
            # Usario dio algo inválido
            output("Has apuntado algo inválido. Adivino otra vez.")
            continue

        # PC ha adivinado el número
        if res == "s":
            # El juego se acabó
            break
        
        # Adivinanza de la PC es demasiado grande
        elif res == 'g':
            max = decrease_max(adiv)
        else:
            min = increase_min(adiv)            

def player_guess():
    # Iniciar el alcance para adivinar
    min = 1
    max = 100

    # Generar un numero
    num = generate_number(min, max)

    while True:
        # Pedirle al usario un número
        output("Qué es tu adivinanza?")
        adiv = get_user_number()
        if adiv == "Invalid Input":
           output("Has apuntado algo inválido. Volvé a intentar otra vez.")
           continue
        output(give_user_feedback(num, adiv))
            

    while not (adiv == num):
        # Decirle al usario como fue su adivinanza
        output(give_user_feedback(num, adiv))
        output("Qué es tu adivinanza?")
        adiv = get_user_number()
        if adiv == "Invalid Input":
           output("Has apuntado algo inválido. Volvé a intentar otra vez.")
    
    # ha llegado al número
    output("¡Felicidades! Has adivinado mi número.")

def main():
    # Preguntarle al usario si querés jugar
    res = input("Hola! Bienvenido al juego! ¿Listo para jugar (s/n)?")

    # Usario no está list@
    if res.lower() == "n":
        # dejar del programa
        return "Game Over"
    elif res.lower() != "s":
        output("No sé que querés, así continuaremos.")
    
    # Mandarle un mensaje al usario
    output("\nBueno, vamos a jugar un juego de adivinanzas. Alguien eligirá un número, y el otro va a adivinar hasta llegar al número.\n")
    output("¿Querés elegir primero?")
    output("Si es así, pulse <enter> y pensá en un número entre 1 y 100.")
    res = input("Si no, dime 'no' y yo empezaré. ")

    if res.lower() == 'no':
        player_guess()
    else:
        computer_guess()
                
    output("¡Gracias por jugar conmigo! Chau.")

    return
    
if __name__ == "__main__":
    main()

