from word2 import Word
from memory_editor2 import MemoryEditor
from enum import Enum, auto
from commands2 import NoCommand, ReadCommand, WriteCommand, ReadFileCommand, AddCommand, MultiplyCommand, DivideCommand, SubtractCommand

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

class Memory:
    def __init__(self):
        """Creates memory bank and accumulator for UVSim initializing all values to 0. """
        self.curr = 0
        self.memory = []
        for _ in range (250):
            self.memory.append(Word(0))
        self.accumulator = Word(0)
        self.is_halted = False
        self.memory_editor = MemoryEditor(self)


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


    def advance_memory(self):
        self.curr += 1


    # def operate(self):
    #     """separates op_code and operand, reads in the command, and then increments self.current"""
    #     curr_word = self.memory[self.curr]
    #     #find operand(last 6 digits)
    #     operand = curr_word.get_value() % 10**4
    #     if operand > 250:
    #         raise ValueError("Operand operating on a value greater than 250")
    #     #find op code(first 2 digits)
    #     op_code = int(curr_word.get_value() // 10**4)
    #     # print(f"Opcode: {op_code}   Operand: {operand}")

    #     op = Opcode(op_code)

    #     match op:
    #         case Opcode.READ:
    #             self.read(operand)
    #             info = f"reading {operand} from {curr_word}"
    #             # instead of appending to info, I just make info = the new string 
    #             # because it is returned every time operate is called
    #             self.curr += 1
    #         case Opcode.WRITE:
    #             self.write(operand)
    #             info = f"writing {operand} to {curr_word}"
    #             self.curr += 1
    #         case Opcode.LOAD:
    #             self.load(operand)
    #             info = f"loading {operand} from {curr_word}"
    #             self.curr += 1
    #         case Opcode.STORE:
    #             self.store(operand)
    #             info = f"storing {operand} from {curr_word}"
    #             self.curr += 1
    #         case Opcode.ADD:
    #             self.add(operand)
    #             self.accumulator = AddCommand(self.accumulator).execute()
    #             info = f"adding {operand} from {curr_word}"
    #             self.curr += 1
    #         case Opcode.SUBTRACT:
    #             self.subtract(operand)
    #             info = f"subtracting {operand} from {curr_word}"
    #             self.curr += 1
    #         case Opcode.DIVIDE:
    #             self.divide(operand)
    #             info = f"dividing {operand} from {curr_word} \n"
    #             self.curr += 1
    #         case Opcode.MULTIPLY:
    #             self.multiply(operand)
    #             info = f"multiplying {operand} from {curr_word}"
    #             self.curr += 1
    #         case Opcode.BRANCH:
    #             self.branch(operand)
    #             info = f"branching to {operand} from {curr_word} \n"
    #             #curr not incremented as branch changes it
    #         case Opcode.BRANCHNEG:
    #             self.branchneg(operand)
    #             info = f"attempting to branch to {operand} from {curr_word}"
    #             #curr not incremented as branch changes it
    #         case Opcode.BRANCHZERO:
    #             self.branchzero(operand)
    #             info = f"attempting to branch to {operand} from {curr_word} \n"
    #             #curr not incremented as branch changes it
    #         case Opcode.HALT:
    #             self.halt()
    #             info = f"halting"
    #         case _:
    #             info = f"ValueError: {op_code} of {op_code}{operand} is an invalid input."
    #     return info
            