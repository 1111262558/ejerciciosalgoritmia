humano=input("es humano:  ")
volar=input("puede volar:  ")
mascara=input("tiene mascara:  ")
if humano=="si"and volar=="si" and mascara=="si":
    print("Iroman")

elif humano=="si" and volar=="si" and mascara=="no":
    print("capitan marvel")

elif humano=="no" and volar=="si" and mascara=="si":
    print("ronan acuser")

elif humano=="no" and volar=="si" and mascara=="no":
    print("vision")

elif humano=="si" and volar=="no" and mascara=="si":
    print("spiderman")

elif humano=="si" and volar=="no" and mascara=="no":
    print("holk")

elif humano=="no" and volar=="no" and mascara=="si":
    print("blak bolt")

elif humano=="no" and volar=="no" and mascara=="no":
    print("thanos")


