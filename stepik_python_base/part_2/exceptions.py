def f(x, y):
    try:
        return x/y
    except (TypeError, ZeroDivisionError) as e:
        print(type(e))
        print(e)
        print(e.args)


def f1(x, y):
    try:
        return x/y
    except:
        print('error')


def divide(x, y):
    try:
        result = x / y
    except ZeroDivisionError:
        print('div by zero')
    else:
        print('result is', result)
    finally:
        print('fin')


# print(f(5, 0))
# print(f(5, []))
# print(f1(5, 0))
# print(f1(5, []))

# divide(2, 1)
# divide(2, 0)
# divide(2, [])


def greet(name):
    if name[0].isupper():
        return 'Hello ' + name
    else:
        raise ValueError(name + ' is inappropriate name')


while True:
    try:
        name = input('Please enter your name: ')
        greeting = greet(name)
        print(greeting)
    except ValueError:
        print('Please try again')
    else:
        break


class BadName(Exception):
    pass


def greet(name):
    if name[0].isupper():
        return 'Hello ' + name
    else:
        raise BadName(name + ' is inappropriate name')


print(greet('Anton'))
print(greet('anton'))
