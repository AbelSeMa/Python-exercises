def factorial(num: int):
    acc = 1
    for x in range(1,num + 1):
        acc *= x

    print(acc)


factorial(10)