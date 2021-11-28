from math import sqrt
while True:
    a = float(input("Digite o valor de a: "))
    if a == 0:
        while a == 0:
            print("\033[31mERRO!!! DADO INVÁLIDO!!!\033[m")
            a = float(input("Digite novamente: "))
    b = float(input("Digite o valor de b: "))
    c = float(input("Digite o valor de c: "))
    vr = (b**2) - 4*a*c
    if vr < 0:
        print("A equação não tem soluções!!!")
    else:
        s1 = ((0-b) + sqrt(vr))/(2*a)
        s2 = ((0-b) - sqrt(vr))/(2*a)
        print("x = {:.4f} ou x = {:.4f}".format(s1,s2))
    r = str(input("Quer resolver outra equação? [S/N] "))
    if r.upper() not in "SN":
        while r.upper() not in "SN":
            print("\033[31mERRO!!! DADO INVÁLIDO!!!\033[m")
            r = str(input("Digite novamente: "))
    if r.upper() == "S":
        print()
    elif r.upper() == "N":
        break
print("Obrigado por usar o programa!")
