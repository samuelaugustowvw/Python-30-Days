# 🐍 Python 30 Days
My Python learning journey(29/07/2026) 30 hands-on projects, growing in difficulty from simple command-line scripts to production-grade applications. Each level introduces new concepts that build on the last.
## 📊 Progress
| Level | Difficulty | Projects | Status |
|:--|:--|:--|:--|
| 1 | Easy | 5/5 | ✅ Completed |
| 2 | Beginner | 5/5 | ✅ Completed |
| 3 | Intermediary | 5/5 | ✅ Completed |
| 4 | Advanced | 0/5 | ⬜ Not started |
| 5 | Hardcore | 0/5 | ⬜ Not started |
| 6 | Professional | 0/5 | ⬜ Not started |
---
## 📁 Level 1 — Very Easy
Foundational scripts focused on input/output, control flow, and clean function structure.

Concepts practiced in this level:** input validation with `try/except`, `while` loops, `match/case` branching, string manipulation, dictionaries, and splitting logic into small, single-purpose functions.
| # | Project | Description |
|:--|:--|:--|
| 1 | [Temperature Converter](./Level%201/temperature_converter) | Converts temperatures between Celsius, Fahrenheit, and Kelvin (6 directions) via a menu loop. |
| 2 | [Password Generator](./Level%201/password_generator) | Generates random passwords with configurable length and character types. |
| 3 | [IMC Calculator](./Level%201/imc_calculator) | Calculates Body Mass Index from weight and height and returns the health classification. |
| 4 | [Guess the Number](./Level%201/guess_the_number) | Number guessing game with Easy/Medium/Hard difficulty and higher/lower hints. |
| 5 | [Word Counter](./Level%201/word_and_character_counter) | Counts characters, words, and lines in a text and builds a word-frequency table. |

---
## 📁 Level 2 — Beginner
Projects that introduce **file persistence** and the first real-world **automation** — data that survives between runs.

**Concepts practiced in this level:** reading and writing files (`json`), the "load on start, save on every change" persistence pattern, CRUD operations, filesystem automation with `os` and `shutil`, `set` for tracking state, and data-driven logic with dictionaries.
| # | Project | Description |
|:--|:--|:--|
| 1 | [To-Do List](./Level%202/to_do_list) | Task manager with add/list/complete/remove, saving tasks to a JSON file so they persist between runs. |
| 2 | [Hangman](./Level%202/hangman) | Word guessing game with hints and an ASCII drawing that builds up across 6 wrong attempts. |
| 3 | [Rock Paper Scissors](./Level%202/rock_paper_scissors) | Best-of-3 game against the computer with a running score and dictionary-based win logic. |
| 4 | [Currency Converter](./Level%202/currency_converter) | Converts between any supported currencies using a single base-currency rate table, with session history. |
| 5 | [File Organizer](./Level%202/file_organizer) | Sorts files in a folder into subfolders by extension, with a preview and confirmation before moving. |

---
## 📁 Level 3 — Intermediary
Projects that reach out to **the internet** — consuming APIs, scraping web pages, and running a live service.

**Concepts practiced in this level:** HTTP requests with `requests`, API keys and environment variables, parsing nested JSON, HTML parsing with BeautifulSoup, writing CSV, handling HTTP status codes and network errors, collision-safe code generation, and `async`/`await` for a continuously running service.
| # | Project | Description |
|:--|:--|:--|
| 1 | [Weather App](./Level%203/weather_app) | Fetches live weather for any city from the OpenWeatherMap API and parses the nested JSON response. |
| 2 | [Web Scraper](./Level%203/book_scraper) | Scrapes book titles, prices, and ratings from a web page with BeautifulSoup and saves them to CSV. |
| 3 | [Quiz](./Level%203/quiz) | Multiple-choice quiz that loads questions from an external JSON file, shuffles them, and tracks a high score. |
| 4 | [URL Shortener](./Level%203/url_shortener) | Generates unique short codes for long URLs, expands them back, tracks clicks, and persists to JSON. |
| 5 | [Telegram Bot](./Level%203/telegram_bot) | A live Telegram bot with commands (`/start`, `/help`, `/echo`, `/roll`) built on the async python-telegram-bot library. |

---
## 🚀 How to Run
Each project is a standalone script. Requires **Python 3.10+** (some projects use the `match` statement).
```bash
python "Level 1/temperature_converter/main.py"
```
## 🛠️ Tech
- **Language:** Python 3.10+
- **Dependencies:** Standard library (Levels 1–2). Level 3 adds `requests`, `beautifulsoup4`, and `python-telegram-bot`.

> **Note:** the Weather App and Telegram Bot read secrets (API key / bot token) from environment variables — no keys are committed to this repo.
## 👤 Author
**[Samuel Augusto]** — [GitHub](https://github.com/samuelaugustowvw) · [LinkedIn](https://www.linkedin.com/in/samuel-augusto-bb398040b/)
