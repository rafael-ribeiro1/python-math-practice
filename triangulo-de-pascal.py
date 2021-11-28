from math import factorial
print("\033[35m=-"*5+"=", end=' ')
print("TRIÂNGULO DE PASCAL", end=' ')
print("=-"*5+"=\033[m")
while True:
    l = int(input("Digite o número da linha: "))
    if l < 0:
        while l < 0:
            print("\033[31mERRO!!! DADO INVÁLIDO!!!\033[m")
            l = int(input("Digite novamnte: "))
    if l == 0:
        la = 0
        l = 1
        ls = 2
    else:
        la = l - 1
        ls = l + 1
    print("\033[32mL{}: \033[m".format(la),end=' ')
    p1 = 0
    for c1 in range(la, -1, -1):
        nCp = int(factorial(la)/(factorial(la-p1)*factorial(p1)))
        print("\033[36m"+str(nCp), end=' ')
        p1 += 1
    print()
    print("\033[32mL{}: \033[m".format(l), end=' ')
    p2 = 0
    for c2 in range(l, -1, -1):
        nCp = int(factorial(l) / (factorial(l - p2) * factorial(p2)))
        print("\033[36m" + str(nCp), end=' ')
        p2 += 1
    print()
    print("\033[32mL{}: \033[m".format(ls), end=' ')
    p3 = 0
    for c3 in range(ls, -1, -1):
        nCp = int(factorial(ls) / (factorial(ls - p3) * factorial(p3)))
        print("\033[36m" + str(nCp), end=' ')
        p3 += 1
    print()
    print()
    r = str(input("\033[mDeseja ver outra secção do triângulo de Pascal? [S/N] "))
    if r.upper() not in "SN":
        while r.upper() not in "SN":
            print("\033[31mERRO!!! DADO INVÁLIDO!!!\033[m")
            r = str(input("Digite novamnte: "))
    if r.upper() == "S":
        print()
    elif r.upper() == "N":
        break
print("Obrigado por usar o programa!!!")
