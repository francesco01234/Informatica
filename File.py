import random
import time

# Scelta difficolta
print("=== GIOCO DEI FUNGHI ===")
print("1 - Facile")
print("2 - Medio")
print("3 - Difficile")
scelta = input("Scegli difficoltà: ").strip()

if scelta == "1":
    dimensione = 5
    numero_funghi = 10
    tempo_limite = 240
elif scelta == "2":
    dimensione = 7
    numero_funghi = 25
    tempo_limite = 120
elif scelta == "3":
    dimensione = 9
    numero_funghi = 40
    tempo_limite = 60
else:
    print("Scelta non valida. Il programma si interromperà.")
    exit()