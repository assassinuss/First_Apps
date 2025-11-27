def details():
    date = input("Data tranzacției (ex: 2025-10-08): ")
    summary = input("Descriere / Sumar: ")
    amount = float(input("Suma: "))
    return date, summary, amount

def menu():
    print("\n--- Meniu ---")
    print("1. Adaugă venit")
    print("2. Adaugă cheltuială")
    print("3. Afișează bugetul")
    print("4. Afișează istoricul")
    print("5. Ieșire")
    return input("Alege o opțiune: ")

def add_income(budget):
    date, summary, amount = details()
    budget += amount
    entry = f"{date} - Venit: {summary} +{amount} | Sold: {budget}\n"
    History.append(entry)
    with open("ziua3.txt", "w", encoding="utf-8") as file:
        file.writelines(entry)
    print("Venit adăugat cu succes!")
    return budget

def add_expense(budget):
    date, summary, amount = details()
    budget -= amount
    entry = f"{date} - Cheltuială: {summary} -{amount} | Sold: {budget}\n"
    History.append(entry)
    with open("ziua3.txt", "w", encoding="utf-8") as file:
        file.writelines(entry)
    print("Cheltuială adăugată cu succes!")
    return budget

def show_budget(budget):
    print(f"Buget curent: {budget}")
    return budget

def show_history(History):
    print("\n--- Istoric tranzacții ---")
    for entry in History:
        print(entry.strip())

option = 0
budget = 0.0
History = []

try:
    with open("ziua3.txt", "r") as file:
        History = file.readlines()
        last_line = ""
        for line in reversed(History):
            if line.strip():
                last_line = line.strip()
                break
except FileNotFoundError:
    print("Fișierul nu a fost găsit. Începem cu un buget de 0.")

print (last_line)
if "Sold: " in last_line:
        budget_str = last_line.split("Sold: ")[1].strip()
        budget = float(budget_str)
else:
    budget = 0.0

while option != 5:
    option = menu()

    if option == "1":
        budget = add_income(budget)
    elif option == "2":
        budget = add_expense(budget)
    elif option == "3":
        show_budget(budget)
    elif option == "4":
        show_history(History)
    elif option == "5":
        print("Ieșire... Istoricul a fost salvat.")
        break
    else:
        print("Alege o actiune")
