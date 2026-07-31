# CS50x 2026 – Lösungen & Projekte

[![Harvard CS50](https://img.shields.io/badge/Harvard-CS50-A51C30?style=flat-square)](https://cs50.harvard.edu/x/)
[![GitHub last commit](https://img.shields.io/github/last-commit/p-keminer/cs50x-26?style=flat-square)](https://github.com/p-keminer/cs50x-26/commits/main)
[![GitHub repo size](https://img.shields.io/github/repo-size/p-keminer/cs50x-26?style=flat-square)](https://github.com/p-keminer/cs50x-26)

Meine Lösungen, Übungsdateien und Projekte aus dem Harvard-CS50-Umfeld. Der Schwerpunkt liegt auf **CS50x 2026**; zusätzlich enthält das Repository Aufgaben aus **CS50P**, **CS50 SQL**, **CS50 AI** und **CS50 Web**.

> [!IMPORTANT]
> Dieses Repository dient als persönliche Dokumentation und Referenz. Wenn du selbst an CS50 teilnimmst, versuche die Aufgaben zuerst eigenständig zu lösen und beachte die [CS50 Academic Honesty Policy](https://cs50.harvard.edu/x/honesty/).

## Übersicht

| Kursbereich | Themen | Technologien |
|---|---|---|
| [CS50x](#cs50x) | Grundlagen, Algorithmen, Speicher, Datenstrukturen, Web | C, Python, SQL, HTML, CSS, JavaScript, Flask |
| [CS50P](#cs50p--introduction-to-programming-with-python) | Python-Grundlagen, Tests, Dateien, reguläre Ausdrücke, OOP | Python, pytest |
| [CS50 SQL](#cs50-sql--introduction-to-databases-with-sql) | Relationale Modelle, Abfragen, Views, Indizes, Skalierung | SQL, SQLite |
| [CS50 AI](#cs50-ai--introduction-to-artificial-intelligence-with-python) | Suche, Wissensrepräsentation, Wahrscheinlichkeit, Optimierung | Python |
| [CS50 Web](#cs50-web--web-programming-with-python-and-javascript) | Frontend, Django und Webanwendungen | Python, Django, HTML, CSS, JavaScript |

## CS50x

| Woche | Schwerpunkt | Lösungen |
|---:|---|---|
| 1 | C | [me](./me), [mario-more](./mario-more), [cash](./cash) |
| 2 | Arrays | [caesar](./caesar), [readability](./readability), [scrabble](./scrabble) |
| 3 | Algorithmen | [plurality](./plurality), [runoff](./runoff), [sort](./sort) |
| 4 | Speicher | [volume](./volume), [filter-less](./filter-less), [recover](./recover) |
| 5 | Datenstrukturen | [inheritance](./inheritance), [speller](./speller) |
| 6 | Python | [sentimental-cash](./sentimental-cash), [sentimental-mario-more](./sentimental-mario-more), [sentimental-readability](./sentimental-readability), [dna](./dna) |
| 7 | SQL | [songs](./songs), [movies](./movies), [fiftyville](./fiftyville) |
| 8 | HTML, CSS & JavaScript | [trivia](./trivia), [homepage](./homepage) |
| 9 | Flask | [birthdays](./birthdays), [finance](./finance) |

## Weitere Kurse

### CS50P – Introduction to Programming with Python

| Woche | Schwerpunkt | Lösungen |
|---:|---|---|
| 0 | Functions & Variables | [hello](./hello), [indoor](./indoor), [playback](./playback), [faces](./faces), [einstein](./einstein), [tip](./tip) |
| 1 | Conditionals | [deep](./deep), [test_bank](./test_bank), [extensions](./extensions), [interpreter](./interpreter), [meal](./meal) |
| 2 | Loops | [camel](./camel), [coke](./coke), [test_twttr](./test_twttr), [test_plates](./test_plates), [nutrition](./nutrition) |
| 3 | Exceptions | [test_fuel](./test_fuel), [taqueria](./taqueria), [grocery](./grocery), [outdated](./outdated) |
| 4 | Libraries | [adieu](./adieu), [bitcoin](./bitcoin), [figlet](./figlet), [game](./game), [professor](./professor) |
| 5 | Unit Tests | [test_twttr](./test_twttr), [test_bank](./test_bank), [test_plates](./test_plates), [test_fuel](./test_fuel) |
| 6 | File I/O | [lines](./lines), [pizza](./pizza), [scourgify](./scourgify), [shirt](./shirt) |
| 7 | Regular Expressions | [numb3rs](./numb3rs), [response](./response), [um](./um), [watch](./watch), [working](./working) |
| 8 | Object-Oriented Programming | [jar](./jar), [seasons](./seasons), [shirtificate](./shirtificate) |
| Final Projects | Eigene Projekte | [projectp](./projectp/project), [projectx](./projectx) |

### CS50 SQL – Introduction to Databases with SQL

Die SQL-Lösungen und zugehörigen Datensätze befinden sich unter:

[atl](./atl) · [bnb](./bnb) · [census](./census) · [connect](./connect) · [cyberchase](./cyberchase) · [dese](./dese) · [dont-panic](./dont-panic) · [dont-panic-python](./dont-panic-python) · [donuts](./donuts) · [harvard](./harvard) · [matlab](./matlab) · [meteorites](./meteorites) · [moneyball](./moneyball) · [packages](./packages) · [players](./players) · [private](./private) · [project](./project) · [sentimental-connect](./sentimental-connect) · [snap](./snap) · [views](./views)

### CS50 AI – Introduction to Artificial Intelligence with Python

| Thema | Projekte |
|---|---|
| Search | [degrees](./degrees), [tictactoe](./tictactoe) |
| Knowledge | [knights](./knights), [minesweeper](./minesweeper) |
| Uncertainty | [pagerank](./pagerank), [heredity](./heredity) |
| Optimization | [crossword](./crossword) |

### CS50 Web – Web Programming with Python and JavaScript

- [Search](./search) – Frontend für Google Search, Image Search und Advanced Search
- [Wiki](./wiki) – Django-basierte Enzyklopädie

## Repository-Struktur

Jede Aufgabe liegt in einem eigenen Ordner. Neben dem eigentlichen Quellcode sind – soweit für die Aufgabe erforderlich – Makefiles, Tests, Templates, statische Dateien und die von den Kursen bereitgestellten Datensätze enthalten.

```text
cs50x-26/
├── caesar/              # C
├── dna/                 # Python
├── finance/             # Flask
├── movies/              # SQL
├── tictactoe/           # AI mit Python
├── wiki/                # Django
└── ...
```

## Lokal ausführen

Repository klonen:

```bash
git clone https://github.com/p-keminer/cs50x-26.git
cd cs50x-26
```

C-Aufgaben werden in ihrem jeweiligen Ordner kompiliert:

```bash
cd cash
make cash
./cash
```

Python-Aufgaben lassen sich ebenfalls aus dem jeweiligen Ordner starten:

```bash
cd sentimental-cash
python cash.py
```

Einzelne Aufgaben benötigen zusätzliche Kursdateien, die CS50 Library oder Python-Pakete. Projektspezifische Abhängigkeiten stehen in den jeweiligen `requirements.txt`-Dateien.

## Hinweis

Die Lösungen spiegeln meinen eigenen Bearbeitungsstand wider und sind nicht als offizielle Musterlösungen von Harvard oder CS50 zu verstehen.
