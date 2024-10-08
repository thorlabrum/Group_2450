To run UVSim:

1. Prepare a test file with the four number commands the simulator should run, in order. No more than 100 lines.
2. In terminal `python main.py`
3. Press the 'open file' button and choose the text file.
4. Press the 'run' button. The results of each operation and the final memory contents will be displayed in the textbox.

Words:
Words are four number sequences - two digits are the op code, two are the number to preform the opcode on.

Available commands:
Read (10): Reads a word from the keyboard into a specific location in memory.
Write (11): Writes a word from a specific location in memory to screen.
Load (20): Loads a word from a specific location in memory into the accumulator.
Store (21): Store a word from the accumulator into a specific location in memory.
Add (30): Adds a word from a specific location in memory to the word in the accumulator (leave the result in the accumulator)
Subtract (31): Subtracts a word from a specific location in memory from the word in the accumulator (leave the result in the accumulator)
Divide (32): Divide the word in the accumulator by a word from a specific location in memory (leave the result in the accumulator).
Multiply (33): Multiplies a word from a specific location in memory and the word in the accumulator (leave the result in the accumulator).
Branch (40): Branch unconditionally to a specific location in memory (operand).
Negative Branch (41):Branch to a specific location if the accumulator is negative.
Zero Branch (42):Branch to a specific location if the accumulator is zero.
Halt: (43):Halts operate function as dictated by the loaded text file
