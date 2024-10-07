class Word:
    def __init__(self, val = 0):
        self.value = val

    def __str__(self):
        if self.value > -1:
            return f"+{self.value:04}"
        return f"{self.value:04}"

    def __int__(self):
        return self.value

    def __add__(self,r):
        return Word(self.value + int(r))
    
    def __subtract__(self,r):
        return Word(self.value - int(r))
    
    def __mult__(self, r):
        return Word(self.value * int(r))
    
    def __floordiv__(self,r):
        return Word(self.value // int(r))
    
    def __iadd__(self,r):
        return self + r
    
    def __isubtract__(self,r):
        return self - r
    
    def __imult__(self,r):
        return self * r
    
    def __ifloordiv__(self,r):
        return self // r

    def set_value(self,x):
        x = int(x)
        if -9999 < x < 9999:
            self.value = x

    def get_value(self):
        return self.value
    

