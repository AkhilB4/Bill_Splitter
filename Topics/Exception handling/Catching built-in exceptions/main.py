def exception_check(a, b):
    try:
        c = a / b
    except ZeroDivisionError:
        print("The Error!")
    else:
        print(c)
