from faker import Faker

# Inicjalizacja biblioteki Faker dla polskiej lokalizacji
fake = Faker('pl_PL')

class BaseContact:
    def __init__(self, imie, nazwisko, telefon, email):
        """Podstawowe dane kontaktowe."""
        self.imie = imie
        self.nazwisko = nazwisko
        self.telefon = telefon
        self.email = email
            
    def contact(self):
        """Dzwoni na numer prywatny."""
        print(f"Wybieram numer {self.telefon} i dzwonię do {self.imie} {self.nazwisko}")

    @property
    def label_length(self):
        """Zwraca długość imienia i nazwiska (razem ze spacją)."""
        return len(f"{self.imie} {self.nazwisko}")

class BusinessContact(BaseContact):
    def __init__(self, imie, nazwisko, telefon, email, stanowisko, firma, telefon_sluzbowy):
        """Rozszerzenie o dane biznesowe."""
        super().__init__(imie, nazwisko, telefon, email)
        self.stanowisko = stanowisko
        self.firma = firma
        self.telefon_sluzbowy = telefon_sluzbowy

    def contact(self):
        """Dzwoni na numer służbowy."""
        print(f"Wybieram numer {self.telefon_sluzbowy} i dzwonię do {self.imie} {self.nazwisko}")

def create_contacts(contact_type, quantity):
    """
    Tworzy losowe wizytówki zgodnie z wymaganiami zadania.
    Argumenty: contact_type ('base' lub 'business'), quantity (liczba wizytówek).
    """
    contacts = []
    
    for _ in range(quantity):
        # Dane wspólne dla obu typów
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

# --- Blok główny programu ---
if __name__ == "__main__":
    # Przykład użycia funkcji zgodnie z wymaganiami
    print("--- GENEROWANIE WIZYTÓWEK ---")
    
    # Tworzenie wizytówek podstawowych
    base_cards = create_contacts('base', 2)
    for card in base_cards:
        card.contact()
        print(f"Długość etykiety: {card.label_length}\n")

    # Tworzenie wizytówek biznesowych
    business_cards = create_contacts('business', 2)
    for card in business_cards:
        card.contact()
        print(f"Długość etykiety: {card.label_length}\n")