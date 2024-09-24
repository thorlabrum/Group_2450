from uvsim import UVSim

"""
Use cases:
1. READ words from the keyboard, so that I can perform operations on a number of my chosen at run time without editing source code.
2. WRITE words to the screen, so that I can see the results of the code I've written
3. LOAD words from memory into the accumulator, so that I can operate on memory
4. STORE words in accumulator to the memory, so that I can save the operations I've done
5. ADD words to the accumulator, so that I can find the sum of any two numbers between 4300 & 9999 *that dont overflow
6. SUBTRACT words (from memory) from the accumulator, so that I can compare (if negative then <, if positive then >)
7. DIVIDE the accumulator by a word from memory, so that I can determine if a number is even or odd, based on if there is a remainder
8. MULTIPLY the accumulator by a word from memory so that I can square numbers by multiplying a word by itself
9. BRANCH to a specific location, so that I can loop the program
10. BRANCH to a location if the accumulator is NEGative, so that I can loop if A>B as described in 6.
11. BRANCH to a location if the accumulator is ZERO, so that I can loop a specific number by subtracting the accumulator by one each iteration.
12. HALT the program, so that it doesn't run forever
13. Differentiate between command values and data values so that the program treats each appropriately.
"""

def test_read1():
    sim = UVSim()
    sim.read_input([1111, 4300])
    assert sim.memory[0] == 1111

def test_read_2():
    sim = UVSim()
    assert sim.read_input(['here']) == ValueError

def test_write1():
    sim = UVSim()
    sim.read_input([1111, 4300])
    sim.operate()

def test_write2():
    sim = UVSim()
    sim.read_input([1154, 4300])
    sim.operate()

def test_load1():
    sim = UVSim()
    sim.read_input([2087, 4300])
    sim.operate()
    assert sim.accumulator == 00

def test_load2():
    sim = UVSim
    sim.read_input([2028, 4300])
    sim.operate()
    assert sim.accumulator == 00

def test_store1(): 
    sim = UVSim()
    sim.read_input([2028, 2102, 4300])
    sim.operate()
    assert sim.memory[2] == 28

def test_store2():
    sim = UVSim
    sim.read_input([2087, 2104, 4300])
    sim.operate()
    assert sim.memory[4] == 87

def test_add1():
    sim = UVSim()
    sim.read_input([2003, 3005, 4300, 1005])
    sim.operate()
    assert sim.accumulator == 1010

def test_add2():
    sim = UVSim()
    sim.read_input([2003, 3007, 4300, 5000])
    sim.operate()
    assert sim.accumulator == 5007

def test_subtract1():
    sim = UVSim()
    sim.read_input([2003, 3107, 4300, 5000])
    sim.operate()
    assert sim.accumulator == 4993

def test_subtract2():
    sim = UVSim()
    sim.read_input([2003, 3005, 4300, 1005])
    sim.operate()
    assert sim.accumulator == 1000

def test_divide1():
    sim = UVSim()
    sim.read_input([2003, 3205, 4300, 1000])
    sim.operate()
    assert sim.accumulator == 200

def test_divide2():
    sim = UVSim()
    sim.read_input([2003, 3210, 4300, 5000])
    sim.operate()
    assert sim.accumulator == 500

def test_multiply1():
    sim = UVSim()
    sim.read_input([2003, 3303, 4300, 1000])
    sim.operate()
    assert sim.accumulator == 3000

def test_multiple2():
    sim = UVSim()
    sim.read_input([2003, 3310, 4300, '0500'])
    sim.operate()
    assert sim.accumulator == 5000

def test_branch1():
    sim = UVSim()
    sim.read_input([4003, 4300])
    sim.operate()
    assert sim.curr == 3

def test_branch2():
    sim = UVSim()
    sim.read_input([4067, 4300])
    sim.operate()
    assert sim.curr == 67

def nbranch1():
    sim = UVSim()
    sim.read_input([2003, 3303, 4115, 4300, 1000])
    sim.operate()
    assert sim.curr == 3

def nbranch2():
    sim = UVSim()
    sim.read_input([2003, 3105, 4115, 4300, 1000])
    sim.operate()
    assert sim.curr == 15

def test_zbranch1():
    sim = UVSim()
    sim.read_input([2003, 3303, 4215, 4300, 1000])
    sim.operate()
    assert sim.curr == 3

def test_zbranch2():
    sim = UVSim()
    sim.read_input([2000, 4215, 4300])
    sim.operate()
    assert sim.curr == 15

def test_halt():
    sim = UVSim()
    sim.read_input([4300])
    sim.operate()
    assert sim.is_halted == True

def test_halt():
    sim = UVSim()
    sim.read_input([2003, 3303, 1000])
    sim.operate()