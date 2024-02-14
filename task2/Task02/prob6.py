while True:
    try:
        number = int(input("enter a number: "))
        result = number % 2
        if result == 0:
            print("this number is an even")
        else:
            break
    except Exception:
        print("enter a number even")
