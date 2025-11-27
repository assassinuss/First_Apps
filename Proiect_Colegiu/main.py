import sys
import os


DBarbitri = "arbitri.txt"
DBsedinte = "sedinte.txt"
DBraliuri = "raliuri.txt"
DBmateriale = "materiale.txt"

class arbitru():
    def __init__(self, id, nume, an_inscriere, nr_raliuri, competente):
        self.id = id
        self.nume = nume
        self.an_inscriere = an_inscriere
        self.nr_raliuri = nr_raliuri
        self.competente = competente
    
    def info_inst(self):
        return f"ID: {self.id.strip()}, Nume: {self.nume.strip()}, An Inscriere: {self.an_inscriere.strip()}, Nr Raliuri: {self.nr_raliuri.strip()}, Competente: {self.competente.strip()}"
    
    def init_inst(self):
        self.id = input("Introduceti ID-ul arbitru: ").strip()
        for i in range(len(self.id), 4):
            self.id += " "
        self.nume = input("Introduceti numele arbitru: ").strip()
        for i in range(len(self.nume), 30):
            self.nume += " "
        self.an_inscriere = input("Introduceti anul inscrierii: ").strip()
        for i in range(len(self.an_inscriere), 6):
            self.an_inscriere += " "
        self.nr_raliuri = input("Introduceti numarul de raliuri: ").strip()
        for i in range(len(self.nr_raliuri), 6):
            self.nr_raliuri += " "
        self.competente = input("Introduceti competentele arbitru (despratite de virgula): ")

    def modify_inst(self):
        print ("Modificati datele arbitru (apasati Enter pentru a pastra valoarea curenta):")
        temp_id = input("Introduceti noul ID al arbitru: ").strip()
        if temp_id != "":
            self.id = temp_id
        temp_nume = input("Introduceti noul numele arbitru: ").strip()
        for i in range(len(self.nume), 30):
            temp_nume += " "
        temp_an_inscriere = input("Introduceti noul anul inscrierii: ").strip()
        if temp_an_inscriere != "":
            self.an_inscriere = temp_an_inscriere   
        temp_nr_raliuri = input("Introduceti noul numarul de raliuri: ").strip()
        if temp_nr_raliuri != "":
            self.nr_raliuri = temp_nr_raliuri
        temp_competente = input("Introduceti noile competentele arbitru (despratite de virgula): ")
        if temp_competente != "":
            self.competente = temp_competente

    def save_inst(self, filename):
        with open(filename, "Arbitri.txt", encoding="utf-8") as f:
            content=f.read()
            entry = f"{self.id}|{self.nume}|{self.an_inscriere}|{self.nr_raliuri}|{self.competente}\n"
            f.write(content)
            f.write(entry)
    
    def remove_inst(self):
        id = input("Introduceti ID-ul arbitru de sters: ")
        with open("arbitri.txt", "r", encoding="utf-8") as f:
            lines = f.readlines()
        with open("arbitri.txt", "w", encoding="utf-8") as f:
            for line in lines:
                if not line.startswith(id):
                    f.write(line)  


class sedinta:
    def __init__(self, id, data, subiect, participanti, locatie, Log):
        self.id = id
        self.data = data
        self.subiect = subiect
        self.participanti = participanti
        self.locatie = locatie

class raliu:
    def __init__(self, nume, data, locatie, arbitri_delegati):
        self.nume = nume
        self.data = data
        self.locatie = locatie
        self.arbitri_delegati = arbitri_delegati

class material:
    def __init__(self, id, nume, an_dare_in_folosinta, nr_folosiri, stare):
        self.id = id    
        self.nume = nume
        self.an_dare_in_folosinta = an_dare_in_folosinta
        self.nr_folosiri = nr_folosiri
        self.stare = stare

#Utilitare generale

def open_file(filename, mode):
    try:
        file=open(filename, mode)
        return file
    except FileNotFoundError:
        print(f"Eroare: fisierul {filename} nu a fost gasit.")
        return None
    
def add_entry(filename, entry):
    with open(filename, "a") as file:
        file.write(entry + "\n")

def sort_file(filename, header):
    with open(filename, "r") as file:
        lines=file.readlines()
    lines.sort()
    with open (filename, "w") as file:
        file.write(header)
        file.writelines(lines)
    return lines

#functii principale pentru gestionare

