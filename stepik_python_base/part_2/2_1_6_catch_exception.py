import random

dir_exception = {
    1: ZeroDivisionError,
    2: ArithmeticError,
    3: AssertionError}


def foo():
    n = random.randint(1, 3)
    raise dir_exception[n]


def get_answer():
    try:
        foo()
    except ZeroDivisionError:
        print('ZeroDivisionError')
    except ArithmeticError:
        print('ArithmeticError')
    except AssertionError:
        print('AssertionError')


def main():
    get_answer()


if __name__ == '__main__':
    main()

# https://stepik.org/lesson/24463/step/6?unit=6771
