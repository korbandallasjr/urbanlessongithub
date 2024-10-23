number = int(input('Введите выпавшее в левом столбце число: '))
result = ''


def crack(number):
    global result
    for i in range(1, number):
        for j in range(1, number):
            if i >= j:
                continue
            else:
                multiple = number % (i + j)
            if multiple == 0:
                result = result + str(i) + str(j)
    return result


crack(number)
print(f'{number} - {result}')
