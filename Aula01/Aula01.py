sum = 0
for i in range(1, 10):
    if i % 3 == 0 or i % 5 == 0:
        sum += i


def le_inteiro(x):
    try:
        integerVal = int(x)
        soma_digitos(x)
    except ValueError:
        print("InValid input")


def soma_digitos(x):
    size = len(x)
    sum = 0
    for i in range(0, size):
        sum += int(x[i])
    print(sum)


# x = input('Escreve um valor inteiro')
# le_inteiro(x)


def apaga_ocorrencias(tuplo, inteiro):
    mylist = []
    for x in range(len(tuplo)):
        if tuplo[x] != inteiro:
            mylist.append(tuplo[x])
    mytuple = tuple(mylist)
    print(mytuple)


tuplo = ('r', 30, 30, 22, 234324, 244, 23432, 4, 324, 32, 4, 23)

print(apaga_ocorrencias(tuplo, 30))
