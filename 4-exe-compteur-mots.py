def compter_mots(phrase):
    compteur = {}
    for mot in phrase.lower().split():
        compteur[mot] = compteur.get(mot, 0) + 1
    return compteur


def main():
    phrase = input("Phrase : ")
    compteur = compter_mots(phrase)

    for mot, nombre in compteur.items():
        print(f"{mot} : {nombre}")


if __name__ == "__main__":
    main()

#Explaination:
# This code defines a function `compter_mots` that counts the occurrences of each word in a given phrase. The `main` function prompts the user to input a phrase, calls the `compter_mots` function to get the word count, and then prints each word along with its corresponding count. The words are converted to lowercase to ensure that the counting is case-insensitive.