from word2 import Word
from memory_editor2 import MemoryEditor
from enum import Enum, auto
from commands2 import Read, Write, Load, Store, Add, Subtract, Divide, Multiply, Branch, BranchNeg, BranchZero, Halt, SendError


# class Opcode(Enum):
#     READ = 10
#     WRITE = 11
#     LOAD = 20
#     STORE = 21
#     ADD = 30
#     SUBTRACT = 31
#     DIVIDE = 32
#     MULTIPLY = 33
#     BRANCH = 40
#     BRANCHNEG = 41
#     BRANCHZERO = 42
#     HALT = 43

class DynamicCommand:
    def __init__(self):
        self.operations = {
            10 : "READ",
            11 : "WRITE",
            20 : "LOAD",
            21 : "STORE",
            30 : "ADD",
            31 : "SUBTRACT",
            32 : "DIVIDE",
            33 : "MULTIPLY",
            40 : "BRANCH",
            41 : "BRANCHNEG",
            42 : "BRANCHZERO",
            43 : "HALT"
        }

    def get_operation(self, word):

        op_code = int(word.get_value() // 10**4)
        # print(f"Opcode: {op_code}   Operand: {operand}")

        return self.operations[op_code]
        # op = Opcode(op_code)

        # send_command = None
        # match op:
        #     case Opcode.READ:
        #         send_command = Read(word)
        #     case Opcode.WRITE:
        #         send_command = Write(word)
        #     case Opcode.LOAD:
        #         send_command = Load(word)
        #     case Opcode.STORE:
        #         send_command = Store(word)
        #     case Opcode.ADD:
        #         send_command = Add(word)
        #     case Opcode.SUBTRACT:
        #         send_command = Subtract(word)
        #     case Opcode.DIVIDE:
        #         send_command = Divide(word)
        #     case Opcode.MULTIPLY:
        #         send_command = Multiply(word)
        #     case Opcode.BRANCH: 
        #         send_command = Branch(word)
        #     case Opcode.BRANCHNEG:
        #         send_command = BranchNeg(word)
        #     case Opcode.BRANCHZERO:
        #         send_command = BranchZero(word)
        #     case Opcode.HALT:
        #         send_command = Halt(word)
        #     case _:
        #         send_command = SendError(word)
        # return send_command


new_word = Word(100000)

command = DynamicCommand().get_operation(new_word)
print(command)