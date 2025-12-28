from faker import Faker

fake = Faker('pl_PL')

class BaseContact:
    def __init__(self, imie, nazwisko, telefon, email):
        """Inicjalizacja podstawowych danych kontaktowych."""
        self.imie = imie
        self.nazwisko = nazwisko
        self.telefon = telefon
        self.email = email
            
    def contact(self):
        """Metoda wybiera numer prywatny."""
        print(f"Wybieram numer {self.telefon} i dzwonię do {self.imie} {self.nazwisko}")

    def __str__(self):
        return f"{self.imie} {self.nazwisko}, Tel: {self.telefon}, Email: {self.email}" 

    @property
    def label_length(self):
        """Dynamiczny atrybut zwracający długość imienia i nazwiska."""
        return len(f"{self.imie} {self.nazwisko}")

class BusinessContact(BaseContact):
    def __init__(self, imie, nazwisko, telefon, email, stanowisko, firma, telefon_sluzbowy):
        """Inicjalizacja danych biznesowych z wykorzystaniem dziedziczenia.
        dziedziczy podstawowe dane z BaseContact i dodaje dane firmowe:
        stanowisko, firma, telefon_sluzbowy.
        """
        super().__init__(imie, nazwisko, telefon, email)
        self.stanowisko = stanowisko
        self.firma = firma
        self.telefon_sluzbowy = telefon_sluzbowy

    def contact(self):
        """Metoda wybiera numer służbowy."""
        print(f"Wybieram numer służbowy {self.telefon_sluzbowy} i dzwonię do {self.imie} {self.nazwisko}")

    def __str__(self):
        """
        Nadpisuje metodę __str__ dla wizytówki biznesowej.
        Wyświetla dane prywatne oraz dodatkowo firmę i stanowisko.
        """
        return (f"{self.imie} {self.nazwisko}, Tel prywatny: {self.telefon}, Email: {self.email}, "
                f"Stanowisko: {self.stanowisko}, Firma: {self.firma}, Tel służbowy: {self.telefon_sluzbowy}")

# --- UNIWERSALNA FUNKCJA ZGODNA Z WYMOGAMI MENTORA ---
def create_contacts(contact_type, quantity):
    """Tworzy kontakty na podstawie typu. """
    
    base_list = []
    business_list = []
    
    for _ in range(quantity):
        # Generowanie wspólnych danych osobowych
        imie = fake.first_name()
        nazwisko = fake.last_name()
        telefon = fake.phone_number()
        email = fake.email()
        
        # Tworzenie obiektu bazowego
        base_card = BaseContact(imie, nazwisko, telefon, email)
        
        # Tworzenie obiektu biznesowego (te same dane osobowe + firmowe)
        business_card = BusinessContact(
            imie, nazwisko, telefon, email, 
            fake.job(), fake.company(), fake.phone_number()
        )
        
        base_list.append(base_card)
        business_list.append(business_card)
    
    # Zwracanie wyniku w zależności od parametru
    if contact_type == 'base':
        return base_list
    elif contact_type == 'business':
        return business_list
    elif contact_type == 'linked':
        return base_list, business_list

# --- GŁÓWNY BLOK PROGRAMU ---
if __name__ == "__main__":
    
    # Wywołujemy funkcję RAZ, aby dane były spójne (tryb 'linked')
    base_contacts, business_contacts = create_contacts('linked', 5)

    print("\n--- Wizytówki - dane podstawowe: ---\n")
    for contact in base_contacts:
        print(contact)
        contact.contact()
        print(f"Długość etykiety: {contact.label_length}")
        print("-" * 20)

    print("\n--- Wizytówki - dane biznesowe: ---\n")
    for contact in business_contacts:
        print(contact)
        contact.contact()
        print(f"Długość etykiety: {contact.label_length}")
        print("-" * 20)