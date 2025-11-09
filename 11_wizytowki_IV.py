from faker import Faker  # import biblioteki Faker

fake = Faker('pl_PL')

class BaseContact:
    def __init__(self, imie, nazwisko, telefon, email):
        self.imie = imie
        self.nazwisko = nazwisko
        self.telefon = telefon
        self.email = email
    
    def contact(self):
        print(f"Wybieram numer: {self.telefon} i dzwonię do: {self.imie} {self.nazwisko}")
        

    @property
    def label_length(self):
        return len(f"{self.imie} {self.nazwisko}")


class BussinessContact(BaseContact):
    def __init__(self, imie, nazwisko, telefon, email, stanowisko, firma, telefon_sluzbowy):
        super().__init__(imie, nazwisko, telefon, email)
        self.stanowisko = stanowisko
        self.firma = firma
        self.telefon_sluzbowy = telefon_sluzbowy
             
    def contact(self):
        print(f"Wybieram numer: {self.telefon_sluzbowy} i dzwonię do: {self.imie} {self.nazwisko} z firmy {self.firma} na stanowisku {self.stanowisko}") 

    @property 
    def label_length(self):
        return len(f"{self.imie} {self.nazwisko}")

