def arbitri():
    header = "ID  |nume                |An Ins|Nr Ral|Competente\n"
    print("Gestionare arbitri")
    selectie = ""
    while selectie != "5":
        selectie=input("Alegeti o optiune: \n1. Adauga arbitru\n2. Afiseaza arbitri\n3. Sterge arbitru\n4. Modifica arbitru\n5.Meniu Anterior\n\n")
        match selectie:
            case "1":
                with open("arbitri", "r", encoding="utf-8") as data:
                    content = data.read()
                id = input("Introduceti ID-ul arbitru: ")
                for i in range(len(id), 4):
                    id += " "
                nume = input("Introduceti numele arbitru: ")
                for i in range(len(nume), 20):
                    nume += " "
                an_inscriere = input("Introduceti anul inscrierii: ")
                for i in range(len(an_inscriere), 6):
                    an_inscriere += " "
                nr_raliuri = input("Introduceti numarul de raliuri: ")
                for i in range(len(nr_raliuri), 6):
                    nr_raliuri += " "
                competente = input("Introduceti competentele arbitru: ")
                print (type(data))
                entry = f"{id}|{nume}|{an_inscriere}|{nr_raliuri}|{competente}\n"
                with open("arbitri", "a", encoding="utf-8") as data:
                    data.write(entry)               

            case "2":
                with open("arbitri", "r", encoding="utf-8") as data:
                    content = data.read()
                    print(content)
                    data.close()

            case "3":
                with open("arbitri", "w", encoding="utf-8") as data:
                    id_sters = input("Introduceti ID-ul arbitru de sters: ")
                    lines = data.readlines()
                    data.seek(0)
                    for line in lines:
                        if not line.startswith(id_sters):
                            data.write(line)
                    data.truncate()
                    data.close()

            case "4":
                try:
                    with open("arbitri", "r", encoding="utf-8") as f:
                        lines = f.readlines()
                except FileNotFoundError:
                    print("Fișierul nu există.")
                    return  
                id_arbitru=input("Introduceti ID-ul arbitru de modificat: ")
                id_gasit=False
                for line in lines:
                    if line.startswith(id_arbitru):
                        print(line)
                        print("Introduceti noile date pentru arbitru:")
                        id = input("Introduceti ID-ul arbitru: ")
                        for i in range(len(id), 4):
                            id += " "
                        nume = input("Introduceti numele arbitru: ")
                        for i in range(len(nume), 20):
                            nume += " "
                        an_inscriere = input("Introduceti anul inscrierii: ")
                        for i in range(len(an_inscriere), 6):
                            an_inscriere += " "
                        nr_raliuri = input("Introduceti numarul de raliuri: ")
                        for i in range(len(nr_raliuri), 6):
                            nr_raliuri += " "
                        competente = input("Introduceti competentele arbitru: ")

                        entry = f"{id}|{nume}|{an_inscriere}|{nr_raliuri}|{competente}\n"
                        lines[lines.index(line)] = entry
                        id_gasit=True
                    else:
                        lines.append(line)
                    f.close()
                    
                if not id_gasit:
                    print("ID-ul arbitru nu a fost gasit.")
                    return
            case "5":
                pass
            
        sort_file("arbitri", header)

#gestionare sedinte - inca in lucru

def sedinte():
    print("Gestionare materiale")
    selectie = ""
    separtor="end of meeting"
    while selectie != "5":
        with open(DBsedinte, "r", encoding="utf-8") as f:
            content=f.read()
            lines=content.splitlines()
            entry=""
            ID=1
            to_print=7
            for line in lines:
                if line==separtor:
                    print(f"{ID} - {entry}")
                    print("\n")
                    entry=""
                    ID+=1
                    to_print=9
                elif to_print==5:
                        entry+=f"{line} - "
                elif to_print==1:
                        entry+=f"{line} ; "                 
                to_print-=1


        selectie = input(
            "Alegeti o optiune: \n"
            "0. Iesire din gestionare sedinte\n"
            "1. Adauga log-ul unei sedinte\n"
            "2. Afiseaza log-ul unei sedinte\n"
            "3. Modifica log-ul unei sedinte\n")
        match selectie:
            case "0":
                return
            
