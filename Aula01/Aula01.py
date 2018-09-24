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


x = input('Escreve um valor inteiro')
le_inteiro(x)


def apaga_ocorrencias(t, value):
    lenTuplo = 0
    newTuplo = ()
    while len(t) < lenTuplo - 1:
        if t[lenTuplo] == value:
            newTuplo = newTuplo + t[lenTuplo]
    print(newTuplo)

print("-------------------")
apaga_ocorrencias((1, 2, 2, 3, 4, 9), 10)
