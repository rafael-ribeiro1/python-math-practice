from math import sqrt
from math import acos
from math import degrees
from time import sleep
print("\033[32m=-"*10+"=", end=' ')
print("PRODUTO ESCALAR", end=' ')
print("=-"*10+"=\033[m")
while True:
    print("\033[35m=-" * 16 + "=")
    print("1 - oXY")
    print("2 - oXYZ")
    print("=-" * 16 + "=\033[m")
    d = int(input("Escolha o referencial: "))
    if d < 1 or d > 2:
        while d < 1 or d > 2:
            print("\033[31mERRO!!! DADO INVÁLIDO!!!\033[m")
            d = int(input("Digite novamente: "))
    if d == 1:
        v1 = list()
        v2 = list()
        v1.append(float(input("Coordenada \033[34mX\033[m do Vetor 1: ")))
        v1.append(float(input("Coordenada \033[34mY\033[m do Vetor 1: ")))
        v2.append(float(input("Coordenada \033[34mX\033[m do Vetor 2: ")))
        v2.append(float(input("Coordenada \033[34mY\033[m do Vetor 2: ")))
        pe = v1[0] * v2[0] + v1[1] * v2[1]
        print("O produto escalar entre os vetores ({}, {}) e ({}, {}) é {}".format(v1[0], v1[1], v2[0], v2[1], pe))
        print("=-" * 16 + "=")
        print("\033[35m1 - Norma do vetor 1")
        print("2 - Norma do vetor 2")
        print("3 - Ângulo entre os vetores\033[m")
        print("=-" * 16 + "=")
        while True:
            m = int(input("Ação a executar para estes vetores: "))
            if m < 1 or m > 3:
                while m < 1 or m > 3:
                    print("\033[31mERRO!!! DADO INVÁLIDO\033[m")
                    m = int(input("Digite novamente: "))
            if m == 1:
                n1 = sqrt((v1[0]) ** 2 + (v1[1]) ** 2)
                print("A norma do vetor 1 é {:.2f}".format(n1))
            elif m == 2:
                n2 = sqrt((v2[0]) ** 2 + (v2[1]) ** 2)
                print("A norma do vetor 2 é {:.2f}".format(n2))
            elif m == 3:
                n1 = sqrt((v1[0]) ** 2 + (v1[1]) ** 2)
                n2 = sqrt((v2[0]) ** 2 + (v2[1]) ** 2)
                av = pe / (n1 * n2)
                print("O ângulo entre os vetores é {:.2f}º".format(degrees(acos(av))))
            r = str(input("Deseja executar outra ação para estes vetores? [S/N] "))
            if r.upper() not in "SN":
                while r.upper() not in "SN":
                    print("\033[31mERRO!!! DADO INVÁLIDO\033[m")
                    m = int(input("Digite novamente: "))
            if r.upper() == "N":
                break
            if r.upper() == "S":
                print()
    elif d == 2:
        v1 = list()
        v2 = list()
        v1.append(float(input("Coordenada \033[34mX\033[m do Vetor 1: ")))
        v1.append(float(input("Coordenada \033[34mY\033[m do Vetor 1: ")))
        v1.append(float(input("Coordenada \033[34mZ\033[m do Vetor 1: ")))
        v2.append(float(input("Coordenada \033[34mX\033[m do Vetor 2: ")))
        v2.append(float(input("Coordenada \033[34mY\033[m do Vetor 2: ")))
        v2.append(float(input("Coordenada \033[34mZ\033[m do Vetor 2: ")))
        pe = v1[0] * v2[0] + v1[1] * v2[1] + v1[2] * v2[2]
        print("O produto escalar entre os vetores ({}, {}) e ({}, {}) é {}".format(v1[0], v1[1], v2[0], v2[1], pe))
        print("=-" * 16 + "=")
        print("\033[35m1 - Norma do vetor 1")
        print("2 - Norma do vetor 2")
        print("3 - Ângulo entre os vetores\033[m")
        print("=-" * 16 + "=")
        while True:
            m = int(input("Ação a executar para estes vetores: "))
            if m < 1 or m > 3:
                while m < 1 or m > 3:
                    print("\033[31mERRO!!! DADO INVÁLIDO\033[m")
                    m = int(input("Digite novamente: "))
            if m == 1:
                n1 = sqrt((v1[0]) ** 2 + (v1[1]) ** 2 + (v1[2]) ** 2)
                print("A norma do vetor 1 é {:.2f}".format(n1))
            elif m == 2:
                n2 = sqrt((v2[0]) ** 2 + (v2[1]) ** 2 + (v2[2]) ** 2)
                print("A norma do vetor 2 é {:.2f}".format(n2))
            elif m == 3:
                n1 = sqrt((v1[0]) ** 2 + (v1[1]) ** 2 + (v1[2]) ** 2)
                n2 = sqrt((v2[0]) ** 2 + (v2[1]) ** 2 + (v2[2]) ** 2)
                av = pe / (n1 * n2)
                print("O ângulo entre os vetores é {:.2f}º".format(degrees(acos(av))))
            r = str(input("Deseja executar outra ação para estes vetores? [S/N] "))
            if r.upper() not in "SN":
                while r.upper() not in "SN":
                    print("\033[31mERRO!!! DADO INVÁLIDO\033[m")
                    m = int(input("Digite novamente: "))
            if r.upper() == "N":
                break
            if r.upper() == "S":
                print()
    v = str(input("Deseja usar outros vetores? [S/N] "))
    if v.upper() not in "SN":
        while v.upper() not in "SN":
            print("\033[31mERRO!!! DADO INVÁLIDO\033[m")
            m = int(input("Digite novamente: "))
    if v.upper() == "S":
        print()
    elif v.upper() == "N":
        break
print("Obrigado por usar o programa!!!")
print("ENCERRANDO")
for c in range(0, 3):
    sleep(0.5)
    print(".")
