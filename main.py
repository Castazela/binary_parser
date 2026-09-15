from binary_to_decimal import binary_to_decimal
from decimal_to_binary import decimal_to_binary

# Vous voulez faire quoi ?
print("Quel convertisseur voulez-vous utiliser ?")
print("1. Entier vers Binaire \n2. Binaire vers Entier")
choix = input()

# Convertir décimal -> binaire
if choix == '1':
    print("Donnez votre nombre entier")
    decimal_number = input()
    print(decimal_number,
          "convertit en binaire est :",
          decimal_to_binary(decimal_number))
else:
    print("Donnez votre nombre binaire")
    binary_number = input()
    print(binary_number,
          "convertit en nombre entier est :",
          binary_to_decimal(binary_number))
