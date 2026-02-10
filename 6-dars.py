    # Faylga yozish
# f = open("data.txt","w")
# f.write("Salom Python\n")
# f.close

#     # Faylni o'qish
# f = open("data.txt", "r")
# print(f.read())
# f.close()

#     # To'g'ri usul
# with open("data .txt", "a") as f:
#     f.write("Yangi qator\n")

# c=open("contacts.txt", "w")
# c.write("Ali:231\nVali:456")
# c.close()
# c=open("contacts.txt", "r")
# print(c.read())
# c.close()

# with open("contacts.txt", "w") as c:
#     c.write("Ali:123\nVali:456")

# with open("contacts.txt", "a") as c:
#     c.write("\nGuli:7890\nOlim:9900")

# with open("contacts.txt", "r") as c:
#     print(c.read())

ism = input("Ismingiz: ")
telefon = input("Telefon: ")
with open("contacts.txt", "a") as c:
    c.write(f"\n{ism}:{telefon}")

with open("contacts.txt", "r") as c:
    print(c.read())