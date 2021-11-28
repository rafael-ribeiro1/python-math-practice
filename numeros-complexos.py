import math


def convert_alg_trig(alg):
    re = alg[0]
    im = alg[1]
    r = math.sqrt(re**2 + im**2)
    arg = math.atan2(im, re)
    return [r, arg, 1]


def convert_trig_alg(trig):
    r = trig[0]
    arg = trig[1]
    re = r * math.cos(arg)
    im = r * math.sin(arg)
    return [re, im, 0]


def menu():
    print("\033[32m" + "-"*51)
    print("| 1 - Converter forma algébrica em trigonométrica |")
    print("| 2 - Converter forma trigonométrica em algébrica |")
    print("| 3 - Soma de dois números complexos              |")
    print("| 4 - Subtração de dois números complexos         |")
    print("| 5 - Multiplicação de dois números complexos     |")
    print("| 6 - Divisão de dois números complexos           |")
    print("| 7 - Potência de número complexo                 |")
    print("| 8 - Raízes de ordem n de número complexo        |")
    print("| 9 - Sair                                        |")
    print("-"*51 + "\033[m")
    print()
    nm = int(input("Tecla: "))
    if (nm < 1) or (nm > 9):
        while (nm < 1) or (nm > 9):
            print("\033[31mERRO! Digitou uma tecla inválida!\033[m")
            nm = int(input("Tecla: "))
    return nm


def complexo_input(txt):
    print("\033[36m-"*8)
    print("| " + txt)
    print("| \033[33m1 - Número complexo na forma algébrica")
    print("\033[36m| \033[33m2 - Número complexo na forma trigonométrica\033[36m")
    ncm = int(input("| \033[32mTecla: "))
    if (ncm < 1) or (ncm > 2):
        while (ncm < 1) or (ncm > 2):
            print("\033[36m| \033[31mERRO! Digitou uma tecla inválida!\033[36m")
            ncm = int(input("| \033[32mTecla: "))
    compl = []
    if ncm == 1:
        compl = alg_input()
    elif ncm == 2:
        compl = trig_input()
    return compl


def alg_input():
    re = float(input("\033[36m| \033[35mParte real: "))
    im = float(input("\033[36m| \033[35mParte imaginária: "))
    print("\033[36m-"*8 + "\033[m")
    return [re, im, 0]


def trig_input():
    r = float(input("\033[36m| \033[35mMódulo: "))
    if r < 0:
        while r < 0:
            print("\033[36m| \033[31mERRO! O módulo tem que ser positivo!")
            r = float(input("| \033[35mMódulo: "))
    arg = float(input("\033[36m| \033[35mArgumento principal (graus): "))
    if (arg <= -180) or (arg > 180):
        while (arg <= -180) or (arg > 180):
            print("\033[36m| \033[31mERRO! O argumento principal tem que estar entre -\u03C0 e \u03C0!")
            arg = float(input("| \033[35mArgumento principal: "))
    print("\033[36m-"*8 + "\033[m")
    return [r, math.radians(arg), 1]


def arg_prin(arg):
    if (arg <= -math.pi) or (arg > math.pi):
        while (arg <= -math.pi) or (arg > math.pi):
            if arg <= -math.pi:
                arg = arg + (2 * math.pi)
            if arg > math.pi:
                arg = arg - (2 * math.pi)
    return arg


