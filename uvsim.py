from word import Word

class Memory:
    def __init__(self):
        self.curr = 0
        self.memory = []
        for i in range (100):
            self.memory.append(Word())

    def read_file(self,filename):
        # iterate throught the lines
        # if it is an int [-9999, 9999] then store it as a word
        # in order for the words lsit

        return 0

    def operate(self):
        self.curr = -1

    def is_halted(self):
        return self.curr == -1
