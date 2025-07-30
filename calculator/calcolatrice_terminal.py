from colorama import init, Fore, Style

# Inizializza colorama (per Windows)
init(autoreset=True)

# Funzioni per operazioni
def somma(a, b):
    return a + b

def sottrazione(a, b):
    return a - b

def moltiplicazione(a, b):
    return a * b

def divisione(a, b):
    if b == 0:
        return "Errore: divisione per zero"
    return a / b

# Storico dei calcoli
storico = []

print(Fore.CYAN + "Benvenuto nella calcolatrice Python avanzata!")
print("Scrivi 'esci' per uscire oppure 'storico' per vedere i calcoli effettuati.")

while True:
    operazione = input(Fore.YELLOW + "\nScegli un'operazione (+, -, *, /): ").strip()

    if operazione == "esci":
        print(Fore.GREEN + "Programma terminato.")
        break
    elif operazione == "storico":
        print(Fore.MAGENTA + "\n📜 Storico calcoli:")
        if not storico:
            print("Nessun calcolo ancora.")
        else:
            for item in storico:
                print("  " + item)
        continue
    elif operazione not in ['+', '-', '*', '/']:
        print(Fore.RED + "Operazione non valida.")
        continue

    try:
        num1 = float(input("Inserisci il primo numero: "))
        num2 = float(input("Inserisci il secondo numero: "))

        if operazione == '+':
            risultato = somma(num1, num2)
        elif operazione == '-':
            risultato = sottrazione(num1, num2)
        elif operazione == '*':
            risultato = moltiplicazione(num1, num2)
        elif operazione == '/':
            risultato = divisione(num1, num2)

        messaggio = f"{num1} {operazione} {num2} = {risultato}"
        print(Fore.CYAN + "Risultato:", risultato)
        storico.append(messaggio)

    except ValueError:
        print(Fore.RED + "Devi inserire numeri validi.")
