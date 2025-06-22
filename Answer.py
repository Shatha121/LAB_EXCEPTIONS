def additoin(x, y):
    try:
        x = 10
        y = 20
        print("Addition:", x + b)
    except NameError as e:
        print(f"Something went wrong: {e}")
    else:
        print("the operation is successful")


additoin(10, 20)