from faker import Faker  # import biblioteki Faker

fake = Faker('pl_PL')

class BizCard:
    def __init__(self):
        full_name = fake.name().split() # generowanie pełnego imienia i nazwiska
        self.imie = full_name[0] # pierwsza część jako imię
        self.nazwisko = full_name[-1] # ostatnia część jako nazwisko
        self.email = fake.email() # generowanie e-maila

    def __str__(self): # metoda do reprezentacji obiektu jako string
        return f"{self.imie} {self.nazwisko}, {self.email}" 

    def contact(self):
        # Punkt 1 ćwiczenia: kontaktowanie się z osobą
        print(f"Kontaktuję się z {self.imie} {self.nazwisko} pod adresem email: {self.email}") 

    @property 
    def label_length(self):
        # Punkt 2 ćwiczenia: dynamiczny atrybut zwracający długość etykiety
        return len(f"{self.imie} {self.nazwisko}") 

# Tworzenie listy wizytówek
business_cards = [BizCard() for _ in range(5)]  # tworzenie 5 wizytówek

print("Wizytówki:")
for wiz in business_cards: 
    print(wiz) 
    wiz.contact() 
    print(f"Długość etykiety: {wiz.label_length}")
    print()

print("\nSortowanie według imienia:")
for wiz in sorted(business_cards, key=lambda x: x.imie): # sortowanie według imienia 
    print(wiz)

print("\nSortowanie według nazwiska:")
for wiz in sorted(business_cards, key=lambda x: x.nazwisko):
    print(wiz)

print("\nSortowanie według e-maila:")
for wiz in sorted(business_cards, key=lambda x: x.email):
    print(wiz)