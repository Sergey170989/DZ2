def bank(X, Y):
    total = X
    for _ in range(Y):
        total += total * 0.1
    return total

X = int(input("Введите размер вклада: "))
Y = int(input("Введите срок вклада (в годах): "))

result = bank(X, Y)
print("Сумма на счету спустя", Y, "лет:", result)