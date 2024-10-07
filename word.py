class Word:
    def __init__(self):
        self.value = 0

    def __str__(self):
        return f"{self.value}"

    def set_value(self,x):
        if -9999 < x < 9999:
            self.value = x

    def get_value(self):
        return self.value
    

