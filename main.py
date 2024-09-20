from word import Word
from uvsim import Memory

accumulator = Word()

memory = Memory()

memory.read_file("Test1.txt")

print(len(memory.memory))
for line in memory.memory:
    print(line.get_value())
# word_bank = Word_bank()
# word_bank.read_file("filename")

# while word_bank.is_halted() == False:
#     word_bank.operate()

