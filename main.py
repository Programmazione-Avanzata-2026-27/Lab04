from lingotto_fiere import LingottoFiere

def menu():
    print(f'\n--- MENU LINGOTTO FIERE ---')
    print("1. Modifica nome del centro fieristico")
    print("2. Carica dati da file")
    print("3. Assegna stand a espositore")
    print("4. Visualizza elenco espositori")
    print("5. Visualizza stand ordinati per prezzo")
    print("6. Esci")

    return input("Scegli un'opzione >> ")

def main():
    lingotto = LingottoFiere("Lingotto Fiere")

    while True:
        scelta = menu()

        if scelta == "1":
            nuovo_nome = input("Inserisci il nuovo nome del centro fieristico: ")
            # TODO: Aggiorna il nome del centro fieristico
            lingotto.nome= nuovo_nome
            print(f"Il nuovo nome è {lingotto.nome}")

        elif scelta == "2":
            file_path = "dati_lingotto.csv"
            try:
                lingotto.carica_file_dati(file_path)
                print("Dati caricati correttamente.")
            except FileNotFoundError:
                print("File non trovato.")

        elif scelta == "3":
            codice_stand = input("Codice stand: ")
            codice_espositore = input("Codice espositore: ")
            try:
                lingotto.assegna_stand_a_espositore(codice_stand, codice_espositore)
                print("Stand assegnato con successo.")
            except Exception as e:
                print(f"Errore: {e}")

        elif scelta == "4":
            print("\n--- Elenco espositori ---")
            lingotto.elenca_espositori()

        elif scelta == "5":
            stand_ordinati = lingotto.stand_ordinati_per_prezzo()
            print("\n--- Stand ordinati per prezzo ---")
            for s in stand_ordinati:
                print(s.descrivi_stand())

        elif scelta == "6":
            print("Uscita dal programma.")
            break

        else:
            print("Scelta non valida.")

if __name__ == "__main__":
    main()
