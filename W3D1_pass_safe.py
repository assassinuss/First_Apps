import os
import json

FILE = "passwords.json"

def load_data():
    if os.path.exists(FILE):
        with open(FILE, "r", encoding="utf-8") as f:
            try:
                return json.load(f)
            except json.JSONDecodeError:
                return []
    return []

def save_data(data):
    with open(FILE, "w", encoding="utf-8") as f:
        json.dump(data, f)

def add_entry(data):
    site = input("Site: ").strip()
    user = input("User: ").strip()
    password = input("Parola: ").strip()

    entry = {"site": site, "user": user, "password": password}
    data.append(entry)
    save_data(data)
    print("Intrare salvata.")

def view_entries(data):
    if not data:
        print("Nu exista intrari.")
        return
    print("\n=== Intrari salvate ===")
    for i, e in enumerate(data, 1):
        print(f"{i}. {e['site']}")
        print(f"   User: {e['user']}")
        print(f"   Parola: {e['password']}")
    print()

def search_entries(data):
    q = input("Cautare dupa site (substring): ").strip().lower()
    found = [e for e in data if q in e.get("site","").lower()]
    if not found:
        print("Niciun rezultat.")
        return
    for i, e in enumerate(found, 1):
        print(f"{i}. {e['site']}  |  {e['user']}  |  {e['password']}")

def delete_entry(data):
    view_entries(data)
    if not data:
        return
    try:
        idx = int(input("Numarul intrarii de sters (0 pentru anulare): ").strip())
    except ValueError:
        print("Input invalid.")
        return
    if idx == 0:
        return
    if 1 <= idx <= len(data):
        removed = data.pop(idx - 1)
        save_data(data)
        print(f"Sters: {removed['site']}")
    else:
        print("Index in afara intervalului.")

def clear_entries():
    confirm = input("Stergi TOT (da/nu)? ").strip().lower()
    if confirm == "da":
        save_data([])
        print("Toate intrarile au fost sterse.")
    else:
        print("Anulat.")

def menu():
    data = load_data()
    while True:
        print("\n=== PASSWORD SAFE ===")
        print("1. Adauga parola")
        print("2. Vezi toate intrarile")
        print("3. Cauta dupa site")
        print("4. Sterge o intrare")
        print("5. Sterge tot")
        print("6. Iesire")
        choice = input("> ").strip()
        if choice == "1":
            add_entry(data)
        elif choice == "2":
            view_entries(data)
        elif choice == "3":
            search_entries(data)
        elif choice == "4":
            delete_entry(data)
        elif choice == "5":
            clear_entries()
            data = []
        elif choice == "6":
            break
        else:
            print("Optiune invalida.")

menu()
