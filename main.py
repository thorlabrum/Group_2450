from word import Word
from uvsim import Memory


def main():
    memory = Memory()
    memory.read_file("Test1.txt")
    memory.operate()

if __name__ == "__main__":
    main()