# Adauga log-ul unei sedinte, inca nu merge, nu afiseaza corect sedintele anterioare in meniul de selectare

            case "1":
                with open(DBsedinte, "a", encoding="utf-8") as f:
                    entry=""
                    entry+=f"Data: \n\n{input('Introduceti data sedintei (ex: 2025-05-10): ')}\n"
                    entry+=f"\nLocatie: \n\n{input('Introduceti locatia sedintei: ')}\n"
                    entry+=f"\nParticipanti: \n\n{input('Introduceti participantii la sedinta (separati prin virgula): ')}\n"
                    entry+=f"\nLog:\n"
                    f.write(entry + "\n")

                    print("Introduceti log-ul sedintei (terminati cu 'end of meeting' pe o linie noua):")
                    while True:
                        line = input()
                        if line.strip() == separtor:
                            f.write("\nend of file\n")
                            break                        
                        f.write(line + "\n")

            
            case "2":
                ID = int(input("Introduceti ID-ul sedintei de afisat: "))
                for line in lines:
                    while ID!=1:
                        if line==separtor:
                            ID-=1
                        pass
                    if line!=separtor:
                        print(line)
                    else:
                        break

#         
            case "3":
                ID = int(input("Introduceti ID-ul sedintei de modificat: "))
                new_lines = []
                current_id = 1
                inside_meeting = False
                for line in lines:
                    if line == separtor:
                        if current_id == ID:
                            print("Introduceti noul log al sedintei (terminati cu 'end of meeting' pe o linie noua):")
                            while True:
                                new_line = input()
                                if new_line.strip() == separtor:
                                    break
                                new_lines.append("\n" + new_line + "\n")
                            inside_meeting = False
                        else:
                            new_lines.append(line + "\n")
                        current_id += 1
                    else:
                        if current_id == ID:
                            inside_meeting = True
                        if not inside_meeting:
                            new_lines.append(line + "\n")

                with open(DBsedinte, "w", encoding="utf-8") as f:
                    f.writelines(new_lines)
                    
      
    
    pass

