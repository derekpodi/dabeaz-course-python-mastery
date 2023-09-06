# typedproperty.py

def typedproperty(name, expected_type):
    private_name = '_' + name

    @property
    def value(self):
        return getattr(self, private_name)

    @value.setter
    def value(self, val):
        if not isinstance(val, expected_type):
            raise TypeError(f'Expected {expected_type}')
        setattr(self, private_name, val)
   
    return value


def String(name: str):
    return typedproperty(name, str)

def Integer(name):
    return typedproperty(name, int)
 
def Float(name):
    return typedproperty(name, float)

'''
from typedproperty import typedproperty

class Stock:
    name = typedproperty('name', str)
    shares = typedproperty('shares', int)
    price = typedproperty('price', float)

    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price

'''
String = lambda name: typedproperty(name, str)
Integer = lambda name: typedproperty(name, int)
Float = lambda name: typedproperty(name, float)

# Example
if __name__ == '__main__':
    class Stock:
        name = String('name')
        shares = Integer('shares')
        price = Float('price')
        def __init__(self, name, shares, price):
            self.name = name
            self.shares = shares
            self.price = price