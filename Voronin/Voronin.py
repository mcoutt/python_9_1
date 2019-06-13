def f(name=None, *args, **kwargs):
    print(f'Hello (name)')

def dec(some_func):
    def wrapper(name=None, *args, **kwargs):
        print('before call')
        print(*args)
        print(**kwargs)
        some_func(name)
        print('after call')
    return wrapper

decor_func = dec(f)
print()

some_name = 'Dima'

@dec
def another_func(some_name, name=None):
    print(f'from another func (some name)')


another_func(some_name)
