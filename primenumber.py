for no in range(2, 1001):
    if no > 1:
        for i in range(2, no):
            if (no % i) == 0:
                break
        else:
            print(no)