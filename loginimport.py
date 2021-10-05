def login(username, password):
    if check_string(username) and check_string(password):
        if check_pass(password):
            return True
        else:
            return False
    return False


def check_string(x):
    if type(x) == str:
        return True
    else:
        return False


def check_pass(y):
    special = ['@', '#', '$', '%']
    out = True

    if len(y) < 8:
        out = False

    if any(char.isdigit() for char in y):
        out = True

    if any(char.isupper() for char in y):
        out = True

    if any(char.isupper() for char in y):
        out = True

    if any(char in special for char in y):
        out = True

    return out