from faker import Faker  # Import biblioteki do generowania losowych danych

fake = Faker('pl_PL')  # Ustawienie polskiej lokalizacji dla generatora danych

class BaseContact:
    def __init__(self, imie, nazwisko, telefon, email):
        """Inicjalizacja podstawowych danych kontaktowych."""
        self.imie = imie
        self.nazwisko = nazwisko
        self.telefon = telefon
        self.email = email
            
    def contact(self):
        """
        Metoda wyświetlająca komunikat o dzwonieniu.
        Metoda wybiera numer prywatny.
        """
        print(f"Wybieram numer {self.telefon} i dzwonię do {self.imie} {self.nazwisko}")

    def __str__(self):
        return f"{self.imie} {self.nazwisko}, Tel: {self.telefon}, Email: {self.email}" 

    @property
    def label_length(self):
        """
        Dynamiczny atrybut, oblicza długość imienia i nazwiska.
        Zwraca długość imienia i nazwiska (w tym spacja).
        """
        return len(f"{self.imie} {self.nazwisko}")

class BusinessContact(BaseContact):
    def __init__(self, imie, nazwisko, telefon, email, stanowisko, firma, telefon_sluzbowy):
        """
        Inicjalizacja danych biznesowych.
        >>Tu mam dziedziczenie z BaseContact.<<
        ️Dodatkowo dodaję stanowisko, firmę i telefon służbowy.        
        """
        super().__init__(imie, nazwisko, telefon, email) # Wywołanie konstruktora klasy bazowej
        self.stanowisko = stanowisko
        self.firma = firma
        self.telefon_sluzbowy = telefon_sluzbowy

    def contact(self):
        """
        Nadpisuje metodę contact dla wizytówki firmowej.
        Tutaj wybiera numer służbowy.
        """
        print(f"Wybieram numer {self.telefon_sluzbowy} i dzwonię do {self.imie} {self.nazwisko}")

    def __str__(self):
        """
        Nadpisuje metodę __str__ dla wizytówki biznesowej.
        Wyświetla dane prywatne oraz dodatkowo firmę i stanowisko.
        Nadpisane __str__ w klasie pochodnej, aby reprezentacja tekstowa obiektu odzwierciedlała
        rozszerzony zestaw danych (stanowisko, firma), który posiada BusinessContact, a którego nie posiada klasa bazowa.
        """
        return (f"{self.imie} {self.nazwisko}, Tel prywatny: {self.telefon}, Email: {self.email}, "
                f"Stanowisko: {self.stanowisko}, Firma: {self.firma}, Tel służbowy: {self.telefon_sluzbowy}")

def create_contacts(contact_type, quantity):
    """
    Tworzy listę losowych wizytówek zadanego typu.
    Parametry:
    - contact_type: 'base' (prywatna) lub 'business' (firmowa)
    - quantity: ile wizytówek wygenerować
    """
    contacts = []
    
    for _ in range(quantity):
        # 1. Generuje dane wspólne dla każdego człowieka
        imie = fake.first_name()
        nazwisko = fake.last_name()
        telefon = fake.phone_number()
        email = fake.email()

        # 2. Sprawdza, o jaki typ wizytówki prosił użytkownik
        if contact_type == 'base':
            # Tworzy zwykłą wizytówkę
            contacts.append(BaseContact(imie, nazwisko, telefon, email))
            
        elif contact_type == 'business':
            # Dla biznesowej dolosowuje dodatkowe dane (praca)
            stanowisko = fake.job()
            firma = fake.company()
            telefon_sluzbowy = fake.phone_number()
            # Tworzy wizytówkę biznesową przekazując komplet danych
            contacts.append(BusinessContact(imie, nazwisko, telefon, email, stanowisko, firma, telefon_sluzbowy))
            
    return contacts

# Ten blok sprawia, że kod wykona się tylko przy bezpośrednim uruchomieniu pliku,
# a nie przy importowaniu go w innym miejscu.

if __name__ == "__main__":
    
    # 1. Test wizytówek podstawowych
    print("\n--- Wizytówki - dane podstawowe: ---\n")
    base_contacts = create_contacts('base', 5) # Generujemy 5 sztuk
    
    for contact in base_contacts:
        print(contact)       # Wywołuje metodę __str__ dla podstawowej wizytówki
        contact.contact()    # Wywołuje metodę contact (Wybieram numer...)
        print(f"Długość etykiety: {contact.label_length}")
        print("-" * 20)

    # 2. Test wizytówek biznesowych
    print("\n--- Wizytówki - dane biznesowe: ---\n")
    business_contacts = create_contacts('business', 5) # Generujemy 5 sztuk
    
    for contact in business_contacts:
        print(contact)       # Wywołuje __str__ dla biznesu (pełne dane + firma)
        contact.contact()    # Wywołuje contact dla biznesu (numer służbowy!)
        print(f"Długość etykiety: {contact.label_length}")
        print("-" * 20)