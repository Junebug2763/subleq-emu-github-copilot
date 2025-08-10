import sys

class SubleqEmulator:
    def __init__(self, memory):
        self.memory = memory
        self.pc = 0

    def run(self):
        while self.pc < len(self.memory):
            a = self.memory[self.pc]
            b = self.memory[self.pc + 1]
            c = self.memory[self.pc + 2]
            # Handle negative indices as exit signal (convention)
            if a < 0 or b < 0 or c < 0:
                break

            # Perform SUBLEQ: memory[b] = memory[b] - memory[a]
            self.memory[b] = self.memory[b] - self.memory[a]
            # If result <= 0, branch to c; else pc += 3
            if self.memory[b] <= 0:
                self.pc = c
            else:
                self.pc += 3

def load_subleq_program(filename):
    with open(filename) as f:
        contents = f.read()
    # Assume program is a whitespace-separated list of integers
    program = [int(x) for x in contents.split()]
    # Memory size can be larger than program if needed
    memory = program + [0] * (4096 - len(program))
    return memory

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python subleq_emulator.py dawnos.subleq")
        sys.exit(1)
    memory = load_subleq_program(sys.argv[1])
    emulator = SubleqEmulator(memory)
    emulator.run()
