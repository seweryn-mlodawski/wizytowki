from faker import Faker  # import biblioteki Faker

fake = Faker('pl_PL')

class BaseContact:
    def __init__(self, imie, nazwisko, telefon, email): # inicjalizacja podstawowych danych kontaktowych
        self.imie = imie
        self.nazwisko = nazwisko
        self.telefon = telefon
        self.email = email
            
    def contact(self): # metoda do kontaktowania się z osobą
        print(f"Wybieram numer: {self.telefon} i dzwonię do: {self.imie} {self.nazwisko}")
    def __str__(self): # metoda do reprezentacji obiektu jako string
        return f"{self.imie} {self.nazwisko}, Tel: {self.telefon}, Email: {self.email}" 
        
    @property # dynamiczny atrybut zwracający długość etykiety
    def label_length(self): 
        return len(f"{self.imie} {self.nazwisko}") # długość etykiety to suma znaków imienia i nazwiska

    
class BusinessContact(BaseContact): # klasa dziedzicząca po BaseContact z dodatkowymi danymi biznesowymi
    def __init__(self, imie, nazwisko, telefon, email, stanowisko, firma, telefon_sluzbowy):
        super().__init__(imie, nazwisko, telefon, email) # wywołanie konstruktora klasy bazowej
        # dodatkowe atrybuty dla danych biznesowych
        self.stanowisko = stanowisko 
        self.firma = firma
        self.telefon_sluzbowy = telefon_sluzbowy

    def contact(self):
        print(f"Wybieram numer służbowy: {self.telefon_sluzbowy} i dzwonię do: {self.imie} {self.nazwisko}, z firmy {self.firma}, stanowisko - {self.stanowisko}")

    def __str__(self):
        return (f"{self.imie} {self.nazwisko}, Tel prywatny: {self.telefon}, Email: {self.email}, "
                f"Stanowisko: {self.stanowisko}, Firma: {self.firma}, Tel służbowy: {self.telefon_sluzbowy}")

def create_contacts(contact_type, quantity):
    contacts = []
    for _ in range(quantity):
        imie = fake.first_name()
        nazwisko = fake.last_name()
        telefon = fake.phone_number()
        email = fake.email()

        if contact_type == 'base':
            contacts.append(BaseContact(imie, nazwisko, telefon, email))
        elif contact_type == 'business':
            stanowisko = fake.job()
            firma = fake.company()
            telefon_sluzbowy = fake.phone_number()
            contacts.append(BusinessContact(imie, nazwisko, telefon, email, stanowisko, firma, telefon_sluzbowy))
    return contacts

base_contacts = create_contacts('base', 5) # tworzenie 5 wizytówek podstawowych
business_contacts = create_contacts('business', 5) # tworzenie 5 wizytówek biznesowych

# pętla wyświetlająca wszystkie wizytówki
print("\nWizytówki - dane podstawowe:\n")
for contact in base_contacts:
    print(contact)
    contact.contact()
    print(f"Długość etykiety: {contact.label_length}")
    print()
print("\nWizytówki - dane biznesowe:\n")
for contact in business_contacts:
    print(contact)
    contact.contact()
    print(f"Długość etykiety: {contact.label_length}")
    print()

#dla każdej z list dane generowane są osobno i wyświetlane osobno - można to poprawić aby po wygenerowaniu były powtarzane w opcji wizytówek biznesowych
