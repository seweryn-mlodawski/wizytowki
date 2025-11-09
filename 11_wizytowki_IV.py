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
    def __str__(self):
        return f"{self.imie} {self.nazwisko}, Tel: {self.telefon}, Email: {self.email}"
        
    @property
    def label_length(self):
        return len(f"{self.imie} {self.nazwisko}")

class BusinessContact(BaseContact):
    def __init__(self, imie, nazwisko, telefon, email, stanowisko, firma, telefon_sluzbowy):
        super().__init__(imie, nazwisko, telefon, email)
        self.stanowisko = stanowisko
        self.firma = firma
        self.telefon_sluzbowy = telefon_sluzbowy
             
    def contact(self):
        print(f"Wybieram numer: {self.telefon_sluzbowy} i dzwonię do: {self.imie} {self.nazwisko} z firmy {self.firma} na stanowisku {self.stanowisko}")

    def __str__(self):
        return (f"{self.imie} {self.nazwisko}, Tel prywatny: {self.telefon}, Email: {self.email}, "
                f"Stanowisko: {self.stanowisko}, Firma: {self.firma}, Tel służbowy: {self.telefon_sluzbowy}")

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
            biz_Cards.append(BusinessContact(imie, nazwisko, telefon, email, stanowisko, firma, telefon_sluzbowy))
    return biz_Cards

base_contacts = create_bizCards('base', 5)
business_contacts = create_bizCards('business', 5)

all_contacts = base_contacts + business_contacts

for contact in all_contacts:
    print(contact)
    contact.contact()
    print(f"Długość etykiety: {contact.label_length}")
    print()
