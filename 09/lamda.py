#two ways to wrap a function

def wrap(func):
    def addToLog(*args):
        print('exec wrap, args:', args)
        return func(*args)

    return addToLog


def add(num1, num2):
    return num1 + num2


@wrap
def multiple(num1, num2):
    return num1 * num2


addWrapper = wrap(add)
sum = addWrapper(1, 2)
print(sum)

product = multiple(10, 20)
print(product)
