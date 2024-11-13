def divide(first, second):
    result = ''
    if second == 0:
        result = 'Ошибка'
    else:
        result = float(first) / float(second)
    return result
