class Espositore:

    def __init__(self, codice, nome, cognome):
        self.codice = codice
        self.nome = nome
        self.cognome = cognome
        self.assegnato = None

    def __str__(self):
        if self.assegnato == None:
            return f"[{self.codice}] {self.nome} {self.cognome} - Stand: Nessuno"
        else:
            return f"[{self.codice}] {self.nome} {self.cognome} - Stand: {self.assegnato.codice}"


class Stand:

    def __init__(self, codice, superficie, padiglione, prezzo_base):
        self.codice = codice
        self.superficie = float(superficie)
        self.padiglione = int(padiglione)
        self.prezzo_base = float(prezzo_base)
        self.assegnato = None

    def calcola_prezzo(self):
        return self.prezzo_base

    def __eq__(self, other):
        return self.codice == other.codice

    def __lt__(self, other):
        return self.calcola_prezzo() < other.calcola_prezzo()

    def __str__(self):
        if self.assegnato == None:
            stato = "disponibile"
        else:
            stato = f"Assegnato a {self.assegnato.codice}"
        return f"{self.codice}: Standard | {self.superficie} mq - Padiglione {self.padiglione} - Prezzo {self.calcola_prezzo():.2f}€ - {stato}"


class StandPrese(Stand):

    def __init__(self, codice, superficie, padiglione, prezzo_base, numeroprese):
        super().__init__(codice, superficie, padiglione, prezzo_base)
        self.numeroprese = int(numeroprese)

    def calcola_prezzo(self):
        return self.prezzo_base * (1 + 0.07 * self.numeroprese)

    def __str__(self):
        if self.assegnato == None:
            stato = "disponibile"
        else:
            stato = f"Assegnato a {self.assegnato.codice}"
        return f"{self.codice}: Prese Extra | {self.superficie} mq - Padiglione {self.padiglione} - Prezzo {self.calcola_prezzo():.2f}€ - Prese aggiuntive: {self.numeroprese} - {stato}"


class StandPremium(Stand):

    def __init__(self, codice, superficie, padiglione, prezzo_base, posizione):
        super().__init__(codice, superficie, padiglione, prezzo_base)
        self.posizione = posizione

    def calcola_prezzo(self):
        return self.prezzo_base * 1.3

    def __str__(self):
        if self.assegnato == None:
            stato = "disponibile"
        else:
            stato = f"Assegnato a {self.assegnato.codice}"
        return f"{self.codice}: Premium ({self.posizione}) | {self.superficie} mq - Padiglione {self.padiglione} - Prezzo {self.calcola_prezzo():.2f}€ - {stato}"


class LingottoFiere:

    def __init__(self, nome):
        self.nome = nome
        self.listastand = []
        self.listaespositori = []
    @property
    def nome(self):
        return self._nome
    @nome.setter
    def nome(self, nuovonome):
        self._nome = nuovonome

    def carica_file_dati(self, file_path):
        try:
            with open(file_path, "r") as f:
                for riga in f:
                    dati = riga.strip().split(",")
                    codice = dati[0]
                    if codice.startswith("ES"):
                        nuovoespositore = Espositore(codice, dati[1], dati[2])
                        self.listaespositori.append(nuovoespositore)
                    elif codice.startswith("ST"):
                        if len(dati) == 4:
                             nuovostand = Stand(codice, dati[1], dati[2], dati[3])
                        elif len(dati) == 5:
                            if dati[4].isdigit():
                                nuovostand = StandPrese(codice, dati[1], dati[2], dati[3], dati[4])
                            else:
                                nuovostand = StandPremium(codice, dati[1], dati[2], dati[3], dati[4])
                        self.listastand.append(nuovostand)
        except FileNotFoundError:
            raise FileNotFoundError(f"File {file_path} non trovato")

    def assegna_stand_a_espositore(self, codice_stand, codice_espositore):
        standtrovato = None
        espositoretrovato = None
        for stand in self.listastand:
            if stand.codice == codice_stand:
                standtrovato = stand
                break
        for espositore in self.listaespositori:
            if espositore.codice == codice_espositore:
                espositoretrovato = espositore
                break
        if standtrovato == None or espositoretrovato == None:
            raise ValueError("errore, stand o espositore non presenti nel sistema")
        if standtrovato.assegnato != None:
            raise ValueError(f"Errore: Lo stand {codice_stand} è già occupato.")
        if espositoretrovato.assegnato != None:
            raise ValueError(f"Errore: L' espositore {codice_espositore} ha già uno stand")
        standtrovato.assegnato = espositoretrovato
        espositoretrovato.assegnato = standtrovato

    def elenca_espositori(self):
        for espositore in self.listaespositori:
            print(espositore)

    def stand_ordinati_per_prezzo(self):
        standordinati = sorted(self.listastand)
        return standordinati

















    """Aggiungere setter e getter se necessari"""
    # TODO

    def carica_file_dati(self, file_path):
        """Carica i dati (stand ed espositori) dal file"""
        # TODO

    def assegna_stand_a_espositore(self, codice_stand, codice_espositore):
        """Associa uno stand a un espositore"""
        # TODO

    def elenca_espositori(self):
        """Stampa l'elenco degli espositori mostrando, per ognuno, lo stand a cui è associato, quando applicabile """
        # TODO

    def stand_ordinati_per_prezzo(self):
        """Restituisce la lista ordinata degli stand in base al prezzo"""
        # TODO
