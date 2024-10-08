# Kalendarz Wydarzeń

## Opis

Aplikacja kalendarza wydarzeń stworzona w Django, która umożliwia przeglądanie wydarzeń, ich szczegółowe wyświetlanie oraz interakcję z interfejsem kalendarza.

## Wymagania

- Python 3.12 lub nowszy
- Django 5.1 lub nowszy
- SQLite (domyślnie)
- Pakiety Python zdefiniowane w `requirements.txt`

## Instalacja

### 1. Klonowanie repozytorium

Aby sklonować repozytorium, użyj następującej komendy:

```bash
git clone https://github.com/uhnajs/Kalendarz-wydarzen.git
cd Kalendarz-wydarzen
```

### 2. Utworzenie wirtualnego środowiska

Zaleca się utworzenie wirtualnego środowiska dla projektu:

```bash
python -m venv .venv
```

### 3. Aktywacja wirtualnego środowiska

- **Windows**:

  ```bash
  .venv\Scripts\activate
  ```

- **macOS / Linux**:

  ```bash
  source .venv/bin/activate
  ```

### 4. Instalacja zależności

Zainstaluj wszystkie wymagane pakiety:

```bash
pip install -r requirements.txt
```

### 5. Wykonanie migracji bazy danych

Przygotuj bazę danych:

```bash
cd .\calendar_project\
python manage.py migrate
```

### 6. Uruchomienie serwera deweloperskiego

Uruchom aplikację Django:

```bash
python manage.py runserver
```

Aplikacja powinna być dostępna pod adresem: `http://127.0.0.1:8000/`. 

## Testowanie

Aby uruchomić testy aplikacji, skorzystaj z poniższej komendy:

```bash
python manage.py test events.tests
```

Testy obejmują:
- **Widoki (Views)** - Sprawdzają poprawność wyświetlania stron oraz połączenia z API.
- **Modele (Models)** - Sprawdzają poprawność działania modeli bazy danych.

Uruchomienie testów pozwala upewnić się, że wszystkie kluczowe funkcje aplikacji działają poprawnie.

## Użycie

1. Po uruchomieniu aplikacji zobaczysz kalendarz, na którym wyświetlane są wydarzenia.
2. Kliknij na konkretne wydarzenie, aby zobaczyć jego szczegóły.
3. Wydarzenia są pobierane z zewnętrznego API.

## Wsparcie

W przypadku pytań lub problemów, proszę o kontakt.
