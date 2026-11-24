# Importation des fonctions depuis les autres fichiers
from binary_to_decimal import binary_to_decimal
from decimal_to_binary import decimal_to_binary

# Menu utilisateur
print("===Convertisseur binaire/décimal===")
choix = 0
while True:
    print("Quel convertisseur voulez-vous utiliser ?")
    print("1. Entier vers Binaire \n2. Binaire vers Entier  \n3. Quitter")
    choix = input()

# Action réalisée en fonction du choix de l'utilisateur :
    match choix:
        case 1:
            print("Donnez votre nombre entier")
            decimal_number = input()
            print(decimal_number,
                  "convertit en binaire est :",
                  decimal_to_binary(decimal_number))

        case 2:
            print("Donnez votre nombre binaire")
            binary_number = input()
            print(binary_number,
                  "convertit en nombre entier est :",
                  binary_to_decimal(binary_number))

        case 3:
            print("Merci et à bientôt")
            break
