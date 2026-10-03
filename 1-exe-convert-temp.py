def celsius_vers_fahrenheit(celsius):
    return celsius * 9 / 5 + 32


def main():
    valeur = float(input("Température en Celsius : "))
    resultat = celsius_vers_fahrenheit(valeur)
    print(f"{valeur}°C = {resultat}°F")


if __name__ == "__main__":
    main()