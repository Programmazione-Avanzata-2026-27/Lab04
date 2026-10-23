
class Stand:
    def __init__(self, codice, superficie, padiglione, prezzo_base):
        self.__codice = codice
        self.__superficie = superficie
        self.__padiglione =  padiglione
        self.__prezzo_base = prezzo_base

        self.__espositore = None

    @property
    def codice(self):
        return self.__codice
    @codice.setter
    def codice(self, valore):
        self.__codice = valore

    @property
    def superficie(self):
        return self.__superficie
    @superficie.setter
    def superficie(self, valore):
        self.__superficie = valore

    @property
    def padiglione(self):
        return self.__padiglione
    @padiglione.setter
    def padiglione(self, valore):
        self.__padiglione = valore

    @property
    def prezzo_base(self):
        return self.__prezzo_base
    @prezzo_base.setter
    def prezzo_base(self, valore):
        self.__prezzo_base = valore

    def __str__(self):
        return f"{self.codice} {self.superficie} {self.padiglione} {self.prezzo_base}"

    def __lt__(self, other):
        return self.prezzo_finale() < other.prezzo_finale()

    def __eq__(self, other):
        return self.codice == other.codice

    """
    def __hash__(self):
        return hash(self.codice)
    """

    def prezzo_finale(self):
        return self.prezzo_base

    def stato(self):
        if self.__espositore is None:
            return "Disponibile"
        else:
            return "Non disponibile"

    # Metodo invocato per stampare lo stand come suggerito, e con prezzo finale
    def descrivi_stand(self):
        if isinstance(self, StandPremium):
            return f"{self.codice}: Premium | {self.superficie} mq - Padiglione {self.padiglione} - Prezzo {self.prezzo_finale():.2f}€"
        elif isinstance(self, StandPreseExtra):
            return f"{self.codice}: Con Prese | {self.superficie} mq - Padiglione {self.padiglione} - Prezzo {self.prezzo_finale():.2f}€"
        elif isinstance(self, Stand):
            return f"{self.codice}: Standard | {self.superficie} mq - Padiglione {self.padiglione} - Prezzo {self.prezzo_finale():.2f}€ - {self.stato()}"




    def assegna_espositore(self, espositore):
        if self.__espositore is not None: # Già assegnato
            if self.__espositore == espositore:
                raise ValueError(f"Lo stand {self.codice} è già assegnato a questo espositore!")
            else:
                raise ValueError(f"Lo stand {self.codice} è già assegnato ad un espositore!")

        self.__espositore = espositore



class StandPreseExtra(Stand):
    def __init__(self, codice, superficie, padiglione, prezzo_base, num_prese):
        super().__init__(codice, superficie, padiglione, prezzo_base)
        self.__num_prese = num_prese

    @property
    def num_prese(self):
        return self.__num_prese
    @num_prese.setter
    def num_prese(self, valore):
        self.__num_prese = valore

    def __str__(self):
        return f"{super().__str__()}, {self.num_prese}"

    def prezzo_finale(self):
        return self.prezzo_base * (1 + 0.07 * self.num_prese)

    def descrivi_stand(self):
        return f"{super().descrivi_stand()} - Prese aggiuntive: {self.num_prese} - {self.stato()}"


class StandPremium(Stand):
    def __init__(self, codice, superficie, padiglione, prezzo_base, posizione):
        super().__init__(codice, superficie, padiglione, prezzo_base)
        self.__posizione = posizione

    @property
    def posizione(self):
        return self.__posizione

    @posizione.setter
    def posizione(self, valore):
        self.__posizione = valore

    def __str__(self):
        return f"{super().__str__()}, {self.posizione}"

    def descrivi_stand(self):
        return f"{super().descrivi_stand()} - Posizione: {self.posizione} - {self.stato()}"

    def prezzo_finale(self):
        return self.prezzo_base * 1.30



# Codice di debug nella classe/nel modulo
# Quando importerò questo modulo, questo codice non verrà eseguito
if __name__ == "__main__":
    st1 = Stand("ST1", 16, 1, 150.0)
    print(st1)