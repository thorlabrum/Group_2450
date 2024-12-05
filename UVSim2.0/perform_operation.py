from word2 import Word
from memory_editor2 import MemoryEditor
from enum import Enum, auto
from commands2 import Read, Write, Load, Store, Add, Subtract, Divide, Multiply, Branch, BranchNeg, BranchZero, Halt, SendError

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

class PerformOperation:
    def __init__(self):
        self.operation = None
    
    def set_command(self, word):
        send_command = None
        match word:
            case "READ":
                send_command = Read(word)
            case "WRITE":
                send_command = Write(word)
            case "LOAD":
                send_command = Load(word)
            case "STORE":
                send_command = Store(word)
            case "ADD":
                send_command = Add(word)
            case "SUBTRACT":
                send_command = Subtract(word)
            case "DIVIDE":
                send_command = Divide(word)
            case "MULTIPLY":
                send_command = Multiply(word)
            case "BRANCH": 
                send_command = Branch(word)
            case "BRANCHNEG":
                send_command = BranchNeg(word)
            case "BRANCHZERO":
                send_command = BranchZero(word)
            case "HALT":
                send_command = Halt()
            case _:
                send_command = SendError(word)

        self.operation = send_command

    def execute(self, word):

        operand = word.get_value() % 10**4

        if operand > 250:
            raise ValueError("Operand operating on a value greater than 250")

        return self.operation.execute(operand)