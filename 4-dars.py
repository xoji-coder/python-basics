    # Eng oddiy funksiya
# def salom():
#     print("Salom,Python")

#     # Parametrli funksiya
# def qoshish(a,b):
#     return a+b
# c = qoshish(3,7)
# print(c)

#     # Funksiya if
# def tekshir(son):
#     if son > 0:
#         return "Musbat"
#     elif son < 0:
#         return "Manfiy"
#     else:
#         return "Nol"
# print(tekshir(22))

#     # 1-vazifa
# ism = input("Ismingiz: ")
# def salom(ism):
#     print("Assalamu alaykum",ism)
# salom(ism)

    # 1-vazifa
# def salom(ism):
#     return f"Assalamu alaykum {ism}"
# ism = input("Ismingiz: ")
# print(salom(ism))

    # 2-vazifa
# def qoshish(son1,son2):
#     return son1+son2
# son1 = int(input("1-son: "))
# son2 = int(input("2-son: "))
# print(qoshish(son1,son2))

    # 3-vazifa
def tekshir(son):
    if son % 2 == 0:
        return "Juft"
    else:
        return "Toq"
print(tekshir(son=int(input("Butun son kiriting: "))))