def delegari():
    header = (
        "ID  |Raliu       |Data      |Locatie     |IDAr|Nume arbitru        |Post              |Decont|Coord|Materiale\n"
    )

    def genereaza_id_delegare():
        try:
            with open(DBraliuri, "r", encoding="utf-8") as f:
                lines = f.readlines()
        except FileNotFoundError:
            return "2500"

        max_id = 2499
        for line in lines[1:]:
            parts = line.split("|")
            if not parts:
                continue
            id_str = parts[0].strip()
            if len(id_str) == 4 and id_str.isdigit() and id_str.startswith("25"):
                val = int(id_str)
                if val > max_id:
                    max_id = val
        urmator = max_id + 1
        return str(urmator).zfill(4)

    if not os.path.exists(DBraliuri):
        with open(DBraliuri, "w", encoding="utf-8") as f:
            f.write(header)
    else:
        with open(DBraliuri, "r+", encoding="utf-8") as f:
            content = f.read()
            if content.strip() == "":
                f.seek(0)
                f.write(header)
                f.truncate()

    print("Gestionare delegari la raliuri")
    print("--------------------------------")
    with open(DBraliuri, "r", encoding="utf-8") as f:
        content = f.read()
        if content.strip() == "" or content.strip() == header.strip():
            print("Nu exista delegari inregistrate.")
        else:
            print(content)

    selectie = ""
    while selectie != "0":
        selectie = input(
            "\nAlegeti o optiune: \n"
            "0. Meniu aterior\n"
            "1. Adauga delegare la un raliu\n"
            "2. Afiseaza toate delegarile\n"
            "3. Sterge o delegare\n"
            "4. Modifica o delegare\n"
            "5. Adauga delegat la raliu\n\n"
        )

        if selectie == "1":
            id_del = genereaza_id_delegare()
            header = "ID  |Nume                |Post               |Decont|Materiale\n"
            print(f"ID-ul generat pentru delegare este: {id_del}")
            id_del_col = id_del
            for i in range(len(id_del_col), 4):
                id_del_col += " "

            nume_raliu = input("Introduceti numele raliului: ")
            for i in range(len(nume_raliu), 12):
                nume_raliu += " "

            data = input("Introduceti data raliului (ex: 2025-05-10): ")
            for i in range(len(data), 10):
                data += " "

            locatie = input("Introduceti locatia raliului: ")
            for i in range(len(locatie), 12):
                locatie += " "

            id_arb = input("Introduceti ID-ul arbitrului: ")
            for i in range(len(id_arb), 4):
                id_arb += " "

            nume_arb = input("Introduceti numele arbitrului: ")
            for i in range(len(nume_arb), 20):
                nume_arb += " "

            post = input("Introduceti postul avut la raliu (ex: Comisar sportiv): ")
            for i in range(len(post), 18):
                post += " "

            decont = input("A avut decont de masina? (DA/NU): ").upper()
            if decont not in ["DA", "NU"]:
                decont = "NU"
            for i in range(len(decont), 5):
                decont += " "

            coord = input("A fost coordonator de delegatie? (DA/NU): ").upper()
            if coord not in ["DA", "NU"]:
                coord = "NU"
            for i in range(len(coord), 5):
                coord += " "

            materiale = input("Materialele avute (separate prin virgula): ")

            entry = f"{id_del_col}|{nume_raliu}|{data}|{locatie}|{id_arb}|{nume_arb}|{post}|{decont}|{coord}|{materiale}\n"
            with open(DBraliuri, "a", encoding="utf-8") as f:
                f.write(entry)

            with open("/arhiva_delegari/{id_del}.txt", "w", encoding="utf-8") as f:
                f.write(header)
                f.write(id_arb + "    ")
                f.write(nume_arb)
                i = len(nume_arb.strip())
                for i in range(20):
                    nume_arb+=" "
                f.write(post)
                f.write("|")
                i = len(post.strip())
                for i in range(20):
                    post+=" "
                f.write(decont.strip())
                f.write("    |")                
                f.write(materiale)

        elif selectie == "2":
            with open(DBraliuri, "r", encoding="utf-8") as f:
                content = f.read()
                if content.strip() == "" or content.strip() == header.strip():
                    print("Nu exista delegari inregistrate.")
                else:
                    print(content)

        elif selectie == "3":
            try:
                with open(DBraliuri, "r", encoding="utf-8") as f:
                    lines = f.readlines()
            except FileNotFoundError:
                print(f"Fisierul {DBraliuri} nu exista inca.")
                continue

            id_del_cautat = input("Introduceti ID-ul delegarii de sters (de forma 25**): ").strip()

            new_lines = []
            gasit = False
            for idx, line in enumerate(lines):
                if idx == 0:
                    new_lines.append(line)
                    continue

                parts = line.split("|")
                if not parts:
                    new_lines.append(line)
                    continue

                if parts[0].strip() == id_del_cautat:
                    gasit = True
                    continue 

                new_lines.append(line)

            if not gasit:
                print("Delegarea nu a fost gasita.")
            else:
                with open(DBraliuri, "w", encoding="utf-8") as f:
                    f.writelines(new_lines)
                print("Delegare stearsa cu succes.")

        elif selectie == "4":
            try:
                with open(DBraliuri, "r", encoding="utf-8") as f:
                    lines = f.readlines()
            except FileNotFoundError:
                print(f"Fisierul {DBraliuri} nu exista inca.")
                continue

            id_del_cautat = input("Introduceti ID-ul delegarii de modificat (de forma 25**): ").strip()
            id_gasit = False

            for index, line in enumerate(lines):
                if index == 0:
                    continue 

                parts = line.split("|")
                if not parts:
                    continue

                if parts[0].strip() == id_del_cautat:
                    print("Inregistrarea curenta:")
                    print(line)
                    print("Introduceti noile date (Enter = pastreaza valoarea curenta).")

                    id_vechi = parts[0].strip()
                    raliu_vechi = parts[1].strip()
                    data_veche = parts[2].strip()
                    locatie_veche = parts[3].strip()
                    idarb_vechi = parts[4].strip()
                    numearb_vechi = parts[5].strip()
                    post_vechi = parts[6].strip()
                    decont_vechi = parts[7].strip()
                    coord_vechi = parts[8].strip()
                    materiale_vechi = parts[9].strip() if len(parts) > 9 else ""

                    id_nou = input(f"ID delegare [{id_vechi}]: ").strip()
                    if id_nou == "":
                        id_nou = id_vechi
                    for i in range(len(id_nou), 4):
                        id_nou += " "

                    nume_raliu = input(f"Nume raliu [{raliu_vechi}]: ")
                    if nume_raliu == "":
                        nume_raliu = raliu_vechi
                    for i in range(len(nume_raliu), 12):
                        nume_raliu += " "

                    data = input(f"Data raliului [{data_veche}]: ")
                    if data == "":
                        data = data_veche
                    for i in range(len(data), 10):
                        data += " "

                    locatie = input(f"Locatie [{locatie_veche}]: ")
                    if locatie == "":
                        locatie = locatie_veche
                    for i in range(len(locatie), 12):
                        locatie += " "

                    id_arb = input(f"ID arbitru [{idarb_vechi}]: ")
                    if id_arb == "":
                        id_arb = idarb_vechi
                    for i in range(len(id_arb), 4):
                        id_arb += " "

                    nume_arb = input(f"Nume arbitru [{numearb_vechi}]: ")
                    if nume_arb == "":
                        nume_arb = numearb_vechi
                    for i in range(len(nume_arb), 20):
                        nume_arb += " "

                    post = input(f"Post [{post_vechi}]: ")
                    if post == "":
                        post = post_vechi
                    for i in range(len(post), 18):
                        post += " "

                    decont = input(f"Decont auto (DA/NU) [{decont_vechi.strip()}]: ").upper()
                    if decont == "":
                        decont = decont_vechi.strip().upper()
                    if decont not in ["DA", "NU"]:
                        decont = "NU"
                    for i in range(len(decont), 5):
                        decont += " "

                    coord = input(f"Coordonator (DA/NU) [{coord_vechi.strip()}]: ").upper()
                    if coord == "":
                        coord = coord_vechi.strip().upper()
                    if coord not in ["DA", "NU"]:
                        coord = "NU"
                    for i in range(len(coord), 5):
                        coord += " "

                    materiale = input(f"Materiale [{materiale_vechi}]: ")
                    if materiale == "":
                        materiale = materiale_vechi

                    entry = f"{id_nou}|{nume_raliu}|{data}|{locatie}|{id_arb}|{nume_arb}|{post}|{decont}|{coord}|{materiale}\n"
                    lines[index] = entry
                    id_gasit = True
                    break

            if not id_gasit:
                print("Delegarea nu a fost gasita.")
            else:
                with open(DBraliuri, "w", encoding="utf-8") as f:
                    f.writelines(lines)
                print("Delegare modificata cu succes.")
        elif selectie == "5":
                id_del = input("Introduceti ID-ul delegarii pentru care doriti sa adaugati un delegat (de forma 25**): ")
                try:
                    with open(fr"arhiva_delegari/{id_del}.txt", "r", encoding="utf-8") as f:
                        print(f.read())
                except FileNotFoundError:
                    try:
                        with open(fr"arhiva_delegari/{id_del}", "r", encoding="utf-8") as f:
                            print(f.read())

                    except FileNotFoundError:    
                        print("Fisierul de arhiva pentru aceasta delegare nu exista. Creati mai intai delegarea.")
                        continue

                try:
                    with open(fr"/arhiva_delegari/{id_del}.txt", "w", encoding="utf-8") as f:
                        f.write(input("Introduceti ID-ul arbitrului delegat") + "    ")
                        f.write(nume_arb=input("Introduceti numele arbitrului delegat"))
                        i = len(nume_arb.strip())
                        for i in range(20):
                            nume_arb+=" "
                        f.write(post=input("Introduceti postul avut la raliu (ex: Comisar sportiv): "))
                        f.write("|")
                        i = len(post.strip())
                        for i in range(20):
                            post+=" "
                        f.write(input(fr"A avut {nume_arb} decontare carburant? (DA/NU)").strip())
                        f.write("    |")                
                        f.write(input("Materialele avute (separate prin virgula): ") + "\n")
                except FileNotFoundError:
                    try:
                        with open(fr"arhiva_delegari/{id_del}", "a", encoding="utf-8") as f:
                            f.write(input("Introduceti ID-ul arbitrului delegat") + "    ")
                            nume_arb = input("Introduceti numele arbitrului delegat")
                            f.write(nume_arb)
                            i = len(nume_arb.strip())
                            for i in range(20):
                                nume_arb+=" "
                            post=input("Introduceti postul avut la raliu (ex: Comisar sportiv): ")
                            f.write(post)
                            i = len(post.strip())
                            for i in range(20):
                                post+=" "
                            f.write("|")
                            f.write(input(fr"A avut {nume_arb} decontare carburant? (DA/NU)").strip())
                            f.write("    |")                
                            f.write(input("Materialele avute (separate prin virgula): ") + "\n")
                    except FileNotFoundError:
                        print("Fisierul de arhiva pentru aceasta delegare nu exista.")

        elif selectie == "0":
            return
        else:
            print("Optiune invalida. Incercati din nou.")

