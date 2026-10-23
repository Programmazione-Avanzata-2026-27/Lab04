import csv
from operator import attrgetter

from espositore import Espositore
from stand import *   # Stand, StandPremium, StandPreseExtra


class LingottoFiere:
    def __init__(self, nome):
        """Inizializza gli attributi e le strutture dati"""
        self.__nome = nome

        self.dizionario_stand = {}
        self.dizionario_espositori = {}

    """Aggiungere setter e getter se necessari"""

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, valore):
        self.__nome = valore

    def carica_file_dati(self, file_path):
        """Carica i dati (stand ed espositori) dal file"""

        file = open(file_path, "r")
        lettore = csv.reader(file)
        for riga in lettore:
            # Qui ho una riga nel formato ST01... oppure ES02 ...
            codice = riga[0] # Prendo il primo campo, che contiene il codice
            if codice.startswith("ST"): #Stand

                if codice in self.dizionario_stand:
                    raise ValueError(f"Codice stand {codice} duplicato!")

                if len(riga)==4 or len(riga)==5: #Riga corretta
                    if len(riga)==4: # Stand "normale"
                        # Estraggo gli altri campi
                        superficie = int(riga[1])
                        padiglione= int(riga[2])
                        prezzo_base = float(riga[3])

                        # Creo lo stand con quei campi come attributi
                        stand = Stand(codice, superficie, padiglione, prezzo_base)
                        # Inserisco lo stand appena creato nel dizionario degli stand
                        self.dizionario_stand[codice] = stand

                    else: # StandPreseExtra oppure StandPremium
                        campo_extra = riga[4] # Se numero è uno StandPreseExtra
                        try:
                            num_prese = float(campo_extra) # Se la conversione riesce, StandPreseExtra
                            stand = StandPreseExtra(codice, superficie, padiglione, prezzo_base, num_prese)
                            self.dizionario_stand[codice] = stand

                        except ValueError: # Se eccezione, StandPremium
                            posizione = campo_extra
                            stand = StandPremium(codice, superficie, padiglione, prezzo_base, posizione)
                            self.dizionario_stand[codice] = stand

                else: #Riga in formato errato
                    raise ValueError(f"Riga in formato errato!")

            elif codice.startswith("ES"): #Espositore

                if len(riga)==3:
                    nome = riga[1]
                    cognome = riga[2]
                    if codice in self.dizionario_espositori:
                        raise ValueError(f"Codice espositore {codice} duplicato!")
                    else:
                        espositore = Espositore(codice, nome, cognome)
                        self.dizionario_espositori[codice] = espositore
                else:
                    raise ValueError(f"Riga in formato errato!")

            else: #Nè uno né l'altro
                raise ValueError(f"Riga in formato errato!")


    def assegna_stand_a_espositore(self, codice_stand, codice_espositore):
        """Associa uno stand a un espositore"""

        if codice_stand not in self.dizionario_stand:
            raise ValueError(f"Codice stand {codice_stand} inesistente!")
        if codice_espositore not in self.dizionario_espositori:
            raise ValueError(f"Codice espositore {codice_espositore} inesistente!")

        stand = self.dizionario_stand[codice_stand]
        espositore = self.dizionario_espositori[codice_espositore]

        # Non accedo direttamente all'attributo __stand di espositore con espositore.__stand = stand
        # Piuttosto, più correttamente, DELEGO all'espositore il compito di assegnare lo stand
        espositore.assegna_stand(stand) # Così posso, es., effettuare eventuali controlli di errore
        stand.assegna_espositore(espositore) # Idem per assegnare l'espositore allo stand

    def elenca_espositori(self):
        """Stampa l'elenco degli espositori mostrando, per ognuno, lo stand a cui è associato, quando applicabile """
        """Stampa l'elenco degli espositori mostrando, per ognuno, lo stand a cui è associato, quando applicabile """
        # lista_espositori = sorted(self.dizionario_espositori.values())
        lista_espositori = self.dizionario_espositori.values()
        for espositore in lista_espositori:
            print(espositore.descrivi_espositore()+" - "+espositore.descrivi_stand_assegnato())

    def stand_ordinati_per_prezzo(self):
        """Restituisce la lista ordinata degli stand in base al prezzo"""
        lista_ordinata = sorted(self.dizionario_stand.values()) #key=attrgetter("prezzo_base")
        return lista_ordinata



