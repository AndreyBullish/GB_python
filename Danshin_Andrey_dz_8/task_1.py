import re


def email_parse(email: str) -> dict:
    RE_MAIL_1 = re.compile(r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+')
    match_mail = RE_MAIL_1.match(email)
    if not match_mail:
        raise ValueError(f'Wrong mail: {email}')
    if match_mail != None:
        RE_MAIL_2 = re.compile('@')
        list_username_email = RE_MAIL_2.split(email)
        dict_username_email = {list_username_email[i]: list_username_email[i + 1] for i in
                               range(0, len(list_username_email), 2)}
    return dict_username_email

if __name__ == '__main__':
    print(email_parse('someone@geekbrains.ru'))
    # email_parse('someone@geekbrainsru')

print('\n''end')



