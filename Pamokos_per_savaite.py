mon = int(input("Įveskite pamokų skaičių pirmadienį "))
tue = int(input("Įveskite pamokų skaičių antradienį "))
wed = int(input("Įveskite pamokų skaičių trečuadienį "))
thu = int(input("Įveskite pamokų skaičių ketvirtadienį "))
fri = int(input("Įveskite pamokų skaičių penktadienį "))

pamoku_suma = mon + tue + wed + thu + fri
laikas_min = pamoku_suma*45

print(f"Pamokų skaičius: {pamoku_suma}")
print(f"Tai sudaro minučių: {laikas_min}")
