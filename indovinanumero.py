import random

def gioco_indovina_numero():
    numero_da_indovinare = random.randint(1, 100)
    tentativi = 0
    print("Benvenuto al gioco di indovinare il numero!")
    print("Ho scelto un numero tra 1 e 100. Prova a indovinarlo!")

    while True:
        tentativo = int(input("Inserisci il tuo tentativo: "))
        tentativi += 1
        
        if tentativo < numero_da_indovinare:
            print("Troppo basso! Riprova.")
        elif tentativo > numero_da_indovinare:
            print("Troppo alto! Riprova.")
        else:
            print(f"Complimenti! Hai indovinato il numero {numero_da_indovinare} in {tentativi} tentativi.")
            break

gioco_indovina_numero()
