ops = {"+": (lambda x,y: x+y), "-": (lambda x,y: x-y), "*": (lambda x,y: x*y), "/": (lambda x,y: x/y)}

try:
    x, y, oprt = input("Enter a two value with operator: ").split()
    x,y = float(x),float(y)
except ValueError as e:
    print("Invalid Input Please Input number not in string...")

if oprt in ops:
    try:
        val = ops[oprt](float(x),float(y))
        print(val)
    except ValueError as e:
        print(e)

else:
    print("wrong operator")
