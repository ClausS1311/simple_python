row1 = ["_", "_", "_"]
row2 = ["_", "_", "_"]
row3 = ["_", "_", "_"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
pos = input("pozitie")
v = int(pos[0])
o = int(pos[1])
map[v-1][o-1] = "X"
print(f"{row1}\n{row2}\n{row3}")
