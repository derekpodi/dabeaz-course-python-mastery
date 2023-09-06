# mutint.py
from functools import total_ordering        

@total_ordering
class MutInt:
    __slots__ = ['value']

    def __init__(self, value):
        self.value = value

    #String
    def __str__(self):
        return str(self.value)
    
    #Representation
    def __repr__(self):
        return f'MutInt({self.value!r})'

    #Format
    def __format__(self, fmt):
        return format(self.value, fmt)
    
    #Add (a + #)
    def __add__(self, other):
        if isinstance(other, MutInt):
            return MutInt(self.value + other.value)
        elif isinstance(other, int):
            return MutInt(self.value + other)
        else:
            return NotImplemented
    #Reverse Add (# + a)
    __radd__ = __add__    # Reversed operands

    #Inplace Add (+=)
    def __iadd__(self, other):
        if isinstance(other, MutInt):
            self.value += other.value
            return self
        elif isinstance(other, int):
            self.value += other
            return self
        else:
            return NotImplemented
        
    #Comparisons (__eq__, __lt__, __le__, __gt__, __ge__)
    #@total_ordering fills in the missing comparison methods for you as long as you minimally provide an equality operator and one of the other relations
    #Equal to ==
    def __eq__(self, other):
        if isinstance(other, MutInt):
            return self.value == other.value
        elif isinstance(other, int):
            return self.value == other
        else:
            return NotImplemented
    
    #LessThan <
    def __lt__(self, other):
        if isinstance(other, MutInt):
            return self.value < other.value
        elif isinstance(other, int):
            return self.value < other
        else:
            return NotImplemented
        
    #Conversions - int(a), float(a)
    def __int__(self):
        return self.value

    def __float__(self):
        return float(self.value)
    
    __index__ = __int__     # Make indexing work
