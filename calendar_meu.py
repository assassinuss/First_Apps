import os

#Calendar

#user_check

#user_load
def user_load():
    users = []
    for file in os.listdir():
        if file.endswith(".txt"):
            username = file[:-4]
            with open(file, "r") as f:
                first_line = f.readline().strip()
                if first_line == username:
                    users.append(username)
    if not users:
        print("Nu exista utilizatori.")
        return
    print("Utilizatori disponibili:")
    for idx, user in enumerate(users, 1):
        print(f"{idx}. {user}")
    print("Alege utilizatorul (introdu numarul):")
    try:
        choice = int(input())
        if 1 <= choice <= len(users):
            print(f"Utilizatorul selectat: {users[choice-1]}")
        else:
            print("Optiune invalida.")
    except ValueError:
        print("Optiune invalida.")

#user_create
def user_create():
    print("Introdu numele utilizatorului:")
    username = input()
    print(f"Utilizatorul {username} a fost creat cu succes.")
    with open("username.txt", "w") as f:
        f.write()


#select_day

#select_month

#select_year

#count_events

#show events

#menu
def menu():
    print("Alege optiunea: \n1. Selecteaza Utilizator \n2. creaza Utilizator")
    option=input()
    if option == 1:
        user_create ()
    elif option == 2:
        user_load
