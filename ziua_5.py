import datetime
import os

file_name = "ziua_5.txt"

tasks = {day: [] for day in ['luni', 'marti', 'miercuri', 'joi', 'vineri', 'sambata', 'duminica']}

def load_file():
    if not os.path.exists(file_name):
        with open(file_name, "w", encoding="utf-8") as f:
            for zi in tasks:
                f.write(f"{zi}:\n")
        return
    with open(file_name, "r", encoding="utf-8") as f:
        lines = f.readlines()
    current_day = None
    for line in lines:
        line = line.strip()
        if not line:
            continue
        if line.endswith(":"):
            current_day = line[:-1]
        elif current_day and current_day in tasks:
            tasks[current_day].append(line)

def save_file():
    with open(file_name, "w", encoding="utf-8") as f:
        for zi, lista in tasks.items():
            f.write(f"{zi}:\n")
            for i in lista:
                f.write(f"{i}\n")
            f.write("\n")

def get_week():
    for zi, lista in tasks.items():
        print(f"{zi}: {', '.join(lista) if lista else 'Niciun task'}")

def get_day():
    zile = {
        'monday': 'luni', 'tuesday': 'marti', 'wednesday': 'miercuri',
        'thursday': 'joi', 'friday': 'vineri', 'saturday': 'sambata', 'sunday': 'duminica'
    }
    today = datetime.datetime.now().strftime('%A').lower()
    zi = zile.get(today, 'luni')
    print(f"Task-uri pentru azi ({zi}): {', '.join(tasks[zi]) if tasks[zi] else 'Niciun task'}")

def add_task():
    zi = input("Pentru ce zi? ").strip().lower()
    if zi in tasks:
        task = input("Descriere task: ").strip()
        if task:
            tasks[zi].append(task)
            save_file()
            print("Task adaugat.")
    else:
        print("Zi invalida.")

def modify_task():
    zi = input("Pentru ce zi vrei sa modifici? ").strip().lower()
    if zi in tasks and tasks[zi]:
        for j, i in enumerate(tasks[zi]):
            print(f"{j+1}. {i}")
        try:
            nr = int(input("Numarul task-ului de modificat: ")) - 1
            if 0 <= nr < len(tasks[zi]):
                nou = input("Noua descriere: ").strip()
                tasks[zi][nr] = nou
                save_file()
                print("Task modificat.")
            else:
                print("Numar invalid.")
        except ValueError:
            print("Introdu un numar valid.")
    else:
        print("Nu exista task-uri pentru aceasta zi.")

def menu():
    load_file()
    while True:
        print("\n1. Vezi toate task-urile saptamanii")
        print("2. Vezi task-urile de azi")
        print("3. Adauga task")
        print("4. Modifica task")
        print("5. Iesire\n")
        opt = input("Alege optiunea: ").strip()
        if opt == '1':
            get_week()
        elif opt == '2':
            get_day()
        elif opt == '3':
            add_task()
        elif opt == '4':
            modify_task()
        elif opt == '5':
            save_file()
            print("Datele au fost salvate.")
            break
        else:
            print("Optiune invalida.")

if __name__ == "__main__":
    menu()
