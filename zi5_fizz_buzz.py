for i in range(1,101):
    if i%3 == 0 and i%5 == 0:
        print(f"  ",{i},"fizzBuzz")
    elif i%3 == 0:
        print(f"  ",{i},"Fizz")
    elif i%5 == 0:
        print(f"  ",{i},"buzz")
    else:
        print(i)