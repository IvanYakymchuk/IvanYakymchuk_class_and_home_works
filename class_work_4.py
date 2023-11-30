# Реалізація декоратора для забезпечення додатнього результату
def make_positive(f):
    def _make_positive(*args, **kwargs):
        res = f(*args, **kwargs)
        res = 0 if res < 0 else res
        return res
    return _make_positive

# Реалізація декоратора для обмеження результату в заданому діапазоні
def make_slice(a, b):
    def _make_slice(f):
        def __make_slice(*args, **kwargs):
            res = f(*args, **kwargs)
            if res < a:
                res = a
            elif res > b:
                res = b
            return res
        return __make_slice
    return _make_slice


def check_pos_keys(f):
    def _check_pos_keys(*args, **kwargs):
        if len(args) != len(kwargs):
            raise KeyNotequalPositional(len(args), len(kwargs))
        res = f(*args, **kwargs)
        return res
    return _check_pos_keys

def check_type(a):
    def _check_type(f):
        def __check_type(*args, **kwargs):
            for i in args:
                if type(i) != type(a):
                    raise Type(a)
            for i in kwargs.values():
                if type(i) != type(a):
                    raise Type(a)
            res = f(*args, **kwargs)
            return res
        return __check_type
    return _check_type









@make_positive
def function(x):
    return x - 2

@make_slice(0, 2)
def function2(x):
    return x - 2

@make_slice(1, 3)
def function3(x, y, z=3):
    return x + y - z

@check_type(5)
def function4(*args, **kwargs):
    a = sum(args)
    b = sum(kwargs.values())
    return (a+b)/(len(args) + len(kwargs.values()))



class KeyNotequalPositional(Exception):

    def __init__(self, l1, l2):
        self.lenPos = l1
        self.lenKey = l2

    def __str__(self):
        return f"Lengths of positional{self.lenPos} is no equal "\
        f" to the lenhth of key {self.lenKey}"

class Type(Exception):

    def __init__(self, tp):
        self.tp = tp


    def __str__(self):
        return f"arguments types is not the same as {self.tp}"

@check_pos_keys
def req_function(*args, **kwargs):
    p = 1.
    for x,y in zip(args,kwargs.values()):
        p *= (x +1./y)
    return p


if __name__ == "__main__":
    """print(function2(0))
    print(function3(5,2))
    print(function3(1,2))"""

    try:
        print(function4(1,2,y1 = 1.4))
    except Type as e:
        print(e)