def materiale():
    header = "ID      |     Nume    |   An dare in folosinta    |    numar de folosiri    |      Stare\n"
    print("Gestionare materiale")
    selectie = ""
    while selectie != "5":
        selectie = input(
            "Alegeti o optiune: \n"
            "1. Adauga material\n"
            "2. Afiseaza materiale\n"
            "3. Sterge material\n"
            "4. Modifica material\n"
            "5. Meniu anterior\n\n"
        )

        if selectie == "1":
          
            with open(DBmateriale, "a", encoding="utf-8") as f:
                id_mat = input("Introduceti ID-ul materialului: ")
                for i in range(len(id_mat), 4):
                    id_mat += " "

                nume = input("Introduceti numele materialului: ")
                for i in range(len(nume), 20):
                    nume += " "

                an_dare = input("Introduceti anul dării în folosinta: ")
                for i in range(len(an_dare), 6):
                    an_dare += " "

                nr_folosiri = input("Introduceti numarul de folosiri: ")
                for i in range(len(nr_folosiri), 6):
                    nr_folosiri += " "

                stare = input("Introduceti starea materialului: ")

                entry = f"{id_mat}|{nume}|{an_dare}|{nr_folosiri}|{stare}\n"
                f.write(entry)

        elif selectie == "2":  
            with open(DBmateriale, "r", encoding="utf-8") as f:
                    content = f.read()
                    if content.strip() == "":
                        print("Nu exista materiale inregistrate.")
                    else:
                        print(content)

        elif selectie == "3":
            with open(DBmateriale, "r", encoding="utf-8") as f:
                    lines = f.readlines()


            id_sters = input("Introduceti ID-ul materialului de sters: ")

            new_lines = []
            gasit = False
            for line in lines:
                if line.startswith(id_sters):
                    gasit = True
                    continue
                new_lines.append(line)

            if not gasit:
                print("ID-ul materialului nu a fost gasit.")
            else:
                with open(DBmateriale, "w", encoding="utf-8") as f:
                    f.writelines(new_lines)
                print("Material sters cu succes.")

        elif selectie == "4":
           
            try:
                with open(DBmateriale, "r", encoding="utf-8") as f:
                    lines = f.readlines()
            except FileNotFoundError:
                print(f"Fisierul {DBmateriale} nu exista inca.")
                continue

            id_mat = input("Introduceti ID-ul materialului de modificat: ")

            id_gasit = False
            for index, line in enumerate(lines):
                if line.startswith(id_mat):
                    print("Inregistrarea curenta:")
                    print(line)
                    print("Introduceti noile date pentru material:")

                    new_id = input("Introduceti ID-ul materialului: ")
                    for i in range(len(new_id), 4):
                        new_id += " "

                    nume = input("Introduceti numele materialului: ")
                    for i in range(len(nume), 20):
                        nume += " "

                    an_dare = input("Introduceti anul dării în folosinta: ")
                    for i in range(len(an_dare), 6):
                        an_dare += " "

                    nr_folosiri = input("Introduceti numarul de folosiri: ")
                    for i in range(len(nr_folosiri), 6):
                        nr_folosiri += " "

                    stare = input("Introduceti starea materialului: ")

                    entry = f"{new_id}|{nume}|{an_dare}|{nr_folosiri}|{stare}\n"
                    lines[index] = entry
                    id_gasit = True
                    break

            if not id_gasit:
                print("ID-ul materialului nu a fost gasit.")
            else:
                with open(DBmateriale, "w", encoding="utf-8") as f:
                    f.writelines(lines)
                print("Material modificat cu succes.")

        elif selectie == "5":
           
            pass
        else:
            print("Optiune invalida. Incercati din nou.")

        sort_file(DBmateriale, header)

#main loop

def main():
    print("Bine ati venit la aplicatia de gestionare a colegiului Moldova!")
    selectie=""
    while selectie not in ["1", "2", "3", "4", "5"]:
        os.system('cls' if os.name == 'nt' else 'clear')
        selectie=input("Acesati baza de date pentru: \n1. Arbitri\n2. Sedinte\n3. Raliuri\n4. Materiale\n5. Inchideti aplicatia\n\n")
        match selectie:
            case "1":
                arbitri()
            case "2":
                sedinte()
            case "3":
                delegari()
            case "4":
                materiale()
            case "5":
                print("La revedere!")
                return
        selectie=""

main()