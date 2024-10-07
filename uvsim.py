from word import Word

class UVSim:
    def __init__(self):
        """Creates memory bank and accumulator for UVSim initializing all values to 0. """
        self.curr = 0
        self.memory = []
        for _ in range (100):
            self.memory.append(Word(0))
        self.accumulator = Word(0)
        self.is_halted = False

    def read_file(self,filename):
        # iterate through the lines
        with open(filename) as f:
            lines = f.readlines()

            if len(lines) > 100:
                raise IndexError("File exceeds memory capacity of 100 lines.")
            
            for i, line in enumerate(lines):
                self.memory[i].set_value(int(line))

    def read_input(self, input_vals):
        if len(input_vals) > 100:
            raise IndexError("File exceeds memory capacity")
        for i in range(len(input_vals)):
            self.memory[i].set_value(int(input_vals[i]))

    def operate(self, info= ""):
        """Resets current pointer and _is_halted. While loop iterates through each line
        separating op_code and operand, reads in the command, and then increments self.current"""
        curr_word = self.memory[self.curr]
        #find operand(last 2 digits)
        operand = curr_word.get_value() % 100
        #find op code(first 2 digits)
        op_code = int(curr_word.get_value() // 100)
        # print(f"Opcode: {op_code}   Operand: {operand}")

        match op_code:
            case 10:
                self.read(operand)
                info = f"reading {operand} from {curr_word}"
                # instead of appending to info, I just make info = the new string 
                # because it is returned every time operate is called
                self.curr += 1
            case 11:
                self.write(operand)
                info = f"writing {operand} to {curr_word}"
                self.curr += 1
            case 20:
                self.load(operand)
                info = f"loading {operand} from {curr_word}"
                self.curr += 1
            case 21:
                self.store(operand)
                info = f"storing {operand} from {curr_word}"
                self.curr += 1
            case 30:
                self.add(operand)
                info = f"adding {operand} from {curr_word}"
                self.curr += 1
            case 31:
                self.subtract(operand)
                info = f"subtracting {operand} from {curr_word}"
                self.curr += 1
            case 32:
                self.divide(operand)
                info = f"dividing {operand} from {curr_word} \n"
                self.curr += 1
            case 33:
                self.multiply(operand)
                info = f"multiplying {operand} from {curr_word}"
                self.curr += 1
            case 40:
                self.branch(operand)
                info = f"branching to {operand} from {curr_word} \n"
                #curr not incremented as branch changes it
            case 41:
                self.branchneg(operand)
                info = f"attempting to branch to {operand} from {curr_word}"
                #curr not incremented as branch changes it
            case 42:
                self.branchzero(operand)
                info = f"attempting to branch to {operand} from {curr_word} \n"
                #curr not incremented as branch changes it
            case 43:
                self.halt()
                info = f"halting"
                self.curr += 1
            case _:
                raise ValueError("Invalid op code")
            
        return self.memory, info
            


    def read(self, operand):
        """Reads a word from the keyboard into a specific location in memory."""
        value = input("Enter a value: ")
        self.memory[operand].set_value(int(value))
        # print("read function called")

    def write(self, operand):
        """Writes a word from a specific location in memory to screen."""
        print(self.memory[operand])
        # print("write function called")

    def load(self, operand):
        """Loads a word from a specific location in memory into the accumulator."""
        self.accumulator.set_value(self.memory[operand].get_value()) 
        # print("load function called")

    def store(self, operand):
        """Store a word from the accumulator into a specific location in memory."""
        self.memory[operand].set_value(self.accumulator)
        # print("store function called")

    def add(self, operand):
        """Adds a word from a specific location in memory to the word
        in the accumulator (leave the result in the accumulator)"""
        self.accumulator += self.memory[operand]
        # print("add function called")

    def subtract(self, operand):
        """Subtracts a word from a specific location in memory from the word
        in the accumulator (leave the result in the accumulator)"""
        self.accumulator -= self.memory[operand]
        # print("subtract function called")

    def divide(self, operand):
        """Divide the word in the accumulator by a word from a specific
        location in memory (leave the result in the accumulator)."""
        self.accumulator //= self.memory[operand] # floor div because we are using ints
        # print("divide function called")

    def multiply(self, operand):
        """Multiplies a word from a specific location in memory and the word
        in the accumulator (leave the result in the accumulator)."""
        self.accumulator *= self.memory[operand]
        # print("multiply function called")

    def branch(self, operand):
        """Branch unconditionally to a specific location in memory (operand)."""
        self.curr = operand
        print(f"branch to memory location {operand}")

    def branchneg(self, operand):
        """Branch to a specific location if the accumulator is negative."""
        if self.accumulator < 0:
            self.curr = operand
            print(f"branchneg to memory location {operand}")
        else:
            print("No branch, accumulator is not negative")

    def branchzero(self, operand):
        """Branch to a specific location if the accumulator is zero."""
        if self.accumulator == 0:
            self.curr = operand
            print(f"branchzero to memory location {operand}")
        else:
            print("No branch, accumulator is not zero")


    def halt(self):
        """Halts operate function as dictated by the loaded text file."""
        self.is_halted = True
        print("halt function called")
