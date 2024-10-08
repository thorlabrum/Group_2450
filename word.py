class Word:
    def __init__(self, val = 0):
        self.value = in_range(val)

    def __str__(self):
        if self.value > -1:
            return f"+{self.value:04}"
        return f"{self.value:04}"
    
    def __repr__(self):
        if self.value > -1:
            return f"+{self.value:04}"
        return f"{self.value:04}"

    def __int__(self):
        return self.value

    def __lt__(self,r):
        return self.value < int(r)
    
    def __gt__(self, r):
        return self.value > int(r)
    
    def __eq__(self,r):
        return self.value == int(r)

    def __add__(self,r):
        return Word(in_range(self.value + int(r)))
    
    def __sub__(self,r):
        return Word(in_range(self.value - int(r)))
    
    def __mult__(self, r):
        return Word(in_range(self.value * int(r)))
    
    def __floordiv__(self,r):
        return Word(in_range(self.value // int(r)))
    
    def __iadd__(self,r):
        return self + r
    
    def __isub__(self,r):
        return self - r
    
    def __imult__(self,r):
        return self * r
    
    def __ifloordiv__(self,r):
        return self // r

    def set_value(self,x):
        self.value = in_range(x)

    def get_value(self):
        return self.value
    
    
def in_range(x):
    """makes sure x is within the bounds -10000 < x < 10000. It loops it around if it falls outside that range"""
    x = int(x) # insures x is an integer
    while not (-10000 < x < 10000):
        if x < -9999:
            x += 19999
        elif x > 9999:
            x -= 19999
    return x
    

