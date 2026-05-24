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

# Creazione griglia vuota
lettere = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
scacchiera = []
for riga in range(dimensione):
    linea = []
    for colonna in range(dimensione):
        linea.append(".")
    scacchiera.append(linea)

# Posizionamento dei funghi
funghi = set()
while len(funghi) < numero_funghi:
    riga = random.randint(0, dimensione - 1)
    colonna = random.randint(0, dimensione - 1)
    posizione = (riga, colonna)
    if posizione not in funghi:
        funghi.add(posizione)
        scacchiera[riga][colonna] = ","

# Salvataggio scacchiera iniziale su file
file = open("scacchiera.txt", "w", encoding="utf-8")
for riga in scacchiera:
    file.write(" ".join(riga) + "\n")
file.close()

# lettura e stampa della scacchiera dal file
print("\nScacchiera caricata dal file:\n")
file = open("scacchiera.txt", "r", encoding="utf-8")
contenuto = file.read()
print(contenuto)
file.close()

# Funzione per stampare la griglia di gioco
def stampa_scacchiera():
    print("    ", end="")
    for i in range(dimensione):
        print(lettere[i], end=" ")
    print()

    for riga in range(dimensione):
        print(riga + 1, end="  ")
        for colonna in range(dimensione):
            print(scacchiera[riga][colonna], end=" ")
        print()

