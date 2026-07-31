# CS50 Portfolio 2026

[![Harvard CS50](https://img.shields.io/badge/Harvard-CS50-A51C30?style=flat-square)](https://cs50.harvard.edu/)
[![GitHub last commit](https://img.shields.io/github/last-commit/p-keminer/cs50x-26?style=flat-square)](https://github.com/p-keminer/cs50x-26/commits/main)
[![GitHub repo size](https://img.shields.io/github/repo-size/p-keminer/cs50x-26?style=flat-square)](https://github.com/p-keminer/cs50x-26)

Meine Lösungen und Projekte aus dem Harvard-CS50-Umfeld. Das Repository umfasst Aufgaben aus **CS50x**, **CS50P**, **CS50 SQL**, **CS50 AI** und **CS50 Web** sowie drei eigenständige Abschlussprojekte.

> [!IMPORTANT]
> Dieses Repository dokumentiert meinen persönlichen Bearbeitungsstand. Wenn du selbst an einem CS50-Kurs teilnimmst, versuche die Aufgaben zuerst eigenständig zu lösen und beachte die [CS50 Academic Honesty Policy](https://cs50.harvard.edu/x/honesty/).

> [!NOTE]
> Versioniert werden Quellcode, aufgabenrelevante Datenbanken, Tests und Projektdokumentation. Zertifikate, Videos, Aufzeichnungen, persönliche Guides, Cheatsheets, Präsentationsdateien und virtuelle Umgebungen gehören nicht zum Repository.

## Abschlussprojekte

| Kurs | Projekt | Schwerpunkt | Ordner |
|---|---|---|---|
| **CS50x** | **Local Port Scanner & Report Generator** | Netzwerkprogrammierung, Eingabevalidierung, Service-Erkennung und Report-Export | [`projectx`](./projectx) |
| **CS50P** | **Lights Out** | Modulares Terminalspiel mit mehreren Schwierigkeitsgraden und Tests | [`projectp/project`](./projectp/project) |
| **CS50 SQL** | **Network Scanning Ecosystem** | Relationales Datenmodell für Netzwerk- und Portscan-Ergebnisse | [`project`](./project) |

### CS50x — Local Port Scanner & Report Generator

Eine Python-CLI zum kontrollierten Prüfen autorisierter Hosts und Portbereiche.

- TCP- und ausgewählte UDP-Prüfungen
- Validierung von Hosts, Ports und Timeouts
- Banner- und HTTP-Header-Erkennung
- Service-Klassifizierung mit Herkunft und Konfidenz
- Ausgabe als menschenlesbarer TXT- und maschinenlesbarer CSV-Report
- ausschließlich für eigene oder ausdrücklich autorisierte Systeme vorgesehen

```bash
cd projectx
python project.py
```

### CS50P — Lights Out

Ein vollständig im Terminal spielbares Logikspiel in Python.

- frei wählbare Spielfeldgröße von 3×3 bis 12×12
- Schwierigkeitsgrade Easy, Normal und Hard
- garantiert lösbare, aus gültigen Zügen erzeugte Spielfelder
- robuste Eingabeverarbeitung sowie Help-, Restart- und Quit-Kommandos
- reproduzierbare Tests mit optionalem Seed

```bash
cd projectp/project
python project.py
python -m pytest
```

### CS50 SQL — Network Scanning Ecosystem

Eine relationale SQLite-Struktur zum Speichern und Auswerten von autorisierten Netzwerk- und Portscans.

- 9 normalisierte Tabellen für Netzwerke, Hosts, Scans, Ports, Services und Header
- 2 Report-Views für kompakte Netzwerk- und Portübersichten
- 6 Trigger zur automatischen Verknüpfung und Aktualisierung von Scanergebnissen
- 20 explizite Indizes für häufig verwendete Such- und Join-Spalten sowie 4 automatisch erzeugte SQLite-Indizes
- dokumentierte Beispielabfragen und Query-Plan-Analysen

Enthalten sind unter anderem [`schema.sql`](./project/schema.sql), [`queries.sql`](./project/queries.sql), [`explain.sql`](./project/explain.sql), [`import.sql`](./project/import.sql) und das ausführliche [`DESIGN.md`](./project/DESIGN.md).

```bash
cd project
sqlite3 network_scans.db
```

Danach innerhalb der SQLite-Shell:

```sql
.read schema.sql
.read queries.sql
```

> `import.sql` erwartet zusätzliche CSV-Dateien unter `project/csvs/`. Diese Seed-Dateien sind nicht Bestandteil des Repositorys und werden zum Erzeugen einer leeren Datenbank aus `schema.sql` nicht benötigt.

## Kursübersicht

| Kurs | Inhalt | Technologien |
|---|---|---|
| [CS50x](https://cs50.harvard.edu/x/) | Informatik-Grundlagen, Algorithmen, Speicher, Datenstrukturen und Webentwicklung | C, Python, SQL, HTML, CSS, JavaScript, Flask |
| [CS50P](https://cs50.harvard.edu/python/) | Python-Grundlagen, Tests, Dateien, reguläre Ausdrücke und OOP | Python, pytest |
| [CS50 SQL](https://cs50.harvard.edu/sql/) | Relationale Modelle, Abfragen, Views, Trigger, Indizes und Skalierung | SQL, SQLite |
| [CS50 AI](https://cs50.harvard.edu/ai/) | Suche, Wissen, Wahrscheinlichkeit und Optimierung | Python |
| [CS50 Web](https://cs50.harvard.edu/web/) | Frontend, Django, Datenmodelle und Single-Page-Anwendungen | Python, Django, SQL, HTML, CSS, JavaScript |

## CS50x — Introduction to Computer Science

| Woche | Schwerpunkt | Lösungen |
|---:|---|---|
| 1 | C | [Hello](./me), [Mario (More)](./mario-more), [Cash](./cash) |
| 2 | Arrays | [Caesar](./caesar), [Readability](./readability), [Scrabble](./scrabble) |
| 3 | Algorithmen | [Plurality](./plurality), [Runoff](./runoff), [Sort](./sort) |
| 4 | Speicher | [Volume](./volume), [Filter (Less)](./filter-less), [Recover](./recover) |
| 5 | Datenstrukturen | [Inheritance](./inheritance), [Speller](./speller) |
| 6 | Python | [Sentimental Cash](./sentimental-cash), [Sentimental Mario](./sentimental-mario-more), [Sentimental Readability](./sentimental-readability), [DNA](./dna) |
| 7 | SQL | [Songs](./songs), [Movies](./movies), [Fiftyville](./fiftyville) |
| 8 | HTML, CSS & JavaScript | [Trivia](./trivia), [Homepage](./homepage) |
| 9 | Flask | [Birthdays](./birthdays), [Finance](./finance) |
| Final Project | Python & Netzwerkprogrammierung | [Local Port Scanner & Report Generator](./projectx) |

## CS50P — Introduction to Programming with Python

| Woche | Schwerpunkt | Lösungen |
|---:|---|---|
| 0 | Functions & Variables | [Hello](./hello), [Indoor Voice](./indoor), [Playback Speed](./playback), [Making Faces](./faces), [Einstein](./einstein), [Tip Calculator](./tip) |
| 1 | Conditionals | [Deep Thought](./deep), [Bank](./test_bank/bank.py), [File Extensions](./extensions), [Math Interpreter](./interpreter), [Meal Time](./meal) |
| 2 | Loops | [camelCase](./camel), [Coke Machine](./coke), [twttr](./test_twttr/twttr.py), [Vanity Plates](./test_plates/plates.py), [Nutrition Facts](./nutrition) |
| 3 | Exceptions | [Fuel Gauge](./test_fuel/fuel.py), [Felipe’s Taqueria](./taqueria), [Grocery List](./grocery), [Outdated](./outdated) |
| 4 | Libraries | [Emojize](./lines/emojize.py), [Adieu](./adieu), [Bitcoin Price Index](./bitcoin), [FIGlet](./figlet), [Guessing Game](./game), [Little Professor](./professor) |
| 5 | Unit Tests | [Test twttr](./test_twttr), [Test Bank](./test_bank), [Test Vanity Plates](./test_plates), [Test Fuel Gauge](./test_fuel) |
| 6 | File I/O | [Lines of Code](./lines/lines.py), [Pizza Py](./pizza), [Scourgify](./scourgify), [CS50 P-Shirt](./shirt) |
| 7 | Regular Expressions | [NUMB3RS](./numb3rs), [Watch on YouTube](./watch), [Working 9 to 5](./working), [Regular, um, Expressions](./um), [Response Validation](./response) |
| 8 | Object-Oriented Programming | [Seasons of Love](./seasons), [Cookie Jar](./jar), [CS50 Shirtificate](./shirtificate) |
| Final Project | Terminalspiel & Tests | [Lights Out](./projectp/project) |

## CS50 SQL — Introduction to Databases with SQL

| Problem Set | Thema | Lösungen |
|---:|---|---|
| 0 | Querying | [Cyberchase](./cyberchase), [36 Views](./views), [Players](./players) |
| 1 | Relating | [Packages, Please](./packages), [DESE](./dese), [Moneyball](./moneyball) |
| 2 | Designing | [ATL](./atl), [Happy to Connect](./connect), [Union Square Donuts](./donuts) |
| 3 | Writing | [Don’t Panic!](./dont-panic), [Meteorite Cleaning](./meteorites) |
| 4 | Viewing | [Census Taker](./census), [The Private Eye](./private), [Bed and Breakfast](./bnb) |
| 5 | Optimizing | [In a Snap](./snap), [your.harvard](./harvard) |
| 6 | Scaling | [Happy to Connect (Sentimental)](./sentimental-connect), [Don’t Panic! mit Python](./dont-panic-python) |
| Zusatz | MovieLens-Datenmodell und Import | [MovieLens SQL](./matlab) |
| Final Project | Datenbankdesign & Automatisierung | [Network Scanning Ecosystem](./project) |

## CS50 AI — Introduction to Artificial Intelligence with Python

| Thema | Projekte |
|---|---|
| Search | [Degrees](./degrees), [Tic-Tac-Toe](./tictactoe) |
| Knowledge | [Knights](./knights), [Minesweeper](./minesweeper) |
| Uncertainty | [PageRank](./pagerank), [Heredity](./heredity) |
| Optimization | [Crossword](./crossword) |

## CS50 Web — Web Programming with Python and JavaScript

| Projekt | Anwendung | Technologien |
|---:|---|---|
| 0 | [Search](./search) — Frontend für Google Search, Image Search und Advanced Search | HTML, CSS |
| 1 | [Wiki](./wiki) — Django-Enzyklopädie mit Markdown-Einträgen, Suche und Bearbeitung | Python, Django, HTML, CSS |
| 2 | [Commerce](./commerce) — Auktionsplattform mit Listings, Geboten, Kommentaren und Watchlist | Python, Django, SQLite, HTML, CSS |
| 3 | [Mail](./mail) — Single-Page-E-Mail-Client mit Django-API | Python, Django, JavaScript, SQLite, HTML, CSS |

## Repository-Struktur

Jede Aufgabe liegt in einem eigenen Ordner. Die drei Abschlussprojekte sind bewusst den zugehörigen Kursen zugeordnet:

```text
cs50x-26/
├── projectx/              # CS50x Final Project
├── projectp/
│   └── project/           # CS50P Final Project
├── project/               # CS50 SQL Final Project
├── commerce/              # CS50 Web Project 2
├── mail/                  # CS50 Web Project 3
├── wiki/                  # CS50 Web Project 1
├── tictactoe/             # CS50 AI
├── speller/               # CS50x
└── ...
```

## Lokal ausführen

Repository klonen:

```bash
git clone https://github.com/p-keminer/cs50x-26.git
cd cs50x-26
```

### C-Aufgaben

Viele C-Aufgaben verwenden die CS50 Library und lassen sich im jeweiligen Ordner mit `make` kompilieren:

```bash
cd cash
make cash
./cash
```

### Python-Aufgaben

```bash
cd sentimental-cash
python cash.py
```

Für Aufgaben mit Tests:

```bash
cd test_bank
python -m pytest
```

### Django-Projekte

Für `wiki`, `commerce` und `mail` werden Django und für `wiki` zusätzlich Markdown-Unterstützung benötigt:

```bash
python -m venv .venv
python -m pip install django markdown2
cd commerce
python manage.py migrate
python manage.py runserver
```

Der Projektordner kann entsprechend durch `wiki` oder `mail` ersetzt werden.

Einzelne Aufgaben benötigen zusätzliche Kursdateien, die CS50 Library oder weitere Python-Pakete. Maßgeblich sind die Dateien und Hinweise im jeweiligen Projektordner.

## Academic Honesty

Die Lösungen spiegeln meinen eigenen Bearbeitungsstand wider und sind keine offiziellen Musterlösungen von Harvard oder CS50. Nutze dieses Repository verantwortungsvoll und beachte die für deinen Kurs geltenden Regeln zur [Academic Honesty](https://cs50.harvard.edu/x/honesty/).
