#Exercice 3 - Fichier python
def demander_nombre(message):
    while True:
        saisie = input(message)
        try:
            return float(saisie)
        except ValueError:
            print("Saisie invalide, recommence.")


def main():
    a = demander_nombre("Premier nombre : ")
    b = demander_nombre("Second nombre : ")

    try:
        resultat = a / b
        print(f"{a} / {b} = {resultat}")
    except ZeroDivisionError:
        print("Impossible de diviser par zéro.")


if __name__ == "__main__":
    main()

#Explaination:
# This code defines a function `demander_nombre` that prompts the user for a number and keeps asking until a valid float is entered. The `main` function uses this to get two numbers from the user, attempts to divide the first number by the second, and handles any division by zero


