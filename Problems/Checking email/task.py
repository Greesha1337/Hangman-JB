def check_email(string):
    if ' ' not in string:
        if '@' in string:
            if '.' in string and '@.' not in string:
                return True
    return False