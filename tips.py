pret = float(input("ai de plata = "))
tips = int(input("ca procent cat bacsisi vrei sa dai "))
pers = int(input("cate persoane sunteti "))
bacsis = pret * (tips/100)
print(
    f"pretul total cu tot cu bacis la un nr de {pers} este {round((bacsis+pret)/pers)} \n totalul cu tot cu tips este {round(pret+bacsis)} ")
