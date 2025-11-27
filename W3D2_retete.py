import json
import os

FILE = "retete.json"

def load_recipes():
    if os.path.exists(FILE):
        with open(FILE, "r", encoding="utf-8") as f:
            try:
                return json.load(f)
            except json.JSONDecodeError:
                return []
    return []

def save_recipes(data):
    with open(FILE, "w", encoding="utf-8") as f:
        json.dump(data, f)

def add_recipe(data):
    name = input("Nume rețetă: ").strip()
    ingredients = input("Ingrediente (separate prin virgulă): ").strip()
    steps = input("Pași de preparare: ").strip()

    recipe = {"nume": name, "ingrediente": ingredients, "pași": steps}
    data.append(recipe)
    save_recipes(data)
    print("Rețeta a fost adăugată cu succes!\n")

def view_recipes(data):
    if not data:
        print("Nu există rețete salvate.\n")
        return
    print("\n=== Toate rețetele ===")
    for i, r in enumerate(data, 1):
        print(f"{i}. {r['nume']}")
        print(f"   Ingrediente: {r['ingrediente']}")
        print(f"   Pași: {r['pași']}\n")

def search_recipe(data):
    q = input("Caută rețetă după nume: ").lower()
    found = [r for r in data if q in r['nume'].lower()]
    if not found:
        print("Nicio rețetă găsită.\n")
        return
    for i, r in enumerate(found, 1):
        print(f"{i}. {r['nume']}")
        print(f"   Ingrediente: {r['ingrediente']}")
        print(f"   Pași: {r['pași']}\n")

def modify_recipe(data):
    view_recipes(data)
    if not data:
        return
    try:
        idx = int(input("Numărul rețetei de modificat (0 pentru anulare): "))
    except ValueError:
        print("Input invalid.\n")
        return
    if idx == 0 or idx > len(data):
        return
    r = data[idx - 1]
    print(f"Modifici rețeta: {r['nume']}")
    r['nume'] = input(f"Nume nou [{r['nume']}]: ").strip() or r['nume']
    r['ingrediente'] = input(f"Ingrediente noi [{r['ingrediente']}]: ").strip() or r['ingrediente']
    r['pași'] = input(f"Pași noi [{r['pași']}]: ").strip() or r['pași']
    save_recipes(data)
    print("Rețeta a fost actualizată!\n")

def delete_recipe(data):
    view_recipes(data)
    if not data:
        return
    try:
        idx = int(input("Numărul rețetei de șters (0 pentru anulare): "))
    except ValueError:
        print("Input invalid.\n")
        return
    if idx == 0 or idx > len(data):
        return
    removed = data.pop(idx - 1)
    save_recipes(data)
    print(f"Rețeta '{removed['nume']}' a fost ștearsă.\n")

def menu():
    data = load_recipes()
    while True:
        print("=== CARTE DE BUCATE ===")
        print("1. Adaugă rețetă")
        print("2. Vezi toate rețetele")
        print("3. Caută o rețetă")
        print("4. Modifică o rețetă")
        print("5. Șterge o rețetă")
        print("6. Ieșire")
        choice = input("> ").strip()
        if choice == "1":
            add_recipe(data)
        elif choice == "2":
            view_recipes(data)
        elif choice == "3":
            search_recipe(data)
        elif choice == "4":
            modify_recipe(data)
        elif choice == "5":
            delete_recipe(data)
        elif choice == "6":
            print("La revedere!")
            break
        else:
            print("Opțiune invalidă.\n")

menu()
