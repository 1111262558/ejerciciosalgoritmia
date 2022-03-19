papel=3
tijera=2
piedra=1
p_1=int(input("digite puntaje de persona 1: "))
p_2=int(input("digite puntaje de persona 2: "))
if p_1==papel and p_2==piedra:
    print("p_1 ganador: papel emvuelve la piedra ")
elif p_1==papel and p_2==papel:
    print("empate entre papel")
elif p_1==papel and p_2==tijera:
    print("papel mata a tigera ")
elif p_1==papel and p_2==papel:
    print("empate entre papel")
elif p_1==tijera and p_2==tijera:
    print("empate entre tijera")
