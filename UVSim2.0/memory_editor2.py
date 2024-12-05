from word2 import Word
import pyperclip

class MemoryEditor:
    def __init__(self, uvsim):
        self.uvsim = uvsim

    def insert_val(self, position):
        """This is the add command for the gui in Milestone 4"""
        new_word = Word(int(input(f"Word to insert on line {position}: ")))
        self.uvsim.memory.insert(position, new_word)

    def delete(self, position):
        """Delete command for the gui in Milestone 4"""
        self.uvsim.memory.pop(position)

    def copy(self, position):
        """Copy for gui. Milestone 4"""
        pyperclip.copy(str(self.uvsim.memory[position].value))

    def cut(self, position):
        """Cut for gui. Milestone 4"""
        pyperclip.copy(str(self.uvsim.memory[position].value))
        self.delete(position)

    def paste(self, position):
        """Paste for gui. Milestone 4"""
        new_word = Word(int((pyperclip.paste())))
        self.uvsim.memory.insert(position, new_word)