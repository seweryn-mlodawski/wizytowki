from faker import Faker  # import biblioteki Faker

fake = Faker('pl_PL')

def create_bizCards(contact_type, quantity):
    biz_Cards = []
    for _ in range(quantity):
        imie = fake.first_name()
        nazwisko = fake.last_name()
        telefon = fake.phone_number()
        email = fake.email()

        if contact_type == 'base':
            biz_Cards.append(BaseContact(imie, nazwisko, telefon, email))
        elif contact_type == 'business':
            stanowisko = fake.job()
            firma = fake.company()
            telefon_sluzbowy = fake.phone_number()
            
            

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

#    @property 
#    def label_length(self):
#        return len(f"{self.imie} {self.nazwisko}")

















