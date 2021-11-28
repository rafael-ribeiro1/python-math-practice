print("\033[33m=-"*3 + "=", end=' ')
print("BINÓMIO DE NEWTON", end=' ')
print("=-"*3 + "=\033[m")
while True:                                         # Tipo de Binómio
    print("\033[35m=-" * 15 + "=")
    print(" 1 - (a+b)")
    print(" 2 - (a-b)")
    print("=-" * 15 + "=\033[m")
    tp = int(input("Digite o número do tipo de binómio que pretende: "))
    if tp < 1 or tp > 2:
        while tp < 1 or tp > 2:
            print("\033[31mERRO!!! DADO INVÁLIDO!!!\033[m")
            tp = int(input("Digite novamente: "))
    if tp == 1:                                     # a+b
        g = int(input("Digite o grau do binómio: "))
        if g < 1:
            while g < 1:
                print("\033[31mERRO!!! DADO INVÁLIDO!!! (grau>0)\033[m")
                g = int(input("Digite novamente: "))
        print("\033[35mSimplificação do binómio (a+b)^{}: ".format(g), end=' ')         # Simplificação (a+b)
        if g == 1:
            print("\033[31ma+b\033[m")
        else:
            p = 1
            for n in range(g, -1, -1):
                if n == g:
                    print("\033[31ma^{}".format(g), end=' ')
                    print("+", end=' ')
                elif n == 0:
                    print("b^{}\033[m".format(g))
                else:
                    fg = fgmp = fp = 1
                    for c1 in range(g, 0, -1):
                        fg = fg * c1
                    for c2 in range(g-p, 0, -1):
                        fgmp = fgmp * c2
                    for c3 in range(p, 0, -1):
                        fp = fp * c3
                    gCp = fg / (fgmp*fp)
                    print("{:.0f}a^{}b^{}".format(gCp, n, p), end=' ')
                    print("+", end=' ')
                    p = p + 1
            print()
        a = str(input("\033[32mDigite o valor de \033[31ma\033[32m: "))                  # a ; b
        b = str(input("\033[32mDigite o valor de \033[31mb\033[32m: "))
        print("\033[35mSubstituir \033[33ma\033[35m e \033[33mb\033[35m ({}+{})^{}: ".format(a, b, g), end=' ')
        if g == 1:
            print("\033[31m{}+{}\033[m".format(a, b))
        else:
            p = 1
            for n in range(g, -1, -1):
                if n == g:
                    print("\033[31m({})^{}".format(a, g), end=' ')
                    print("+", end=' ')
                elif n == 0:
                    print("({})^{}\033[m".format(b, g))
                else:
                    fg = fgmp = fp = 1
                    for c1 in range(g, 0, -1):
                        fg = fg * c1
                    for c2 in range(g - p, 0, -1):
                        fgmp = fgmp * c2
                    for c3 in range(p, 0, -1):
                        fp = fp * c3
                    gCp = fg / (fgmp * fp)
                    print("{:.0f}({})^{}({})^{}".format(gCp, a, n, b, p), end=' ')
                    print("+", end=' ')
                    p = p + 1
            print()
        print("\033[35mSimplificação do binómio ({}+{})^{}: ".format(a, b, g), end=' ')
        aa = a.isalpha()
        an = a.isnumeric()
        aan = a.isalnum()
        al = list()
        if aan is True and aa == an is False:
            num1 = str
            for c1 in range(0, len(a)):
                if a[c1].isnumeric() is True:
                    if c1 == 0:
                        num1 = a[c1]
                    else:
                        num1 = num1 + a[c1]
                elif a[c1].isalpha() is True:
                    al.append(int(num1))
                    al.append(a[c1])
        ba = b.isalpha()
        bn = b.isnumeric()
        ban = b.isalnum()
        bl = list()
        if ban is True and ba == bn is False:
            num2 = str
            for c2 in range(0, len(b)):
                if b[c2].isnumeric() is True:
                    if c2 == 0:
                        num2 = a[c2]
                    else:
                        num2 = num2 + a[c2]
                elif b[c2].isalpha() is True:
                    bl.append(int(num2))
                    bl.append(b[c2])
        if g == 1:
            if aa is False and an is True and ba is False and bn is True:
                s = int(a) + int(b)
                print("\033[31m{}\033[m".format(s))
            else:
                print("\033[31m{}+{}\033[m".format(a, b))
            print()
        else:
            p = 1
            for n in range(g, -1, -1):
                if n == g:
                    if aa is False and an is True:
                        print("\033[31m{}".format(int(a)**g), end=' ')
                    elif aa is True and an is False:
                        print("\033[31m{}^{}".format(a, g), end=' ')
                    else:
                        print("\033[31m{}{}^{}".format(al[0]**g, al[1], g), end=' ')
                    print("+", end=' ')
                elif n == 0:
                    if ba is False and bn is True:
                        print("\033[31m{}\033[m".format(int(b) ** g))
                    elif ba is True and bn is False:
                        print("{}^{}\033[m".format(b, g))
                    else:
                        print("\033[31m{}{}^{}\033[m".format(bl[0] ** g, bl[1], g))
                else:
                    fg = fgmp = fp = 1
                    for c1 in range(g, 0, -1):
                        fg = fg * c1
                    for c2 in range(g - p, 0, -1):
                        fgmp = fgmp * c2
                    for c3 in range(p, 0, -1):
                        fp = fp * c3
                    gCp = fg / (fgmp * fp)
                    if aa is False and an is True:                      # ####
                        if ba is False and bn is True:
                            print("{}".format(gCp*(int(a)**n)*(int(b)**p)), end=' ')
                        elif ba is True and bn is False:
                            print("{}{}^{}".format(gCp*(int(a)**n), b, p), end=' ')
                        else:
                            print("{}{}^{}".format(gCp*(int(a)**n)*(bl[0]**p), bl[1], p), end=' ')
                    elif aa is True and an is False:
                        if ba is False and bn is True:
                            print("{}{}^{}".format(gCp*(int(b)**p), a, n), end=' ')
                        elif ba is True and bn is False:
                            print("{}{}^{}{}^{}".format(gCp, a, n, b, p), end=' ')
                        else:
                            print("{}{}^{}{}^{}".format(gCp*(bl[0]**p), a, n, bl[1], p), end=' ')
                    else:
                        if ba is False and bn is True:
                            print("{}{}^{}".format(gCp*(al[0]**n)*(int(b)**p), al[1], n), end=' ')
                        elif ba is True and bn is False:
                            print("{}{}^{}{}^{}".format(gCp*(al[0]**n), al[1], n, b, p), end=' ')
                        else:
                            print("{}{}^{}{}^{}".format(gCp*(al[0]**n)*(bl[0]**p), al[1], n, bl[1], p), end=' ')
                    print("+", end=' ')
                    p = p + 1
            print()
    elif tp == 2:                                   # a-b
        g = int(input("Digite o grau do binómio: "))
        if g < 1:
            while g < 1:
                print("\033[31mERRO!!! DADO INVÁLIDO!!! (g>0)\033[m")
                g = int(input("Digite novamente: "))
        print("\033[35mSimplificação do binómio (a-b)^{}: ".format(g), end=' ')         # Simplificação (a-b)
        if g == 1:
            print("\033[31ma-b\033[m")
        else:
            p = 0
            for n in range(g, -1, -1):
                if n == g:
                    print("\033[31ma^{}".format(g), end=' ')
                    print("-", end=' ')
                    p = p + 1
                elif n == 0:
                    print("b^{}\033[m".format(g))
                else:
                    fg = fgmp = fp = 1
                    for c1 in range(g, 0, -1):
                        fg = fg * c1
                    for c2 in range(g - p, 0, -1):
                        fgmp = fgmp * c2
                    for c3 in range(p, 0, -1):
                        fp = fp * c3
                    gCp = fg / (fgmp * fp)
                    print("{:.0f}a^{}b^{}".format(gCp, n, p), end=' ')
                    if p % 2 == 0:
                        print("-", end=' ')
                    else:
                        print("+", end=' ')
                    p = p + 1
            print()
        a = str(input("\033[32mDigite o valor de \033[31ma\033[32m: "))                     # a ; b
        b = str(input("\033[32mDigite o valor de \033[31mb\033[32m: "))
        print("\033[35mSubstituir \033[33ma\033[35m e \033[33mb\033[35m ({}-{})^{}: ".format(a, b, g), end=' ')
        if g == 1:
            print("\033[31m{}-{}\033[m".format(a, b))
        else:
            p = 0
            for n in range(g, -1, -1):
                if n == g:
                    print("\033[31m({})^{}".format(a, g), end=' ')
                    print("+", end=' ')
                    p = p + 1
                elif n == 0:
                    print("({})^{}\033[m".format('-'+b, g))
                else:
                    fg = fgmp = fp = 1
                    for c1 in range(g, 0, -1):
                        fg = fg * c1
                    for c2 in range(g - p, 0, -1):
                        fgmp = fgmp * c2
                    for c3 in range(p, 0, -1):
                        fp = fp * c3
                    gCp = fg / (fgmp * fp)
                    print("{:.0f}({})^{}({})^{}".format(gCp, a, n, '-'+b, p), end=' ')
                    print("+", end=' ')
                    p = p + 1
            print()
        print("\033[35mSimplificação do binómio ({}-{})^{}: ".format(a, b, g), end=' ')
        aa = a.isalpha()
        an = a.isnumeric()
        aan = a.isalnum()
        al = list()
        if aan is True and aa == an is False:
            num1 = str
            for c1 in range(0, len(a)):
                if a[c1].isnumeric() is True:
                    if c1 == 0:
                        num1 = a[c1]
                    else:
                        num1 = num1 + a[c1]
                elif a[c1].isalpha() is True:
                    al.append(int(num1))
                    al.append(a[c1])
        ba = b.isalpha()
        bn = b.isnumeric()
        ban = b.isalnum()
        bl = list()
        if ban is True and ba == bn is False:
            num2 = str
            for c2 in range(0, len(b)):
                if b[c2].isnumeric() is True:
                    if c2 == 0:
                        num2 = a[c2]
                    else:
                        num2 = num2 + a[c2]
                elif b[c2].isalpha() is True:
                    bl.append(int(num2))
                    bl.append(b[c2])
        if g == 1:
            if aa is False and an is True and ba is False and bn is True:
                s = int(a) + int(b)
                print("\033[31m{}\033[m".format(s))
            elif bn is True:
                print("\033[31m{}{}\033[m".format(a, b))
            else:
                print("\033[31m{}+{}\033[m".format(a, b))
            print()
        else:
            p = 1
            for n in range(g, -1, -1):
                if n == g:
                    if aa is False and an is True:
                        print("\033[31m{}".format(int(a)**g), end=' ')
                    elif aa is True and an is False:
                        print("\033[31m{}^{}".format(a, g), end=' ')
                    else:
                        print("\033[31m{}{}^{}".format(al[0]**g, al[1], g), end=' ')
                elif n == 0:
                    if ba is False and bn is True:                     # ####
                        if p % 2 == 1:
                            print("- {}\033[m".format(int(b) ** g))
                        else:
                            print("+ {}\033[m".format(int(b) ** g))
                    elif ba is True and bn is False:
                        if p % 2 == 1:
                            print("- {}^{}\033[m".format(b, g))
                        else:
                            print("+ {}^{}\033[m".format(b, g))
                    else:
                        if p % 2 == 1:
                            print("- {}{}^{}\033[m".format(bl[0] ** g, bl[1], g))
                        else:
                            print("+ {}{}^{}\033[m".format(bl[0] ** g, bl[1], g))
                else:
                    fg = fgmp = fp = 1
                    for c1 in range(g, 0, -1):
                        fg = fg * c1
                    for c2 in range(g - p, 0, -1):
                        fgmp = fgmp * c2
                    for c3 in range(p, 0, -1):
                        fp = fp * c3
                    gCp = fg / (fgmp * fp)
                    if aa is False and an is True:                      # ####
                        if ba is False and bn is True:
                            if p % 2 == 1:
                                print("- {}".format(gCp * (int(a) ** n) * (int(b) ** p)), end=' ')
                            else:
                                print("+ {}".format(gCp * (int(a) ** n) * (int(b) ** p)), end=' ')
                        elif ba is True and bn is False:
                            if p % 2 == 1:
                                print("- {}{}^{}".format(gCp * (int(a) ** n), b, p), end=' ')
                            else:
                                print("+ {}{}^{}".format(gCp * (int(a) ** n), b, p), end=' ')
                        else:
                            if p % 2 == 1:
                                print("- {}{}^{}".format(gCp * (int(a) ** n) * (bl[0] ** p), bl[1], p), end=' ')
                            else:
                                print("+ {}{}^{}".format(gCp * (int(a) ** n) * (bl[0] ** p), bl[1], p), end=' ')
                    elif aa is True and an is False:
                        if ba is False and bn is True:
                            if p % 2 == 1:
                                print("- {}{}^{}".format(gCp * (int(b) ** p), a, n), end=' ')
                            else:
                                print("+ {}{}^{}".format(gCp * (int(b) ** p), a, n), end=' ')
                        elif ba is True and bn is False:
                            if p % 2 == 1:
                                print("- {}{}^{}{}^{}".format(gCp, a, n, b, p), end=' ')
                            else:
                                print("+ {}{}^{}{}^{}".format(gCp, a, n, b, p), end=' ')
                        else:
                            if p % 2 == 1:
                                print("- {}{}^{}{}^{}".format(gCp * (bl[0] ** p), a, n, bl[1], p), end=' ')
                            else:
                                print("+ {}{}^{}{}^{}".format(gCp * (bl[0] ** p), a, n, bl[1], p), end=' ')
                    else:
                        if ba is False and bn is True:
                            if p % 2 == 1:
                                print("- {}{}^{}".format(gCp * (al[0] ** n) * (int(b) ** p), al[1], n), end=' ')
                            else:
                                print("+ {}{}^{}".format(gCp * (al[0] ** n) * (int(b) ** p), al[1], n), end=' ')
                        elif ba is True and bn is False:
                            if p % 2 == 1:
                                print("- {}{}^{}{}^{}".format(gCp * (al[0] ** n), al[1], n, b, p), end=' ')
                            else:
                                print("+ {}{}^{}{}^{}".format(gCp * (al[0] ** n), al[1], n, b, p), end=' ')
                        else:
                            if p % 2 == 1:
                                print("- {}{}^{}{}^{}".format(gCp * (al[0] ** n) * (bl[0] ** p), al[1], n, bl[1], p), end=' ')
                            else:
                                print("+ {}{}^{}{}^{}".format(gCp * (al[0] ** n) * (bl[0] ** p), al[1], n, bl[1], p), end=' ')
                    p = p + 1
            print()
    r = str(input("Deseja simplificar outro binómio? [S/N] "))
    if r.upper() not in "SN":
        while r.upper() not in "SN":
            print("\033[31mERRO!!! DADO INVÁLIDO!!!\033[m")
            r = str(input("Digite novamente: "))
    if r.upper() == "S":
        print()
    elif r.upper() == "N":
        break
print("Obrigado por usar o programa!!!")
