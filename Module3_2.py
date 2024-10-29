def send_email(message, recipient, sender='university.help@gmail.com'):
    domains_ = ('.com', '.net', '.ru')
    if recipient.find('@') == -1 or sender.find('@') == -1 or recipient.endswith(domains_) == False or sender.endswith(
            domains_) == False:
        print(f'Невозможно отправить письмо с адреса {sender} на адрес {recipient}.')
    elif sender == recipient:
        print('Нельзя отправить письмо самому себе!')
    elif sender == 'university.help@gmail.com':
        print(f'Письмо успешно отправлено с адреса {sender} на адрес {recipient}.')
    elif sender != 'university.help@gmail.com':
        print(f'НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ!Письмо отправлено с адреса {sender} на адрес {recipient}.')


send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')

