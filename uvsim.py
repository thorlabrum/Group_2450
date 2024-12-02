from word import Word
from memory_editor import MemoryEditor
from enum import Enum, auto

class Opcode(Enum):
    READ = 10
    WRITE = 11
    LOAD = 20
    STORE = 21
    ADD = 30
    SUBTRACT = 31
    DIVIDE = 32
    MULTIPLY = 33
    BRANCH = 40
    BRANCHNEG = 41
    BRANCHZERO = 42
    HALT = 43

class UVSim:
    def __init__(self):
        """Creates memory bank and accumulator for UVSim initializing all values to 0. """
        self.curr = 0
        self.memory = []
        for _ in range (250):
            self.memory.append(Word(0))
        self.accumulator = Word(0)
        self.is_halted = False
        self.memory_editor = MemoryEditor(self)

    def read_file(self,filename):
        # iterate through the lines
        with open(filename) as f:
            lines = f.readlines()

            try:
                if len(lines) > 250:
                    raise IndexError("File exceeds memory capacity of 250 lines.")
                
                for i, line in enumerate(lines):
                    self.memory[i].set_value(int(convert(line)))
            except IndexError:
                return "File exceeds memory capacity of 250 lines."


    def read_input(self, input_vals):
        try:
            if len(input_vals) > 250:
                raise IndexError("File exceeds memory capacity")
            for i in range(len(input_vals)):
                self.memory[i].set_value(int(input_vals[i]))
        except IndexError:
            return "IndexError: File exceeds memory capacity of 250 lines."

    def __iter__(self):
        """ A function to make UVSim iterable """
        return self
    
    def __next__(self):
        """ A function to determine what the next object is when iterating """
        if self.is_halted == True:
            raise StopIteration
        info = self.operate()
        if self.is_halted == True:
            raise StopIteration
        return info

    def operate(self):
        """separates op_code and operand, reads in the command, and then increments self.current"""
        curr_word = self.memory[self.curr]
        #find operand(last 4 digits)
        operand = curr_word.get_value() % 10**4
        if operand > 250:
            raise ValueError("Operand operating on a value greater than 250")
        #find op code(first 2 digits)
        op_code = int(curr_word.get_value() // 10**4)
        # print(f"Opcode: {op_code}   Operand: {operand}")

        op = Opcode(op_code)

        match op:
            case Opcode.READ:
                self.read(operand)
                info = f"reading {operand} from {curr_word}"
                # instead of appending to info, I just make info = the new string 
                # because it is returned every time operate is called
                self.curr += 1
            case Opcode.WRITE:
                self.write(operand)
                info = f"writing {operand} to {curr_word}"
                self.curr += 1
            case Opcode.LOAD:
                self.load(operand)
                info = f"loading {operand} from {curr_word}"
                self.curr += 1
            case Opcode.STORE:
                self.store(operand)
                info = f"storing {operand} from {curr_word}"
                self.curr += 1
            case Opcode.ADD:
                self.add(operand)
                info = f"adding {operand} from {curr_word}"
                self.curr += 1
            case Opcode.SUBTRACT:
                self.subtract(operand)
                info = f"subtracting {operand} from {curr_word}"
                self.curr += 1
            case Opcode.DIVIDE:
                self.divide(operand)
                info = f"dividing {operand} from {curr_word} \n"
                self.curr += 1
            case Opcode.MULTIPLY:
                self.multiply(operand)
                info = f"multiplying {operand} from {curr_word}"
                self.curr += 1
            case Opcode.BRANCH:
                self.branch(operand)
                info = f"branching to {operand} from {curr_word} \n"
                #curr not incremented as branch changes it
            case Opcode.BRANCHNEG:
                self.branchneg(operand)
                info = f"attempting to branch to {operand} from {curr_word}"
                #curr not incremented as branch changes it
            case Opcode.BRANCHZERO:
                self.branchzero(operand)
                info = f"attempting to branch to {operand} from {curr_word} \n"
                #curr not incremented as branch changes it
            case Opcode.HALT:
                self.halt()
                info = f"halting"
            case _:
                info = f"ValueError: {op_code} of {op_code}{operand} is an invalid input."
        return info
            


    def read(self, operand):
        """Reads a word from the keyboard into a specific location in memory."""
        print('READ FUNCTION')
        value = input("Enter a value: ")
        self.memory[operand].set_value(int(value))
        self.curr +=1
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
        self.memory[operand].set_value(self.accumulator.get_value())
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
            self.curr += 1 # branches need to move forward if they dont branch

    def branchzero(self, operand):
        """Branch to a specific location if the accumulator is zero."""
        if self.accumulator == 0:
            self.curr = operand
            print(f"branchzero to memory location {operand}")
        else:
            print("No branch, accumulator is not zero")
            self.curr += 1

    def halt(self):
        """Halts operate function as dictated by the loaded text file."""
        self.is_halted = True
        print("halt function called")

def convert(s):
    """converts string that is 4 digits into 6 digits"""
    if len(s) < 7: # includes sign
        s = s[:3] + ("0" * 2) + s[3:] # needs to be 2 because op codes are two digits
    return s

