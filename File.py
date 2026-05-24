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

# Variabili di gioco
funghi_trovati = 0
tentativi = 0
registro_mosse = []  
inizio = time.time()

# Ciclo principale della partita
while funghi_trovati < numero_funghi:
    tempo_passato = time.time() - inizio
    tempo_rimasto = int(tempo_limite - tempo_passato)
    
    if tempo_rimasto <= 0:
        print("\nTEMPO SCADUTO!")
        print("Hai perso!")
        break
        
    print("\nTempo rimasto:", tempo_rimasto, "secondi")
    print("Funghi trovati:", funghi_trovati, "/", numero_funghi)
    stampa_scacchiera()
    
        coordinata_input = input("\nInserisci coordinata (esempio A1): ").upper().strip()
    
    if len(coordinata_input) < 2:
        print("Input non valido")
        continue
        
    lettera = coordinata_input[0]
    numero = coordinata_input[1:]
    
    if not numero.isdigit():
        print("Numero non valido")
        continue
        
    riga = int(numero) - 1
    colonna = lettere.find(lettera)
    
    # Controllo confini della mappa
    if riga < 0 or riga >= dimensione:
        print("Riga non valida")
        continue
    if colonna < 0 or colonna >= dimensione:
        print("Colonna non valida")
        continue
        
    tentativi += 1

    # Controllo coordinata inserita
    if scacchiera[riga][colonna] == ",":
        print("Fungo trovato!")
        scacchiera[riga][colonna] = "X"
        funghi_trovati += 1
        registro_mosse.append(f"Mossa {tentativi} -> Coordinata {coordinata_input}: FUNGO TROVATO")
    elif scacchiera[riga][colonna] == "X":
        print("Hai già preso questo fungo!")
        registro_mosse.append(f"Mossa {tentativi} -> Coordinata {coordinata_input}: Gia' preso in precedenza")
    else:
        print("Nessun fungo qui!")
        scacchiera[riga][colonna] = " "  
        registro_mosse.append(f"Mossa {tentativi} -> Coordinata {coordinata_input}: Acqua (Vuoto)")

# Controllo vittoria finale
if funghi_trovati == numero_funghi:
    print("\nCOMPLIMENTI!")
    print("Hai trovato tutti i funghi!")

nome = input("\nInserisci il tuo nome: ").strip()
if nome == "":
    nome = "Cacciatore_Anonimo"

# Salvo il punteggio attuale
file = open("punteggi.txt", "a", encoding="utf-8")
file.write(nome + " - Funghi trovati: " + str(funghi_trovati) + "\n")
file.close()
print("Punteggio salvato nel file punteggi.txt")

# Salvataggio dati per le statistiche generali
file_t = open("statistiche.txt", "a", encoding="utf-8")
esito = "COMPLETATO" if funghi_trovati == numero_funghi else "NON_COMPLETATO"
file_t.write(nome + "," + str(tentativi) + "," + esito + "\n")
file_t.close()

# Calcolo del record assoluto registrato
file_t = open("statistiche.txt", "r", encoding="utf-8")
record_nome = ""
min_tentativi = 999999

for linea in file_t:
    dati = linea.strip().split(",")
    if len(dati) == 3 and dati[2] == "COMPLETATO":
        try:
            t_attuali = int(dati[1])
            if t_attuali < min_tentativi:
                min_tentativi = t_attuali
                record_nome = dati[0]
        except ValueError:
            continue
file_t.close()

print("\n=== RECORD ASSOLUTO ===")
if record_nome != "":
    print("Il record attuale è di:", record_nome, "con soli", min_tentativi, "tentativi!")
else:
    print("Nessun record registrato (nessuno ha ancora completato il gioco trovando tutti i funghi).")

# Conteggio tempo e precisione finali
tempo_finale_impiegato = int(time.time() - inizio)
if tempo_finale_impiegato > tempo_limite:
    tempo_finale_impiegato = tempo_limite

precisione_colpi = (funghi_trovati / tentativi * 100) if tentativi > 0 else 0.0

