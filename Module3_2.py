def send_email(message, recipient, sender='university.help@gmail.com'):
    splitted = recipient.split('.')
    splitted2 = sender.split('.')
    if sender == recipient:
        print('Нельзя отправить письмо самому себе!')
    elif splitted[-1] != 'com' and splitted[-1] != 'ru' and splitted[-1] != 'net':
        print(f'Невозможно отправить письмо с адреса {sender} на адрес {recipient}.')
    elif splitted2[-1] != 'com' and splitted2[-1] != 'ru' and splitted2[-1] != 'net':
        print(f'Невозможно отправить письмо с адреса {sender} на адрес {recipient}.')
    else:
        for character in recipient:
            if character == '@':
                for character in sender:
                    if character == '@':
                        if sender != '':
                            print(f'НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}.')
                        else:
                            print(f'Письмо успешно отправлено с адреса {sender} на адрес {recipient}.')


send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')
