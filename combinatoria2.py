print("\033[33m=-"*5 + "=", end=' ')
print("COMBINATÓRIA", end=' ')
print("=-"*5 + "=\033[m")
while True:
    print("\033[35m=-"*15+"=")
    print(" 1 - Combinações")
    print(" 2 - Arranjos sem repetição")
    print(" 3 - Arranjos com repetição")
    print("=-"*15+"=\033[m")
    a = int(input("Digite o número da ação a executar: "))
    if a < 1 or a > 3:
        while a < 1 or a > 3:
            print("\033[31mERRO!!! DADO INVÁLIDO!!!\033[m")
            a = int(input("Digite novamente: "))
    if a == 1:
        print("\033[31mSegundo a notação nCp,")
        n = int(input("\033[32mDigite \033[31mn\033[32m: "))
        p = int(input("\033[32mDigite \033[31mp\033[32m: "))
        if p > n:
            while p > n:
                print("\033[31mERRO!!! DADO INVÁLIDO!!!\033[m")
                p = int(input("Digite novamente: "))
        fn = fnmp = fp = 1
        for c1 in range(n, 0, -1):
            fn = fn * c1
        for c2 in range(n-p, 0, -1):
            fnmp = fnmp * c2
        for c3 in range(p, 0, -1):
            fp = fp * c3
        nCp = fn / (fnmp * fp)
        print("\033[34mExistem \033[36m{:.0f}\033[34m combinações de {} elementos {} a {}".format(nCp, n, p, p))
        s = nCp
        while True:
            print("\033[35m=-" * 15 + "=")
            print(" 1 - Soma")
            print(" 2 - Multiplicação")
            print(" 3 - Nenhum")
            print("=-" * 15 + "=\033[m")
            a2 = int(input("Digite o número da ação a realizar: "))
            if a2 < 1 or a2 > 3:
                while a2 < 1 or a2 > 3:
                    print("\033[31mERRO!!! DADO INVÁLIDO!!!\033[m")
                    a2 = int(input("Digite novamente: "))
            if a2 == 1:
                print("\033[35m=-" * 15 + "=")
                print(" 1 - Combinações")
                print(" 2 - Arranjos sem repetição")
                print(" 3 - Arranjos com repetição")
                print("=-" * 15 + "=\033[m")
                a3 = int(input("Digite o número da ação a executar: "))
                if a3 < 1 or a3 > 3:
                    while a3 < 1 or a3 > 3:
                        print("\033[31mERRO!!! DADO INVÁLIDO!!!\033[m")
                        a = int(input("Digite novamente: "))
                if a3 == 1:
                    print("\033[31mSegundo a notação nCp,")
                    n = int(input("\033[32mDigite \033[31mn\033[32m: "))
                    p = int(input("\033[32mDigite \033[31mp\033[32m: "))
                    if p > n:
                        while p > n:
                            print("\033[31mERRO!!! DADO INVÁLIDO!!!\033[m")
                            p = int(input("Digite novamente: "))
                    fn = fnmp = fp = 1
                    for c1 in range(n, 0, -1):
                        fn = fn * c1
                    for c2 in range(n - p, 0, -1):
                        fnmp = fnmp * c2
                    for c3 in range(p, 0, -1):
                        fp = fp * c3
                    nCp = fn / (fnmp * fp)
                    s = s + nCp
                    print("A soma é igual a \033[32m{:.0f}\033[m".format(s))
                    r2 = str(input("Deseja executar outra ação? [S/N] "))
                    if r2.upper() not in "SN":
                        while r2.upper() not in "SN":
                            print("\033[31mERRO!!! DADO INVÁLIDO!!!\033[m")
                            r2 = str(input("Digite novamente: "))
                    if r2.upper() == "S":
                        print()
                    elif r2.upper() == "N":
                        break
                elif a3 == 2:
                    print("\033[31mSegundo a notação nAp,")
                    n = int(input("\033[32mDigite \033[31mn\033[32m: "))
                    p = int(input("\033[32mDigite \033[31mp\033[32m: "))
                    if p > n:
                        while p > n:
                            print("\033[31mERRO!!! DADO INVÁLIDO!!!\033[m")
                            p = int(input("Digite novamente: "))
                    fn = fnmp = 1
                    for c1 in range(n, 0, -1):
                        fn = fn * c1
                    for c2 in range(n - p, 0, -1):
                        fnmp = fnmp * c2
                    nAp = fn / fnmp
                    s = s + nAp
                    print("A soma é igual a \033[32m{:.0f}\033[m".format(s))
                    r2 = str(input("Deseja executar outra ação? [S/N] "))
                    if r2.upper() not in "SN":
                        while r2.upper() not in "SN":
                            print("\033[31mERRO!!! DADO INVÁLIDO!!!\033[m")
                            r2 = str(input("Digite novamente: "))
                    if r2.upper() == "S":
                        print()
                    elif r2.upper() == "N":
                        break
                elif a3 == 3:
                    print("\033[31mSegundo a notação nA'p,")
                    n = int(input("\033[32mDigite \033[31mn\033[32m: "))
                    p = int(input("\033[32mDigite \033[31mp\033[32m: "))
                    nArp = n ** p
                    s = s + nArp
                    print("A soma é igual a \033[32m{:.0f}\033[m".format(s))
                    r2 = str(input("Deseja executar outra ação? [S/N] "))
                    if r2.upper() not in "SN":
                        while r2.upper() not in "SN":
                            print("\033[31mERRO!!! DADO INVÁLIDO!!!\033[m")
                            r2 = str(input("Digite novamente: "))
                    if r2.upper() == "S":
                        print()
                    elif r2.upper() == "N":
                        break
            elif a2 == 2:
                print("\033[35m=-" * 15 + "=")
                print(" 1 - Combinações")
                print(" 2 - Arranjos sem repetição")
                print(" 3 - Arranjos com repetição")
                print("=-" * 15 + "=\033[m")
                a3 = int(input("Digite o número da ação a executar: "))
                if a3 < 1 or a3 > 3:
                    while a3 < 1 or a3 > 3:
                        print("\033[31mERRO!!! DADO INVÁLIDO!!!\033[m")
                        a = int(input("Digite novamente: "))
                if a3 == 1:
                    print("\033[31mSegundo a notação nCp,")
                    n = int(input("\033[32mDigite \033[31mn\033[32m: "))
                    p = int(input("\033[32mDigite \033[31mp\033[32m: "))
                    if p > n:
                        while p > n:
                            print("\033[31mERRO!!! DADO INVÁLIDO!!!\033[m")
                            p = int(input("Digite novamente: "))
                    fn = fnmp = fp = 1
                    for c1 in range(n, 0, -1):
                        fn = fn * c1
                    for c2 in range(n - p, 0, -1):
                        fnmp = fnmp * c2
                    for c3 in range(p, 0, -1):
                        fp = fp * c3
                    nCp = fn / (fnmp * fp)
                    s = s * nCp
                    print("A multiplicação é igual a \033[32m{:.0f}\033[m".format(s))
                    r2 = str(input("Deseja executar outra ação? [S/N] "))
                    if r2.upper() not in "SN":
                        while r2.upper() not in "SN":
                            print("\033[31mERRO!!! DADO INVÁLIDO!!!\033[m")
                            r2 = str(input("Digite novamente: "))
                    if r2.upper() == "S":
                        print()
                    elif r2.upper() == "N":
                        break
                elif a3 == 2:
                    print("\033[31mSegundo a notação nAp,")
                    n = int(input("\033[32mDigite \033[31mn\033[32m: "))
                    p = int(input("\033[32mDigite \033[31mp\033[32m: "))
                    if p > n:
                        while p > n:
                            print("\033[31mERRO!!! DADO INVÁLIDO!!!\033[m")
                            p = int(input("Digite novamente: "))
                    fn = fnmp = 1
                    for c1 in range(n, 0, -1):
                        fn = fn * c1
                    for c2 in range(n - p, 0, -1):
                        fnmp = fnmp * c2
                    nAp = fn / fnmp
                    s = s * nAp
                    print("A multiplicação é igual a \033[32m{:.0f}\033[m".format(s))
                    r2 = str(input("Deseja executar outra ação? [S/N] "))
                    if r2.upper() not in "SN":
                        while r2.upper() not in "SN":
                            print("\033[31mERRO!!! DADO INVÁLIDO!!!\033[m")
                            r2 = str(input("Digite novamente: "))
                    if r2.upper() == "S":
                        print()
                    elif r2.upper() == "N":
                        break
                elif a3 == 3:
                    print("\033[31mSegundo a notação nA'p,")
                    n = int(input("\033[32mDigite \033[31mn\033[32m: "))
                    p = int(input("\033[32mDigite \033[31mp\033[32m: "))
                    nArp = n ** p
                    s = s * nArp
                    print("A multiplicação é igual a \033[32m{:.0f}\033[m".format(s))
                    r2 = str(input("Deseja executar outra ação? [S/N] "))
                    if r2.upper() not in "SN":
                        while r2.upper() not in "SN":
                            print("\033[31mERRO!!! DADO INVÁLIDO!!!\033[m")
                            r2 = str(input("Digite novamente: "))
                    if r2.upper() == "S":
                        print()
                    elif r2.upper() == "N":
                        break
            elif a2 == 3:
                break
    elif a == 2:
        print("\033[31mSegundo a notação nAp,")
        n = int(input("\033[32mDigite \033[31mn\033[32m: "))
        p = int(input("\033[32mDigite \033[31mp\033[32m: "))
        if p > n:
            while p > n:
                print("\033[31mERRO!!! DADO INVÁLIDO!!!\033[m")
                p = int(input("Digite novamente: "))
        fn = fnmp = 1
        for c1 in range(n, 0, -1):
            fn = fn * c1
        for c2 in range(n-p, 0, -1):
            fnmp = fnmp * c2
        nAp = fn / fnmp
        print("\033[34mExistem \033[36m{:.0f}\033[34m arranjos (sem repetição) de {} elementos {} a {}".format(nAp, n, p, p))
        s = nAp
        while True:
            print("\033[35m=-" * 15 + "=")
            print(" 1 - Soma")
            print(" 2 - Multiplicação")
            print(" 3 - Nenhum")
            print("=-" * 15 + "=\033[m")
            a2 = int(input("Digite o número da ação a realizar: "))
            if a2 < 1 or a2 > 3:
                while a2 < 1 or a2 > 3:
                    print("\033[31mERRO!!! DADO INVÁLIDO!!!\033[m")
                    a2 = int(input("Digite novamente: "))
            if a2 == 1:
                print("\033[35m=-" * 15 + "=")
                print(" 1 - Combinações")
                print(" 2 - Arranjos sem repetição")
                print(" 3 - Arranjos com repetição")
                print("=-" * 15 + "=\033[m")
                a3 = int(input("Digite o número da ação a executar: "))
                if a3 < 1 or a3 > 3:
                    while a3 < 1 or a3 > 3:
                        print("\033[31mERRO!!! DADO INVÁLIDO!!!\033[m")
                        a = int(input("Digite novamente: "))
                if a3 == 1:
                    print("\033[31mSegundo a notação nCp,")
                    n = int(input("\033[32mDigite \033[31mn\033[32m: "))
                    p = int(input("\033[32mDigite \033[31mp\033[32m: "))
                    if p > n:
                        while p > n:
                            print("\033[31mERRO!!! DADO INVÁLIDO!!!\033[m")
                            p = int(input("Digite novamente: "))
                    fn = fnmp = fp = 1
                    for c1 in range(n, 0, -1):
                        fn = fn * c1
                    for c2 in range(n - p, 0, -1):
                        fnmp = fnmp * c2
                    for c3 in range(p, 0, -1):
                        fp = fp * c3
                    nCp = fn / (fnmp * fp)
                    s = s + nCp
                    print("A soma é igual a \033[32m{:.0f}\033[m".format(s))
                    r2 = str(input("Deseja executar outra ação? [S/N] "))
                    if r2.upper() not in "SN":
                        while r2.upper() not in "SN":
                            print("\033[31mERRO!!! DADO INVÁLIDO!!!\033[m")
                            r2 = str(input("Digite novamente: "))
                    if r2.upper() == "S":
                        print()
                    elif r2.upper() == "N":
                        break
                elif a3 == 2:
                    print("\033[31mSegundo a notação nAp,")
                    n = int(input("\033[32mDigite \033[31mn\033[32m: "))
                    p = int(input("\033[32mDigite \033[31mp\033[32m: "))
                    if p > n:
                        while p > n:
                            print("\033[31mERRO!!! DADO INVÁLIDO!!!\033[m")
                            p = int(input("Digite novamente: "))
                    fn = fnmp = 1
                    for c1 in range(n, 0, -1):
                        fn = fn * c1
                    for c2 in range(n - p, 0, -1):
                        fnmp = fnmp * c2
                    nAp = fn / fnmp
                    s = s + nAp
                    print("A soma é igual a \033[32m{:.0f}\033[m".format(s))
                    r2 = str(input("Deseja executar outra ação? [S/N] "))
                    if r2.upper() not in "SN":
                        while r2.upper() not in "SN":
                            print("\033[31mERRO!!! DADO INVÁLIDO!!!\033[m")
                            r2 = str(input("Digite novamente: "))
                    if r2.upper() == "S":
                        print()
                    elif r2.upper() == "N":
                        break
                elif a3 == 3:
                    print("\033[31mSegundo a notação nA'p,")
                    n = int(input("\033[32mDigite \033[31mn\033[32m: "))
                    p = int(input("\033[32mDigite \033[31mp\033[32m: "))
                    nArp = n ** p
                    s = s + nArp
                    print("A soma é igual a \033[32m{:.0f}\033[m".format(s))
                    r2 = str(input("Deseja executar outra ação? [S/N] "))
                    if r2.upper() not in "SN":
                        while r2.upper() not in "SN":
                            print("\033[31mERRO!!! DADO INVÁLIDO!!!\033[m")
                            r2 = str(input("Digite novamente: "))
                    if r2.upper() == "S":
                        print()
                    elif r2.upper() == "N":
                        break
            elif a2 == 2:
                print("\033[35m=-" * 15 + "=")
                print(" 1 - Combinações")
                print(" 2 - Arranjos sem repetição")
                print(" 3 - Arranjos com repetição")
                print("=-" * 15 + "=\033[m")
                a3 = int(input("Digite o número da ação a executar: "))
                if a3 < 1 or a3 > 3:
                    while a3 < 1 or a3 > 3:
                        print("\033[31mERRO!!! DADO INVÁLIDO!!!\033[m")
                        a = int(input("Digite novamente: "))
                if a3 == 1:
                    print("\033[31mSegundo a notação nCp,")
                    n = int(input("\033[32mDigite \033[31mn\033[32m: "))
                    p = int(input("\033[32mDigite \033[31mp\033[32m: "))
                    if p > n:
                        while p > n:
                            print("\033[31mERRO!!! DADO INVÁLIDO!!!\033[m")
                            p = int(input("Digite novamente: "))
                    fn = fnmp = fp = 1
                    for c1 in range(n, 0, -1):
                        fn = fn * c1
                    for c2 in range(n - p, 0, -1):
                        fnmp = fnmp * c2
                    for c3 in range(p, 0, -1):
                        fp = fp * c3
                    nCp = fn / (fnmp * fp)
                    s = s * nCp
                    print("A multiplicação é igual a \033[32m{:.0f}\033[m".format(s))
                    r2 = str(input("Deseja executar outra ação? [S/N] "))
                    if r2.upper() not in "SN":
                        while r2.upper() not in "SN":
                            print("\033[31mERRO!!! DADO INVÁLIDO!!!\033[m")
                            r2 = str(input("Digite novamente: "))
                    if r2.upper() == "S":
                        print()
                    elif r2.upper() == "N":
                        break
                elif a3 == 2:
                    print("\033[31mSegundo a notação nAp,")
                    n = int(input("\033[32mDigite \033[31mn\033[32m: "))
                    p = int(input("\033[32mDigite \033[31mp\033[32m: "))
                    if p > n:
                        while p > n:
                            print("\033[31mERRO!!! DADO INVÁLIDO!!!\033[m")
                            p = int(input("Digite novamente: "))
                    fn = fnmp = 1
                    for c1 in range(n, 0, -1):
                        fn = fn * c1
                    for c2 in range(n - p, 0, -1):
                        fnmp = fnmp * c2
                    nAp = fn / fnmp
                    s = s * nAp
                    print("A multiplicação é igual a \033[32m{:.0f}\033[m".format(s))
                    r2 = str(input("Deseja executar outra ação? [S/N] "))
                    if r2.upper() not in "SN":
                        while r2.upper() not in "SN":
                            print("\033[31mERRO!!! DADO INVÁLIDO!!!\033[m")
                            r2 = str(input("Digite novamente: "))
                    if r2.upper() == "S":
                        print()
                    elif r2.upper() == "N":
                        break
                elif a3 == 3:
                    print("\033[31mSegundo a notação nA'p,")
                    n = int(input("\033[32mDigite \033[31mn\033[32m: "))
                    p = int(input("\033[32mDigite \033[31mp\033[32m: "))
                    nArp = n ** p
                    s = s * nArp
                    print("A multiplicação é igual a \033[32m{:.0f}\033[m".format(s))
                    r2 = str(input("Deseja executar outra ação? [S/N] "))
                    if r2.upper() not in "SN":
                        while r2.upper() not in "SN":
                            print("\033[31mERRO!!! DADO INVÁLIDO!!!\033[m")
                            r2 = str(input("Digite novamente: "))
                    if r2.upper() == "S":
                        print()
                    elif r2.upper() == "N":
                        break
            elif a2 == 3:
                break
    elif a == 3:
        print("\033[31mSegundo a notação nA'p,")
        n = int(input("\033[32mDigite \033[31mn\033[32m: "))
        p = int(input("\033[32mDigite \033[31mp\033[32m: "))
        nArp = n ** p
        print("\033[34mExistem \033[36m{:.0f}\033[34m arranjos com repetição de {} elementos {} a {}".format(nArp, n, p, p))
        s = nArp
        while True:
            print("\033[35m=-" * 15 + "=")
            print(" 1 - Soma")
            print(" 2 - Multiplicação")
            print(" 3 - Nenhum")
            print("=-" * 15 + "=\033[m")
            a2 = int(input("Digite o número da ação a realizar: "))
            if a2 < 1 or a2 > 3:
                while a2 < 1 or a2 > 3:
                    print("\033[31mERRO!!! DADO INVÁLIDO!!!\033[m")
                    a2 = int(input("Digite novamente: "))
            if a2 == 1:
                print("\033[35m=-" * 15 + "=")
                print(" 1 - Combinações")
                print(" 2 - Arranjos sem repetição")
                print(" 3 - Arranjos com repetição")
                print("=-" * 15 + "=\033[m")
                a3 = int(input("Digite o número da ação a executar: "))
                if a3 < 1 or a3 > 3:
                    while a3 < 1 or a3 > 3:
                        print("\033[31mERRO!!! DADO INVÁLIDO!!!\033[m")
                        a = int(input("Digite novamente: "))
                if a3 == 1:
                    print("\033[31mSegundo a notação nCp,")
                    n = int(input("\033[32mDigite \033[31mn\033[32m: "))
                    p = int(input("\033[32mDigite \033[31mp\033[32m: "))
                    if p > n:
                        while p > n:
                            print("\033[31mERRO!!! DADO INVÁLIDO!!!\033[m")
                            p = int(input("Digite novamente: "))
                    fn = fnmp = fp = 1
                    for c1 in range(n, 0, -1):
                        fn = fn * c1
                    for c2 in range(n - p, 0, -1):
                        fnmp = fnmp * c2
                    for c3 in range(p, 0, -1):
                        fp = fp * c3
                    nCp = fn / (fnmp * fp)
                    s = s + nCp
                    print("A soma é igual a \033[32m{:.0f}\033[m".format(s))
                    r2 = str(input("Deseja executar outra ação? [S/N] "))
                    if r2.upper() not in "SN":
                        while r2.upper() not in "SN":
                            print("\033[31mERRO!!! DADO INVÁLIDO!!!\033[m")
                            r2 = str(input("Digite novamente: "))
                    if r2.upper() == "S":
                        print()
                    elif r2.upper() == "N":
                        break
                elif a3 == 2:
                    print("\033[31mSegundo a notação nAp,")
                    n = int(input("\033[32mDigite \033[31mn\033[32m: "))
                    p = int(input("\033[32mDigite \033[31mp\033[32m: "))
                    if p > n:
                        while p > n:
                            print("\033[31mERRO!!! DADO INVÁLIDO!!!\033[m")
                            p = int(input("Digite novamente: "))
                    fn = fnmp = 1
                    for c1 in range(n, 0, -1):
                        fn = fn * c1
                    for c2 in range(n - p, 0, -1):
                        fnmp = fnmp * c2
                    nAp = fn / fnmp
                    s = s + nAp
                    print("A soma é igual a \033[32m{:.0f}\033[m".format(s))
                    r2 = str(input("Deseja executar outra ação? [S/N] "))
                    if r2.upper() not in "SN":
                        while r2.upper() not in "SN":
                            print("\033[31mERRO!!! DADO INVÁLIDO!!!\033[m")
                            r2 = str(input("Digite novamente: "))
                    if r2.upper() == "S":
                        print()
                    elif r2.upper() == "N":
                        break
                elif a3 == 3:
                    print("\033[31mSegundo a notação nA'p,")
                    n = int(input("\033[32mDigite \033[31mn\033[32m: "))
                    p = int(input("\033[32mDigite \033[31mp\033[32m: "))
                    nArp = n ** p
                    s = s + nArp
                    print("A soma é igual a \033[32m{:.0f}\033[m".format(s))
                    r2 = str(input("Deseja executar outra ação? [S/N] "))
                    if r2.upper() not in "SN":
                        while r2.upper() not in "SN":
                            print("\033[31mERRO!!! DADO INVÁLIDO!!!\033[m")
                            r2 = str(input("Digite novamente: "))
                    if r2.upper() == "S":
                        print()
                    elif r2.upper() == "N":
                        break
            elif a2 == 2:
                print("\033[35m=-" * 15 + "=")
                print(" 1 - Combinações")
                print(" 2 - Arranjos sem repetição")
                print(" 3 - Arranjos com repetição")
                print("=-" * 15 + "=\033[m")
                a3 = int(input("Digite o número da ação a executar: "))
                if a3 < 1 or a3 > 3:
                    while a3 < 1 or a3 > 3:
                        print("\033[31mERRO!!! DADO INVÁLIDO!!!\033[m")
                        a = int(input("Digite novamente: "))
                if a3 == 1:
                    print("\033[31mSegundo a notação nCp,")
                    n = int(input("\033[32mDigite \033[31mn\033[32m: "))
                    p = int(input("\033[32mDigite \033[31mp\033[32m: "))
                    if p > n:
                        while p > n:
                            print("\033[31mERRO!!! DADO INVÁLIDO!!!\033[m")
                            p = int(input("Digite novamente: "))
                    fn = fnmp = fp = 1
                    for c1 in range(n, 0, -1):
                        fn = fn * c1
                    for c2 in range(n - p, 0, -1):
                        fnmp = fnmp * c2
                    for c3 in range(p, 0, -1):
                        fp = fp * c3
                    nCp = fn / (fnmp * fp)
                    s = s * nCp
                    print("A multiplicação é igual a \033[32m{:.0f}\033[m".format(s))
                    r2 = str(input("Deseja executar outra ação? [S/N] "))
                    if r2.upper() not in "SN":
                        while r2.upper() not in "SN":
                            print("\033[31mERRO!!! DADO INVÁLIDO!!!\033[m")
                            r2 = str(input("Digite novamente: "))
                    if r2.upper() == "S":
                        print()
                    elif r2.upper() == "N":
                        break
                elif a3 == 2:
                    print("\033[31mSegundo a notação nAp,")
                    n = int(input("\033[32mDigite \033[31mn\033[32m: "))
                    p = int(input("\033[32mDigite \033[31mp\033[32m: "))
                    if p > n:
                        while p > n:
                            print("\033[31mERRO!!! DADO INVÁLIDO!!!\033[m")
                            p = int(input("Digite novamente: "))
                    fn = fnmp = 1
                    for c1 in range(n, 0, -1):
                        fn = fn * c1
                    for c2 in range(n - p, 0, -1):
                        fnmp = fnmp * c2
                    nAp = fn / fnmp
                    s = s * nAp
                    print("A multiplicação é igual a \033[32m{:.0f}\033[m".format(s))
                    r2 = str(input("Deseja executar outra ação? [S/N] "))
                    if r2.upper() not in "SN":
                        while r2.upper() not in "SN":
                            print("\033[31mERRO!!! DADO INVÁLIDO!!!\033[m")
                            r2 = str(input("Digite novamente: "))
                    if r2.upper() == "S":
                        print()
                    elif r2.upper() == "N":
                        break
                elif a3 == 3:
                    print("\033[31mSegundo a notação nA'p,")
                    n = int(input("\033[32mDigite \033[31mn\033[32m: "))
                    p = int(input("\033[32mDigite \033[31mp\033[32m: "))
                    nArp = n ** p
                    s = s * nArp
                    print("A multiplicação é igual a \033[32m{:.0f}\033[m".format(s))
                    r2 = str(input("Deseja executar outra ação? [S/N] "))
                    if r2.upper() not in "SN":
                        while r2.upper() not in "SN":
                            print("\033[31mERRO!!! DADO INVÁLIDO!!!\033[m")
                            r2 = str(input("Digite novamente: "))
                    if r2.upper() == "S":
                        print()
                    elif r2.upper() == "N":
                        break
            elif a2 == 3:
                break
    r = str(input("\033[mDeseja reiniciar o programa? [S/N] "))
    if r.upper() not in "SN":
        while r.upper() not in "SN":
            print("\033[31mERRO!!! DADO INVÁLIDO!!!\033[m")
            r = str(input("Digite novamente: "))
    if r.upper() == "S":
        print()
    elif r.upper() == "N":
        break
print("Obrigado por usar o programa!!!")
