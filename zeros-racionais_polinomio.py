def sup(val):
    val = str(val)
    if len(val) == 1:
        if val == 1:
            print(chr(0x00b9), end=' ')
        elif 2 <= int(val) <= 3:
            print(chr(0x00b0 + int(val)), end=' ')
        else:
            print(chr(0x2070 + int(val)), end=' ')
    else:
        n = list()
        for c2 in range(0, len(val)):
            n.append(val[c2])
        for cont in range(0, len(val)):
            if val == 1:
                print(chr(0x00b9), end='')
            elif 2 <= int(val) <= 3:
                a = n[cont]
                print(chr(0x00b0 + int(a)), end='')
            else:
                print(chr(0x2070 + int(val[cont])), end='')
        print(end=' ')


print('\033[35m=-'*20+'=')
print("{:^41}".format("ZEROS RACIONAIS DE UM POLINÓMIO"))
print('=-'*20+'=\033[m')
print()

while True:
    g = int(input("\033[36mDigite o grau do polinómio: \033[m"))
    if g < 0:
        while g < 0:
            print("\033[31mERRO!!! DADO INVÁLIDO!!!\033[m")
            g = int(input('Digite novamente: '))
    if g == 0:
        c = int(input("Digite o coeficiente do termo de grau 0: "))
        if c != 0:
            while c != 0:
                print("\033[31mERRO!!! Neste caso não pode ser 0!!!\033[m")
                c = int(input('Digite novamente: '))
        print("Este polinómio não tem zeros racionais!!!")
    elif g > 0:
        c = list()
        for i in range(g, -1, -1):
            print("Digite o coeficiente do termo de grau {}".format(i), end='')
            c.append(int(input(": ")))
            if i == g and c[0] == 0:
                while i == g and c[0] == 0:
                    print("\033[31mERRO!!! Neste caso não pode ser 0!!!\033[m")
                    c[0] = int(input('Digite novamente: '))
        c.reverse()
        print()
        print("f(x) = ", end='')
        for i in range(g, -1, -1):
            if c[i] == 0:
                print(end='')
            else:
                if i == 0:
                    if i == g:
                        print("{}".format(c[i]), end=' ')
                    else:
                        if c[i] > 0:
                            print("+", end=' ')
                            print("{}".format(c[i]), end=' ')
                        else:
                            ct = 0 - c[i]
                            print("-", end=' ')
                            print("{}".format(ct), end=' ')
                elif i == 1:
                    if i == g:
                        print("{}x".format(c[i]), end=' ')
                    else:
                        if c[i] > 0:
                            print("+", end=' ')
                            print("{}x".format(c[i]), end=' ')
                        else:
                            ct = 0 - c[i]
                            print("-", end=' ')
                            print("{}x".format(ct), end=' ')
                else:
                    if i == g:
                        print("{}x".format(c[i]), end='')
                    else:
                        if c[i] > 0:
                            print("+", end=' ')
                            print("{}x".format(c[i]), end='')
                        else:
                            ct = 0 - c[i]
                            print("-", end=' ')
                            print("{}x".format(ct), end='')
                    sup(i)
        print()
        print()
        z = list()
        while True:
            if c[0] == 0:
                c.pop(0)
                g = g - 1
                if 0.0 not in z:
                    z.append(float(0))
            else:
                break
        if c[0] > 0:
            a0 = 0 - c[0]
        else:
            a0 = c[0]
        if c[-1] > 0:
            an = 0 - c[-1]
        else:
            an = c[-1]
        for i in range(a0, (0-a0)+1):
            p = i
            for i2 in range(an, (0-an)+1):
                if i2 != 0:
                    q = i2
                    pq = p/q
                    v = 0
                    for i3 in range(g, -1, -1):
                        if i3 != 0:
                            v = v + (c[i3] * (pq**i3))
                        else:
                            v += c[i3]
                    if v == 0:
                        if pq not in z:
                            z.append(pq)
        z.sort()
        if len(z) == 0:
            print("Este polinómio não tem zeros racionais!")
        else:
            print("Zeros racionais de f(x): {", end='')
            for i in range(0, len(z)):
                if i == len(z) - 1:
                    print(z[i], end='')
                    print("}")
                else:
                    print(z[i], end=', ')
            print()
    r = str(input("\033[33mDeseja ver os zeros racionais de outro polinómio? [S/N] \033[m"))
    if r.upper() not in "SN":
        while r.upper() not in 'SN':
            print("\033[31mERRO!!! DADO INVÁLIDO!!!\033[m")
            r = str(input('Digite novamente: '))
    if r.upper() == "S":
        print()
    elif r.upper() == "N":
        break
print("Obrigado por usar o programa!!!")
