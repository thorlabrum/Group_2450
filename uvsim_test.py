import unittest
import unittest.mock
from word import Word
from uvsim import UVSim
from uvsim import convert
from memory_editor import MemoryEditor

class test_word(unittest.TestCase):
    def setUp(self):
        self.word = Word()

    def test_eq(self):
        assert(self.word == 0)
    
    def test_assignment(self):
        self.word.set_value(100)
        assert(self.word == 100)
    
    def test_add(self):
        assert(self.word + 10 == 10)

    def test_subtract(self):
        assert(self.word - 10 == -10)

    def test_iadd(self):
        self.word += 10
        assert(self.word == 10)

    def test_isub(self):
        self.word -= 10
        assert(self.word == -10)

    def test_max(self): # wraps around
        self.word.set_value(10**6)
        assert(self.word == (1 + -10**6))

    def test_min(self):
        self.word.set_value(-10**6)
        assert(self.word == -1 + 10**6)

    def test_print(self):
        self.word.set_value(12345)
        assert(f"{self.word}" == "+012345")
        self.word *= -1
        assert(f"{self.word}" == "-012345")

class test_uvsim(unittest.TestCase):
    def setUp(self):
        self.sim = UVSim()

    def test_empty(self):
        assert(len(self.sim.memory) == 250)
        assert(self.sim.memory[0] == 0)
        assert(self.sim.accumulator == 0)
    
    def test_convert(self):
        assert(Word(convert("+1234")) == 120034)
        assert(Word(convert("-9876")) == -980076)
    
    def test_readfile(self):
        correct = [100007, 100008, 200007, 320008, 210009, 110009, 430000]
        self.sim.read_file("Test1.txt")
        for i in range(len(correct)):
            assert(self.sim.memory[i] == correct[i])

    def test_load(self):
        self.sim.memory[0].set_value(200010)
        self.sim.memory[10].set_value(123456)
        self.sim.operate()
        assert(self.sim.accumulator == 123456)

    def test_store(self):
        self.sim.memory[0].set_value(210010)
        self.sim.accumulator.set_value(123456)
        self.sim.operate()
        assert(self.sim.memory[10] == 123456)

    def test_add(self):
        self.sim.memory[0].set_value(300010)
        self.sim.memory[10].set_value(5)
        self.sim.accumulator.set_value(10)
        self.sim.operate()
        assert(self.sim.accumulator == 15)

    def test_subtract(self):
        self.sim.memory[0].set_value(310010)
        self.sim.memory[10].set_value(10)
        self.sim.accumulator.set_value(5)
        self.sim.operate()
        assert(self.sim.accumulator == -5)

    def test_divide(self ):
        self.sim.memory[0].set_value(320010)
        self.sim.memory[10].set_value(5)
        self.sim.accumulator.set_value(10)
        self.sim.operate()
        assert(self.sim.accumulator == 2)

    def test_multiply(self ):
        self.sim.memory[0].set_value(330010)
        self.sim.memory[10].set_value(10)
        self.sim.accumulator.set_value(5)
        self.sim.operate()
        assert(self.sim.accumulator == 50)
  
    def test_branch(self):
        self.sim.memory[0].set_value(400010)
        self.sim.operate()
        assert(self.sim.curr == 10)

    def test_branchneg_t(self):
        self.sim.memory[0].set_value(410010)
        self.sim.accumulator.set_value(-1)
        self.sim.operate()
        assert(self.sim.curr == 10)

    def test_branchneg_f(self ):
        self.sim.memory[0].set_value(410010)
        self.sim.accumulator.set_value(1)
        self.sim.operate()
        assert(self.sim.curr == 1)

    def test_branchzero_t(self ):
        self.sim.memory[0].set_value(420010)
        self.sim.operate()
        assert(self.sim.curr == 10)
    
    def test_branchzero_t(self ):
        self.sim.memory[0].set_value(420010)
        self.sim.accumulator.set_value(1)
        self.sim.operate()
        assert(self.sim.curr == 1)

    def test_halt(self):
        self.sim.memory[0].set_value(430000)
        self.sim.operate()
        assert(self.sim.is_halted == True)

if __name__ == '__main__':
    unittest.main()