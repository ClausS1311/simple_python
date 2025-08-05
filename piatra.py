import random
piatra = "🪨🪨🪨"
foarfeca = "✂️✂️✂️"
hartie = "📜📜📜"
a = int(input("alege 0.piatra,1.foarfeca, 2.hartie\n "))
# 0 piatra 1 foarfeca 2 hartie

imagini = [piatra,  foarfeca, hartie]
if a > 2 or a < 0:
    print("numar gresit")
else:
    print(imagini[a])

    com = random.randint(0, 2)

    print(f"pc choise {com} \n ")
    print(imagini[com])

    if a == com:
        print("egal")
    elif a == 0 and com == 1:
        print("ai castigat\n")
    elif a == 1 and com == 0:
        print("ai pierdut")
    elif a == com:
        print("nul,egal")
    elif a > com:
        print("ai castigat")
    elif com > a:
        print("ai pierdut")
