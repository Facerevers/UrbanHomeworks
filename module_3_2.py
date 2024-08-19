def checking(recipient, sender):
    chkrec: bool = False
    chksen: bool = False
    rec = str(recipient[recipient.rfind("."): len(recipient)])
    postfix = [".com", ".ru", ".net"]
    for s in postfix:
        if rec == s:
            chkrec = True
            break
    sen = str(sender[sender.rfind("."): len(sender)])
    for s in postfix:
        if sen == s:
            chksen = True
            break
    return chkrec, chksen
def send_email(message, recipient, sender="university.help@gmail.com"):
    chkrec, chksen = checking(recipient, sender)
    if ("@" not in recipient and "@" not in sender) or (chkrec == False or chksen == False):
        print(f"Невозможно отправить письмо с адреса {sender} на адрес {recipient}")
    elif recipient == sender:
        print("Нельзя отправить письмо самому себе!")
    elif sender=="university.help@gmail.com":
        print(f"Письмо успешно отправлено с адреса {sender} на адрес {recipient}")
    else:
        print(f"НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адресата {sender} на адрес {recipient}")
send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')
send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')
send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')
send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')