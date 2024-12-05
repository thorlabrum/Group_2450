from word2 import Word
from memory_editor2 import MemoryEditor
from enum import Enum, auto


class Read:
    def __init__(self, memory):
        self.memory = memory
    def execute(self, operand):
        """Reads a word from the keyboard into a specific location in memory."""
        print('READ FUNCTION')
        value = input("Enter a value: ")
        self.memory.memory[operand].set_value(int(value))
        self.memory.curr += 1
        # print("read function called")


class Write:
    def __init__(self,memory):
        self.memory = memory

    def execute(self, operand):
        """Writes a word from a specific location in memory to screen."""
        print(self.memory.memory[operand])
        self.memory.curr += 1
        # print("write function called")


class Load:
    def __init__(self,memory):
        self.memory = memory
    def execute(self, operand):
        """Loads a word from a specific location in memory into the accumulator."""
        self.memory.accumulator.set_value(self.memory.memory[operand].get_value()) 
        self.memory.curr += 1
        # print("load function called")


class Store:
    def __init__(self,memory):
        self.memory = memory
    def execute(self, operand):
        """Store a word from the accumulator into a specific location in memory."""
        self.memory.memory[operand].set_value(self.memory.accumulator.get_value())
        self.memory.curr += 1
        # print("store function called")

class Add:
    def __init__(self,memory):
        self.memory = memory

    def execute(self, operand):
        """Adds a word from a specific location in memory to the word
        in the accumulator (leave the result in the accumulator)"""
        self.memory.accumulator += self.memory.memory[operand]
        self.memory.curr += 1
        # print("add function called")


class Subtract:
    def __init__(self,memory):
        self.memory = memory

    def execute(self, operand):
        """Subtracts a word from a specific location in memory from the word
        in the accumulator (leave the result in the accumulator)"""
        self.memory.accumulator -= self.memory.memory[operand]
        self.memory.curr += 1
        # print("subtract function called")


class Divide:
    def __init__(self,memory):
        self.memory = memory
    def execute(self, operand):
        """Divide the word in the accumulator by a word from a specific
        location in memory (leave the result in the accumulator)."""
        self.memory.accumulator //= self.memory.memory[operand] # floor div because we are using ints
        self.memory.curr += 1
        # print("divide function called")


class Multiply:
    def __init__(self,memory):
        self.memory = memory
    def execute(self, operand):
        """Multiplies a word from a specific location in memory and the word
        in the accumulator (leave the result in the accumulator)."""
        self.memory.accumulator *= self.memory.memory[operand]
        self.memory.curr += 1
        # print("multiply function called")


class Branch:
    def __init__(self,memory):
        self.memory = memory
    def execute(self, operand):
        """Branch unconditionally to a specific location in memory (operand)."""
        self.memory.curr = operand
        print(f"branch to memory location {operand}")

class BranchNeg:
    def __init__(self,memory):
        self.memory = memory
    def execute(self, operand):
        """Branch to a specific location if the accumulator is negative."""
        if self.memory.accumulator < 0:
            self.memory.curr = operand
            print(f"branchneg to memory location {operand}")
        else:
            print("No branch, accumulator is not negative")
            self.memory.curr += 1 # branches need to move forward if they dont branch

class BranchZero:
    def __init__(self,memory):
        self.memory = memory
    def execute(self, operand):
        """Branch to a specific location if the accumulator is zero."""
        if self.memory.accumulator == 0:
            self.memory.curr = operand
            print(f"branchzero to memory location {operand}")
        else:
            print("No branch, accumulator is not zero")
            self.curr += 1

class Halt:
    def __init__(self,memory):
        self.memory = memory
    def halt(self, *args):
        """Halts operate function as dictated by the loaded text file."""
        self.memory.is_halted = True
        print("halt function called")

class SendError:
    def __init__(self,memory):
        self.memory = memory
    def execute(self, *args):
        return f"Invalid word."

def convert(s):
    """converts string that is 4 digits into 6 digits"""
    if len(s) < 7: # includes sign
        s = s[:3] + ("0" * 2) + s[3:] # needs to be 2 because op codes are two digits
    return s