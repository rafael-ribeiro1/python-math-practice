from time import sleep
while True:
    g = int(input("Grau do binómio (a+b): "))
    if g < 1:
        while g < 1:
            print("\033[31mERRO!!!\033[m")
            g = int(input("Digite um valor maior ou igual a 1: "))
    print("\033[34mBinómio:\033[35m (a+b)^{}\033[m".format(g))
    print("\033[32mDESENVOLVENDO...")
    for c in range(0, 4):
        sleep(0.5)
        print(".")
    print("\033[36mSIMPLIFICANDO...")
    for c in range(0, 4):
        sleep(0.5)
        print(".")
    print("\033[m")
    print("\033[33mSimplificação:\033[31m ", end='')
    if g == 1:
        print("a+b\033[m")
    else:
        print("a^{}".format(g), end='')
        n = 1
        for m in range(g, 1, -1):
            fg = 1
            fmn = 1
            fn = 1
            for f1 in range(g, 0, -1):
                fg = fg * f1
            for f2 in range(g-n, 0, -1):
                fmn = fmn * f2
            for f3 in range(n, 0, -1):
                fn = fn * f3
            mQn = fg / (fmn * fn)
            print(" + {:.0f}a^{}b^{}".format(mQn, m-1, n), end='')
            n = n + 1
        print(" + b^{}\033[m".format(g))
    r = str(input("Deseja simplificar outro binómio? [S/N] "))
    if r.upper() not in "SN":
        while r.upper() not in "SN":
            print("\033[31mERRO!!!\033[m")
            r = str(input("Digite novamente: "))
    if r.upper() == "S":
        print()
    elif r.upper() == "N":
        break
print("\033[33mENCERRANDO O PROGRAMA...\033[m")
