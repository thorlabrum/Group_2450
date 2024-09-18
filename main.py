from word import Word
from memory import Memory

accumulator = Word()

word_bank = Word_bank()
word_bank.read_file("filename")

while word_bank.is_halted() == False:
    word_bank.operate()

