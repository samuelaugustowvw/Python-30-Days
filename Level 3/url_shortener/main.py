import os
import json
import string
import random
DB_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)),"urls.json")
CODE_LENGTH = 6
DOMAIN = "short.ly"
def load_db():
    if os.path.exists(DB_PATH):
        with open(DB_PATH,"r",encoding="utf-8") as file:
            return json.load(file)
    return {}
def save_db(db):
    with open(DB_PATH,"w",encoding="utf-8") as file:
        json.dump(db,file,indent=4)
def get_option():
    while True:
        try:
            option = int(input("Choose an option: "))
            if 0<=option<=3:
                return option
            print("Invalid option.")
        except ValueError:
            print("Please enter a valid number.")
def shorten_url(db):
    url = input("\nEnter the long URL: ").strip()
    if not url:
        print("URL cannot be empty.")
        return
    existing = find_existing_code(db, url)
    if existing:
        print("========================")
        print(f"Already shortened: {DOMAIN}/{existing}")
        print("========================")
        return
    code = generate_code(db)
    db[code] = {"url": url, "clicks": 0}
    save_db(db)
    print("========================")
    print(f"Short URL: {DOMAIN}/{code}")
    print("========================")
def find_existing_code(db,url):
    for code, data in db.items():
        if data["url"]==url:
            return code
    return None
def generate_code(db):
    characters = string.ascii_letters+string.digits
    while True:
        code = "".join(random.choices(characters, k=CODE_LENGTH))
        if code not in db:
            return code
def expand_url(db):
    code = input("\nEnter the short code: ").strip()
    if code not in db:
        print("That code does not exist.")
        return
    db[code]["clicks"]+=1
    save_db(db)
    print("========================")
    print(f"Original URL: {db[code]['url']}")
    print(f"Clicks: {db[code]['clicks']}")
    print("========================")
def list_urls(db):
    if not db:
        print("\nNo URLs shortened yet.")
        return
    print("\n========================")
    print("   ALL SHORTENED URLS")
    print("========================")
    for code, data in db.items():
        print(f"{DOMAIN}/{code}  ({data['clicks']} clicks)")
        print(f"   -> {data['url']}")
    print("========================")
def display_menu():
    print("\n========================")
    print("     URL SHORTENER")
    print("========================")
    print("1 - Shorten a URL")
    print("2 - Expand a short code")
    print("3 - List all URLs")
    print("0 - Exit")
def main():
    db = load_db()
    while True:
        display_menu()
        option = get_option()
        match option:
            case 1:
                shorten_url(db)
            case 2:
                expand_url(db)
            case 3:
                list_urls(db)
            case 0:
                print("\nGoodbye!")
                break
if __name__ == "__main__":
    main()