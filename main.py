from word import Word
from uvsim import Memory

"""accumulator = Word()

word_bank = Memory()
word_bank.read_file("filename")

while word_bank.is_halted() == False:
    word_bank.operate()"""

if __name__ == "__main__":
    word = Word()
    mem = Memory()
    Memory.read_file(mem, "Test1.txt")
    mem.operate()
