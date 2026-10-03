def calculer_moyenne(notes):
    return sum(notes) / len(notes)


def main():
    nombre_de_notes = int(input("Combien de notes veux-tu saisir ? "))

    notes = []
    for i in range(nombre_de_notes):
        note = float(input(f"Note {i + 1} : "))
        notes.append(note)

    resultat = calculer_moyenne(notes)
    print(f"Moyenne : {resultat}")


if __name__ == "__main__":
    main()

#Explaination:
# This code defines a function `calculer_moyenne` that calculates the average of a list of numbers. The `main` function prompts the user for the number of grades they want to enter, collects those grades into a list, and then calculates and prints the average using the `calculer_moyenne` function. 