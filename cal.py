ops = {"+": (lambda x,y: x+y), "-": (lambda x,y: x-y), "*": (lambda x,y: x*y), "/": (lambda x,y: x/y)}

try:
    x, y, oprt = input("Enter a two value with operator: ").split()
    x,y = float(x),float(y)
except ValueError as e:
    print("Invalid Input Please Input number not in string...")

if oprt in ops:
    try:
        val = ops[oprt](x,y)
        print(val)
    except ZeroDivisionError as e:
        print(e)

else:
    pass
