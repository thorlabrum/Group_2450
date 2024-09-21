from word import Word

class Memory:
    def __init__(self):
        """Creates memory bank and accumulator for UVSim initializing all values to 0. """
        self.curr = 0
        self.memory = []
        for _ in range (100):
            self.memory.append(Word())
        self.accumulator = 0
        self.is_halted = True

    def read_file(self,filename):
        # iterate through the lines
        with open(filename) as f:
            lines = f.readlines()

            if len(lines) > 100:
                raise IndexError("File exceeds memory capacity of 100 lines.")
            
            for i, line in enumerate(lines):
                self.memory[i].set_value(int(line))


    def operate(self):
        """Resets current pointer and _is_halted. While loop iterates through each line
        separating op_code and operand, reads in the command, and then increments self.current"""
        self.curr = 0
        self.is_halted = False

        while self.is_halted == False:

            curr_word = self.memory[self.curr]
            #find operand(last 2 digits)
            operand = curr_word.get_value() % 100
            #find op code(first 2 digits)
            op_code = int(curr_word.get_value() // 100)
            # print(f"Opcode: {op_code}   Operand: {operand}")

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
                    self.halt()
                    self.curr += 1
                case _:
                    raise ValueError("Invalid op code")
            


    def read(self, operand):
        """Reads a word from the keyboard into a specific location in memory."""
        value = input()
        self.memory[operand].set_value(int(value))
        # print("read function called")

    def write(self, operand):
        """Writes a word from a specific location in memory to screen."""
        print(self.memory[operand].get_value())
        # print("write function called")

    def load(self, operand):
        """Loads a word from a specific location in memory into the accumulator."""
        self.accumulator = self.memory[operand].get_value()
        # print("load function called")

    def store(self, operand):
        """Store a word from the accumulator into a specific location in memory."""
        self.memory[operand].set_value(self.accumulator)
        # print("store function called")

    def add(self, operand):
        """Adds a word from a specific location in memory to the word
        in the accumulator (leave the result in the accumulator)"""
        self.accumulator += self.memory[operand].get_value()
        # print("add function called")

    def subtract(self, operand):
        """Subtracts a word from a specific location in memory from the word
        in the accumulator (leave the result in the accumulator)"""
        self.accumulator -= self.memory[operand].get_value()
        # print("subtract function called")

    def divide(self, operand):
        """Divide the word in the accumulator by a word from a specific
        location in memory (leave the result in the accumulator)."""
        self.accumulator /= self.memory[operand].get_value()
        # print("divide function called")

    def multiply(self, operand):
        """Multiplies a word from a specific location in memory and the word
        in the accumulator (leave the result in the accumulator)."""
        self.accumulator *= self.memory[operand].get_value()
        # print("multiply function called")

    def branch(self, operand):
        print("branch function called")

    def branchneg(self, operand):
        print("branchneg function called")

    def branchzero(self, operand):
        print("branchzero function called")

    def halt(self):
        """Halts operate function as dictated by the loaded text file."""
        self.is_halted = True
        print("halt function called")
