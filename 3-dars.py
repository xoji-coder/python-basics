    # 1-vazifa
for i in range(1,11):
    print(i)

i = 1
while i < 11:
    print(i)
    i += 1

    # 2-vazifa
son = 0
for i in range(5):
    son += int(input(f"{i+1}-son: "))
print(son)

    # 3-vazifa
juft_sonlar = []
toq_sonlar = []

sonlar = range(1,51)
for son in sonlar:
    if son % 2 == 0:
        juft_sonlar.append(son)
    else:
        toq_sonlar.append(son)
print("Juft sonlar",juft_sonlar)
print("\nToq sonlar",toq_sonlar)