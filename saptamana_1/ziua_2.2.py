def add(a, b):
    return a + b

def subt(a, b):
    return a - b

def mult(a, b):
    return a * b

def div(a, b):
    if b == 0:
        print("Nu se poate imparti la 0!")
        return None
    return a / b

def pow(a, b):
    return a ** b

def get_num():
    num1 = float(input("Introdu primul numar: "))
    num2 = float(input("Introdu al doilea numar: "))
    return num1, num2

print("Calculator")
print("Alege operatia:\n1. Adunare\n2. Scadere\n3. Inmultire\n4. Impartire\n5. Ridicare la putere\n0. Iesire")

option = input()

while option != '0':
    if option in ['1', '2', '3', '4', '5']:
        if option in ['1', '2', '3', '5']:
            num1, num2 = get_num()
        if option == '1':
            result = add(num1, num2)
            print("Rezultat:", result)
        elif option == '2':
            result = subt(num1, num2)
            print("Rezultat:", result)
        elif option == '3':
            result = mult(num1, num2)
            print("Rezultat:", result)
        elif option == '4':
            num1, num2 = get_num()
            result = div(num1, num2)
            if result is not None:
                print("Rezultat:", result)
        elif option == '5':
            result = pow(num1, num2)
            print("Rezultat:", result)
    else:
        print("Optiune invalida")

    print("\nAlege operatia:\n1. Adunare\n2. Scadere\n3. Inmultire\n4. Impartire\n5. Ridicare la putere\n0. Iesire")
    option = input()