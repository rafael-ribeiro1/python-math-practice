print("\033[32m=-"*3 + "=", end=' ')
print("Partes do conjunto", end=' ')
print("=-"*3 + "=\033[m")
while True:
    n = int(input("\033[35mDigite o número de elementos do conjunto: \033[m"))
    if n < 1:
        while n < 1:
            print("\033[31mERRO!!! DADO INVÁLIDO!!!")
            n = int(input("Digite novamente: "))
    while True:
        print("\033[36m=-"*10 + "=")
        print(" 1 - Total de partes do conjunto")
        print(" 2 - Partes do conjunto (excluindo sub-conjunto vazio)")
        print(" 3 - Número de sub-conjuntos com com n elementos")
        print("=-"*10 + "=\033[m")
        a = int(input("Digite o número da ação a realizar: "))
        if a < 1 or a > 3:
            while a < 1 or a > 3:
                print("\033[31mERRO!!! DADO INVÁLIDO!!!\033[m")
                a = int(input("Digite novamente: "))
        if a == 1:
            pc = 2 ** n
            print("\033[32mO total de partes do conjunto é {}.\033[m".format(pc))
            r2 = str(input("Deseja executar outra ação? [S/N] "))
            if r2.upper() not in "SN":
                while r2.upper() not in "SN":
                    print("\033[31mERRO!!! DADO INVÁLIDO!!!\033[m")
                    r2 = str(input("Digite novamente: "))
            if r2.upper() == "S":
                print()
            elif r2.upper() == "N":
                break
        if a == 2:
            pcs = (2 ** n) - 1
            print("\033[32mO total de partes do conjunto sem o sub-conjunto vazio é {}.\033[m".format(pcs))
            r2 = str(input("Deseja executar outra ação? [S/N] "))
            if r2.upper() not in "SN":
                while r2.upper() not in "SN":
                    print("\033[31mERRO!!! DADO INVÁLIDO!!!\033[m")
                    r2 = str(input("Digite novamente: "))
            if r2.upper() == "S":
                print()
            elif r2.upper() == "N":
                break
        if a == 3:
            ne = int(input("Digite o número de elementos para descobrir o número de sub-conjuntos: "))
            if ne < 0 or ne > n:
                while ne < 0 or ne > n:
                    print("\033[31mERRO!!! DADO INVÁLIDO!!!\033[m")
                    ne = int(input("Digite novamente: "))
            if ne == 0 or ne == n:
                nQi = 1
            else:
                fn = 1
                fnmi = 1
                fi = 1
                for c1 in range(n, 0, -1):
                    fn = fn * c1
                for c2 in range(n-ne, 0, -1):
                    fnmi = fnmi * c2
                for c3 in range(ne, 0, -1):
                    fi = fi * c3
                nQi = fn / (fnmi * fi)
            print("\033[32mExistem {} sub-conjuntos com {} elementos.\033[m".format(nQi, n))
            r2 = str(input("Deseja executar outra ação? [S/N] "))
            if r2.upper() not in "SN":
                while r2.upper() not in "SN":
                    print("\033[31mERRO!!! DADO INVÁLIDO!!!\033[m")
                    r2 = str(input("Digite novamente: "))
            if r2.upper() == "S":
                print()
            elif r2.upper() == "N":
                break
    r3 = str(input("Deseja usar outro conjunto? [S/N] "))
    if r3.upper() not in "SN":
        while r3.upper() not in "SN":
            print("\033[31mERRO!!! DADO INVÁLIDO!!!\033[m")
            r3 = str(input("Digite novamente: "))
    if r3.upper() == "S":
        print()
    elif r3.upper() == "N":
        break
print("Obrigado por usar o programa!!!")
