from word import Word
from uvsim import UVSim 


def main():
    sim = UVSim()
    sim.read_file(input("Which file would you like to read?\n>"))
    sim.operate()

if __name__ == "__main__":
    main()