print("\033[31m    Números Complexos")
print("-------------------------\033[m")
print()
print()
while True:
    nmenu = menu()
    if nmenu == 1:
        print("\033[36m-" * 8)
        print("| " + "Registe o número complexo")
        calg = alg_input()
        ctrig = convert_alg_trig(calg)
        ctrig[1] = arg_prin(ctrig[1])
        print("\033[36m| Número complexo na forma trigonométrica")
        print("| \033[33mMódulo: \033[32m{}".format(ctrig[0]))
        print("\033[36m| \033[33mArgumento principal (graus): \033[32m{}".format(math.degrees(ctrig[1])))
        print("\033[36m-" * 8 + "\033[m")
    elif nmenu == 2:
        print("\033[36m-" * 8)
        print("| " + "Registe o número complexo")
        ctrig = trig_input()
        calg = convert_trig_alg(ctrig)
        ctrig[1] = arg_prin(ctrig[1])
        print("\033[36m| Número complexo na forma algébrica")
        print("| \033[33mParte real: \033[32m{}".format(calg[0]))
        print("\033[36m| \033[33mParte imaginária: \033[32m{}".format(calg[1]))
        print("\033[36m-" * 8 + "\033[m")
    elif nmenu == 3:
        compl1 = complexo_input("Registe o primeiro número complexo")
        if compl1[2] == 1:
            compl1 = convert_trig_alg(compl1)
        compl2 = complexo_input("Registe o segundo número complexo")
        if compl2[2] == 1:
            compl2 = convert_trig_alg(compl2)
        sre = compl1[0] + compl2[0]
        sim = compl1[1] + compl2[1]
        compls = [sre, sim, 0]
        complstrig = convert_alg_trig(compls)
        complstrig[1] = arg_prin(complstrig[1])
        print("\033[36m| Número complexo na forma algébrica")
        print("| \033[33mParte real: \033[32m{}".format(compls[0]))
        print("\033[36m| \033[33mParte imaginária: \033[32m{}".format(compls[1]))
        print("\033[36m-" * 8 + "\033[m")
        print("\033[36m| Número complexo na forma trigonométrica")
        print("| \033[33mMódulo: \033[32m{}".format(complstrig[0]))
        print("\033[36m| \033[33mArgumento principal (graus): \033[32m{}".format(math.degrees(complstrig[1])))
        print("\033[36m-" * 8 + "\033[m")
    elif nmenu == 4:
        compl1 = complexo_input("Registe o primeiro número complexo")
        if compl1[2] == 1:
            compl1 = convert_trig_alg(compl1)
        compl2 = complexo_input("Registe o segundo número complexo")
        if compl2[2] == 1:
            compl2 = convert_trig_alg(compl2)
        sre = compl1[0] - compl2[0]
        sim = compl1[1] - compl2[1]
        compls = [sre, sim, 0]
        complstrig = convert_alg_trig(compls)
        complstrig[1] = arg_prin(complstrig[1])
        print("\033[36m| Número complexo na forma algébrica")
        print("| \033[33mParte real: \033[32m{}".format(compls[0]))
        print("\033[36m| \033[33mParte imaginária: \033[32m{}".format(compls[1]))
        print("\033[36m-" * 8 + "\033[m")
        print("\033[36m| Número complexo na forma trigonométrica")
        print("| \033[33mMódulo: \033[32m{}".format(complstrig[0]))
        print("\033[36m| \033[33mArgumento principal (graus): \033[32m{}".format(math.degrees(complstrig[1])))
        print("\033[36m-" * 8 + "\033[m")
    elif nmenu == 5:
        compl1 = complexo_input("Registe o primeiro número complexo")
        if compl1[2] == 0:
            compl1 = convert_alg_trig(compl1)
        compl2 = complexo_input("Registe o segundo número complexo")
        if compl2[2] == 0:
            compl2 = convert_alg_trig(compl2)
        mm = compl1[0] * compl2[0]
        marg = compl1[1] + compl2[1]
        complm = [mm, marg, 1]
        complmalg = convert_trig_alg(complm)
        complm[1] = arg_prin(complm[1])
        print("\033[36m| Número complexo na forma algébrica")
        print("| \033[33mParte real: \033[32m{}".format(complmalg[0]))
        print("\033[36m| \033[33mParte imaginária: \033[32m{}".format(complmalg[1]))
        print("\033[36m-" * 8 + "\033[m")
        print("\033[36m| Número complexo na forma trigonométrica")
        print("| \033[33mMódulo: \033[32m{}".format(complm[0]))
        print("\033[36m| \033[33mArgumento principal (graus): \033[32m{}".format(math.degrees(complm[1])))
        print("\033[36m-" * 8 + "\033[m")
    elif nmenu == 6:
        compl1 = complexo_input("Registe o primeiro número complexo")
        if compl1[2] == 0:
            compl1 = convert_alg_trig(compl1)
        compl2 = complexo_input("Registe o segundo número complexo")
        if compl2[2] == 0:
            compl2 = convert_alg_trig(compl2)
        mm = compl1[0] / compl2[0]
        marg = compl1[1] - compl2[1]
        complm = [mm, marg, 1]
        complmalg = convert_trig_alg(complm)
        complm[1] = arg_prin(complm[1])
        print("\033[36m| Número complexo na forma algébrica")
        print("| \033[33mParte real: \033[32m{}".format(complmalg[0]))
        print("\033[36m| \033[33mParte imaginária: \033[32m{}".format(complmalg[1]))
        print("\033[36m-" * 8 + "\033[m")
        print("\033[36m| Número complexo na forma trigonométrica")
        print("| \033[33mMódulo: \033[32m{}".format(complm[0]))
        print("\033[36m| \033[33mArgumento principal (graus): \033[32m{}".format(math.degrees(complm[1])))
        print("\033[36m-" * 8 + "\033[m")
    elif nmenu == 7:
        compl = complexo_input("Registe o número complexo")
        if compl[2] == 0:
            compl = convert_alg_trig(compl)
        n = int(input("Digite o valor do expoente: "))
        if n < 0:
            while n < 0:
                print("\033[36m| \033[31mERRO! O valor tem que ser positivo!")
                n = float(input("| \033[35mValor: "))
        pm = compl[0] ** n
        parg = compl[1] * n
        complp = [pm, parg, 1]
        complpalg = convert_trig_alg(complp)
        complp[1] = arg_prin(complp[1])
        print("\033[36m| Número complexo na forma algébrica")
        print("| \033[33mParte real: \033[32m{}".format(complpalg[0]))
        print("\033[36m| \033[33mParte imaginária: \033[32m{}".format(complpalg[1]))
        print("\033[36m-" * 8 + "\033[m")
        print("\033[36m| Número complexo na forma trigonométrica")
        print("| \033[33mMódulo: \033[32m{}".format(complp[0]))
        print("\033[36m| \033[33mArgumento principal (graus): \033[32m{}".format(math.degrees(complp[1])))
        print("\033[36m-" * 8 + "\033[m")
    elif nmenu == 8:
        compl = complexo_input("Registe o número complexo")
        if compl[2] == 0:
            compl = convert_alg_trig(compl)
        n = int(input("Digite o valor da ordem da raíz: "))
        if n < 0:
            while n < 0:
                print("\033[36m| \033[31mERRO! O valor tem que ser positivo!")
                n = float(input("| \033[35mValor: "))
        rm = compl[0] ** (1 / n)
        rarg = []
        for c in range(0, n):
            rarg.append((compl[1]/n) + ((2 * c * math.pi)/n))
            complr = [rm, rarg[c], 1]
            complralg = convert_trig_alg(complr)
            complr[1] = arg_prin(complr[1])
            print("\033[36m| Solução nº{} na forma algébrica".format(c))
            print("| \033[33mParte real: \033[32m{}".format(complralg[0]))
            print("\033[36m| \033[33mParte imaginária: \033[32m{}".format(complralg[1]))
            print("\033[36m-" * 8 + "\033[m")
            print("\033[36m| Solução nº{} na forma trigonométrica".format(c))
            print("| \033[33mMódulo: \033[32m{}".format(complr[0]))
            print("\033[36m| \033[33mArgumento principal (graus): \033[32m{}".format(math.degrees(complr[1])))
            print("\033[36m-" * 8 + "\033[m")
    elif nmenu == 9:
        break
    input("\033[35mClique ENTER para avançar . . .\033[m")
    print()
    print()
    print()
print()
print()
print("\033[35mPrograma encerrado . . .\033[m")
