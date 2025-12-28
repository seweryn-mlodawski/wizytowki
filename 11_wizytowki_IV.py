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
        Metoda wyświetlająca komunikat: 
        'Wybieram numer +48... i dzwonię do Jan Kowalski'
        Dla klasy bazowej wybiera numer prywatny.
        """
        print(f"Wybieram numer {self.telefon} i dzwonię do {self.imie} {self.nazwisko}")

    @property
    def label_length(self):
        """Zwraca długość imienia i nazwiska (w tym spacja)."""
        return len(f"{self.imie} {self.nazwisko}")

class BusinessContact(BaseContact):
    def __init__(self, imie, nazwisko, telefon, email, stanowisko, firma, telefon_sluzbowy):
        """Inicjalizacja rozszerzonych danych biznesowych."""
        super().__init__(imie, nazwisko, telefon, email)
        self.stanowisko = stanowisko
        self.firma = firma
        self.telefon_sluzbowy = telefon_sluzbowy

    def contact(self):
        """
        Dla klasy biznesowej wybiera numer służbowy.
        """
        print(f"Wybieram numer {self.telefon_sluzbowy} i dzwonię do {self.imie} {self.nazwisko}")


def create_contacts(contact_type, quantity):
    """
    Funkcja tworząca losowe wizytówki.
    Parametry:
    - contact_type: rodzaj wizytówki ('base' lub 'business')
    - quantity: ilość wizytówek do wygenerowania
    """
    contacts = []
    
    for _ in range(quantity):
        # Generowanie danych wspólnych
        imie = fake.first_name()
        nazwisko = fake.last_name()
        telefon = fake.phone_number()
        email = fake.email()

        if contact_type == 'base':
            contacts.append(BaseContact(imie, nazwisko, telefon, email))
            
        elif contact_type == 'business':
            # Generowanie danych tylko dla biznesu
            stanowisko = fake.job()
            firma = fake.company()
            telefon_sluzbowy = fake.phone_number()
            contacts.append(BusinessContact(imie, nazwisko, telefon, email, stanowisko, firma, telefon_sluzbowy))
            
    return contacts

# --- Blok uruchomieniowy  ---

if __name__ == "__main__":
    # Testowanie generowania wizytówek base
    print("--- Wizytówki Podstawowe ---")
    base_cards = create_contacts('base', 3)
    for card in base_cards:
        card.contact()
        print(f"Długość etykiety: {card.label_length}")
        print("-" * 10)

    # Testowanie generowania wizytówek business
    print("\n--- Wizytówki Biznesowe ---")
    business_cards = create_contacts('business', 3)
    for card in business_cards:
        card.contact()
        print(f"Długość etykiety: {card.label_length}")
        print("-" * 10)