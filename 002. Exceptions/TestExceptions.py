def divide(a):
    try:
        x = 10/a
    except Exception as e:
        print(str(e))
    else:
        print(str(x))


n = input("Enter a number: ")
divide(int(n))
