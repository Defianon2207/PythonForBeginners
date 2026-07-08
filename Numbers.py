import numbers
import fractions
from collections.abc import MutableMapping


def printSetting(**setting):
    print(setting)





class CaseInsensitiveDict(MutableMapping):
    def __init__(self, *args, **kwargs):
        self._data = dict()
        self._lata = dict()
        print("CaseInsensitiveDict initialized with data:", self._lata)
        # Use the standard dict update mechanism to handle initial data
        self._data.update(dict(*args, **kwargs))
        self._lata.update(dict(*args, **kwargs))
        print("CaseInsensitiveDict initialized with data:", self, self._lata)
        print("CaseInsensitiveDict hash data:", self.__hash__())
    
    # 1. Customizing lookup (d[key])
    def __getitem__(self, key):
        return self._data[self._lowercase_key(key)]

    # 2. Customizing assignment (d[key] = value)
    def __setitem__(self, key, value):
        self._data[self._lowercase_key(key)] = value

    # 3. Customizing deletion (del d[key])
    def __delitem__(self, key):
        del self._data[self._lowercase_key(key)]

    # 4. Customizing iteration (e.g., for key in d)
    def __iter__(self):
        return iter(self._data)

    # 5. Customizing length (len(d))
    def __len__(self):
        return len(self._data)

    # Helper method to enforce lowercase keys
    def _lowercase_key(self, key):
        if isinstance(key, str):
            return key.lower()
        return key

    # def __str__(self):
    #     return str(self._lata)  

    # Customizing how it prints in the console
    def __repr__(self):
        return "Nahi karega print jaa jo karna hai kar le"

    def __hash__(self):
        return hash(frozenset(self._lata.items()))
from numbers import Integral, Real, Complex

def do_my_adding_stuff(a, b):
        print("Adding two MyIntegral objects")
        return MyIntegral(a.value + b.value)


def do_my_other_adding_stuff(a, b):
        print("Adding MyIntegral and SpecialNumber")

        if isinstance(a, SpecialNumber):
            return a.value + b.value
        else:
            return a.value + b.value
class SpecialNumber:
    def __init__(self, value):
        self.value = value

    def __repr__(self):
        return f"SpecialNumber({self.value})"

class MyIntegral:
    def __init__(self, value):
        self.value = int(value)
        print("Self value is here", self)
    def __repr__(self):
        return f"MyIntegral({self.value})"

    def __int__(self):
        return self.value

    def __float__(self):
        return float(self.value)

    def __complex__(self):
        return complex(self.value)


    def __add__(self, other):
        print("Adding two numbers:", self, other, isinstance(other, SpecialNumber))

        if isinstance(other, MyIntegral):
            return do_my_adding_stuff(self, other)

        elif isinstance(other, SpecialNumber):
            print("Adding MyIntegral and SpecialNumber")
            return do_my_other_adding_stuff(self, other)

        else:
            return NotImplemented
    def __radd__(self, other):

        if isinstance(other, MyIntegral):
            return do_my_adding_stuff(other, self)

        elif isinstance(other, SpecialNumber):
            return do_my_other_adding_stuff(other, self)

        elif isinstance(other, Integral):
            return int(other) + int(self)

        elif isinstance(other, Real):
            return float(other) + float(self)

        elif isinstance(other, Complex):
            return complex(other) + complex(self)

        return NotImplemented




class Main():
    __name__ = "__main__"
    print(__name__)

    printSetting(volume="high", brightness="medium", contrast="low")
    p = MyIntegral(5)
    d = SpecialNumber(10)
    print(p.__float__(),p.__complex__(), p.__add__(10), p.__add__(d))

Main()