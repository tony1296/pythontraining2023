def exceptionHandling():
    try:
        a=20
        b=50
        c=1
        d=(a+b)/c
        print(d)
    except:
        print("Arithmatic exception")
    else:
        print("Because there was no exception, else is executed")
    finally:
        print("Finally, always executed")

exceptionHandling()