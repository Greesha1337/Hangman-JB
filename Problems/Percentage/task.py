def get_percentage(number, round_digits=None):
    if round_digits is None:
        result = int(number * 100)
    else:
        result = (number * 100).__round__(round_digits)
    return f'{result}%'


