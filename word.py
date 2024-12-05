WORD_LENGTH = 6 # number of digits in word

class Word:
    def __init__(self, val = "000000"):
        self.value = in_range(int(val))

    def __str__(self):
        if self.value > -1:
            return f"+{self.value:06}"
        return f"{self.value:07}" # minus sign counts

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

    def set_value(self,v):
        self.value = in_range(v)

    def get_value(self):
        return self.value
    
    
def in_range(x):
    """makes sure x is within the bounds -1000000 < x < 1000000. It loops it around if it falls outside that range"""
    x = int(x) # insures x is an integer
    maxnum = 10**WORD_LENGTH
    while not (-1*maxnum < x < maxnum):
        if x < -1 * maxnum:
            x += 2*maxnum - 1
        elif x > maxnum:
            x -= 2 * maxnum - 1
    return x
    

