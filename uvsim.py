from word import Word

class Memory:
    def __init__(self):
        self.curr = 0
        self.memory = []
        for i in range (100):
            self.memory.append(Word())

    def read_file(self,filename):
        # iterate through the lines
        with open(filename) as f:

            lines = f.readlines()

            if len(lines) > 100:
                raise IndexError("File exceeds memory capacity of 100 lines.")
            
            for i, line in enumerate(lines):
                self.memory[i].set_value(int(line))
        # if it is an int [-9999, 9999] then store it as a word
        # in order for the words lsit

        # return 0

    def operate(self):
        # start at first word and then increment by 1
        self.curr = 0
        curr_word = self.memory[self.curr]
        #find operand(last 2 digits)
        operand = curr_word.get_value() % 100
        #find op code(first 2 digits)
        op_code = int(curr_word.get_value() // 100)

        match op_code:
            case 10:
                self.read(operand)
                self.curr += 1
            case 11:
                self.write(operand)
                self.curr += 1
            case 20:
                self.load(operand)
                self.curr += 1
            case 21:
                self.store(operand)
                self.curr += 1
            case 30:
                self.add(operand)
                self.curr += 1
            case 31:
                self.subtract(operand)
                self.curr += 1
            case 32:
                self.divide(operand)
                self.curr += 1
            case 33:
                self.multiply(operand)
                self.curr += 1
            case 40:
                self.branch(operand)
                self.curr += 1
            case 41:
                self.branchneg(operand)
                self.curr += 1
            case 42:
                self.branchzero(operand)
                self.curr += 1
            case 43:
                self.halt(operand)
                self.curr += 1
            case _:
                raise ValueError("Invalid op code")
        


    def is_halted(self):
        return self.curr == -1
    
    def read(self, operand):
        print("read function called")

    def write(self, operand):
        print("write function called")

    def load(self, operand):
        print("load function called")

    def store(self, operand):
        print("store function called")

    def add(self, operand):
        print("add function called")

    def subtract(self, operand):
        print("subtract function called")

    def divide(self, operand):
        print("divide function called")

    def multiply(self, operand):
        print("multiply function called")

    def branch(self, operand):
        print("branch function called")

    def branchneg(self, operand):
        print("branchneg function called")

    def branchzero(self, operand):
        print("branchzero function called")

    def halt(self, operand):
        print("halt function called")
    
    