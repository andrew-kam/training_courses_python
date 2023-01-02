class BadName(Exception):
    pass


def greet(name):
    if name[0].isupper():
        return 'Hello ' + name
    else:
        raise BadName(name + ' is inappropriate name')


if __name__ == '__main__':
    print('import')
    print(__name__)
print('import mod')

__all__ = ['BadName', 'greet']
