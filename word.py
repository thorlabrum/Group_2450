class Word:
    def __init__(self):
        self.value = 0

    def set_value(self,x):
        if -9999 < x < 9999:
            self.value = x

    def get_value(self):
        return self.value

