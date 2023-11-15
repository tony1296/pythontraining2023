def exceptionHandling():
    try:
        car = {"make": "bmw","model":"220e","year":"2017"}
        print(car["make"]+car["model"]+car["year"])
        print(car["model"])
        print(car["color"])
    except:
        print("Key not found")
    finally:
        print("Please try a different key")

exceptionHandling()