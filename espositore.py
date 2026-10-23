
class Espositore:
    def __init__(self, codice, nome, cognome):
        self.__codice = codice
        self.__nome = nome
        self.__cognome = cognome

        self.__stand = None


    @property
    def codice(self):
        return self.__codice
    @codice.setter
    def codice(self, codice):
        self.__codice = codice

    @property
    def nome(self):
        return self.__nome
    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @property
    def cognome(self):
        return self.__cognome
    @cognome.setter
    def cognome(self, cognome):
        self.__cognome = cognome

    def __str__(self):
        return f"{self.codice}, {self.nome},  {self.cognome}"

    def __eq__(self, other):
        return self.codice == other.codice

    """
    # Se si vogliono ordinare gli espositori, es. per cognome, nome e codice 
    def __lt__(self, other):
        if self.cognome==other.cognome:
            if self.nome==other.nome:
                return self.codice < other.codice
            else:
                return self.nome < other.nome
        else:
                return self.cognome < other.cognome
    """

    """
    def __hash__(self):
        return hash(self.codice)
    """

    def descrivi_espositore(self):
        return f"{self.codice}: {self.nome} {self.cognome}"

    def descrivi_stand_assegnato(self):
        if self.__stand is None:
            return "Non assegnato ad alcuno stand"
        else:
            return f"Assegnato allo stand {self.__stand.codice}"

    def assegna_stand(self, stand):
        if self.__stand is not None: # Se già assegnato
            if self.__stand == stand:
                raise ValueError(f"L'espositore {self.codice} è già assegnato a questo stand!")
            else:
                raise ValueError(f"L'espositore {self.codice} è già assegnato ad uno stand!")

        self.__stand = stand