import sys
import msvcrt

array = [0] * 255
pointer = 0

def run(array: list, pointer: int, cmd: str):
    count = 0
    loops = []
    while count < len(cmd):
        char = cmd[count]
        if char == ">":
            pointer = (pointer + 1) % len(array)
        elif char == "<":
            pointer = (pointer - 1) % len(array)
        elif char == "+":
            array[pointer] = (array[pointer] + 1) % 256
        elif char == "-":
            array[pointer] = (array[pointer] - 1) % 256
        elif char == ".":
            sys.stdout.write(chr(array[pointer]))
            sys.stdout.flush()
        elif char == ",":
            while not msvcrt.kbhit():
                pass
            array[pointer] = ord(msvcrt.getch().decode('utf-8'))
        elif char == "[":
            if array[pointer] == 0:
                open_brackets = 1
                while open_brackets:
                    count += 1
                    if count >= len(cmd):
                        raise SyntaxError("Unmatched '['")
                    if cmd[count] == "[":
                        open_brackets += 1
                    elif cmd[count] == "]":
                        open_brackets -= 1
            else:
                loops.append(count)
        elif char == "]":
            if array[pointer] != 0:
                count = loops[-1]
            else:
                loops.pop()

        count += 1
    return array, pointer

try:
    with open(sys.argv[1], "r") as file:
        array, pointer = run(array, pointer, file.read())
except IndexError:
    print("This BrainFuck interpreter created by Neo Rafajlovic.\n")
    while True:
        prompt = input("\n> ")
        array, pointer = run(array, pointer, prompt)
