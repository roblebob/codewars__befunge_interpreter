import random
 
class Plane:
    def __init__(self, code):
        self.plane = [list(row) for row in code.split("\n")]
        self.pos = [0, 0] # [row, column]
        self.direction = [0, 1]
 
    def print(self):
        for row in self.plane:
            print("".join(row))

    def get_current_char(self):
        return self.plane[self.pos[0]][self.pos[1]]

    def is_finished(self):
        return self.get_current_char() == "@"

    def move(self):
        self.pos = [self.pos[0] + self.direction[0], self.pos[1] + self.direction[1]]
        self.correct_position()

    def is_correct_position(self):
        return self.pos[0] >= 0 and self.pos[1] >= 0 and self.pos[0] < len(self.plane) and self.pos[1] < len(self.plane[self.pos[0]])

    def correct_position(self):
        while not self.is_correct_position():
            if self.pos[0] == -1:
                self.pos[0] = len(self.plane) - 1

            elif self.pos[0] == len(self.plane):
                self.pos[0] = 0
            
            elif self.pos[1] == -1:
                self.pos[1] = len(self.plane[self.pos[0]]) - 1
                self.pos[0] -= 1

            elif self.pos[1] == len(self.plane[self.pos[0]]):
                self.pos[1] = 0
                self.pos[0] += 1

            else:
                raise Exception("Invalid position")



 

def interpret(code):
    
    plane = Plane(code)
    output = ""
    stack = []

    while not plane.is_finished():
        char = plane.get_current_char()

        if char.isdigit():
            stack.append(int(char))


        elif char == "+":
            stack.append(stack.pop() + stack.pop())

        elif char == "-":
            stack.append(-stack.pop() + stack.pop())

        elif char == "*":
            stack.append(stack.pop() * stack.pop())

        elif char == "/":
            stack.append(int((1 / stack.pop()) * stack.pop()))

        elif char == "%":
            a = stack.pop()
            b = stack.pop()
            stack.append(stack.pop() % stack.pop())

        elif char == "!":
            stack.append(1 if stack.pop() == 0 else 0)

        elif char == "`":
            stack.append(1 if stack.pop() < stack.pop() else 0)


        elif char == ">":
            plane.direction = [0, 1]

        elif char == "<":
            plane.direction = [0, -1]

        elif char == "v":
            plane.direction = [1, 0]

        elif char == "^":
            plane.direction = [-1, 0]

        elif char == "?":
            plane.direction = [[0, 1], [0, -1], [1, 0], [-1, 0]][random.randint(0, 3)]        


        elif char == "_":
            plane.direction = [0, 1] if stack.pop() == 0 else [0, -1]

        elif char == "|":
            plane.direction = [1, 0] if stack.pop() == 0 else [-1, 0]

        elif char == "\"":
            plane.move()
            while plane.get_current_char() != "\"":
                stack.append(ord(plane.get_current_char()))
                plane.move()

        elif char == ":":
            stack.append(0 if len(stack) == 0 else stack[-1])
            
        elif char == "\\":
            if len(stack) < 2:
                stack.append(0)
            else:
                a = stack.pop()
                b = stack.pop()
                stack.append(a)
                stack.append(b)

        elif char == "$":
            stack.pop()
        
        elif char == ".":
            output += str(stack.pop())

        elif char == ",":
            output += chr(stack.pop())

        elif char == "#":
            plane.move()

        elif char == "p":
            y = stack.pop()
            x = stack.pop()
            v = stack.pop()
            plane.plane[y][x] = chr(v)

        elif char == "g":
            y = stack.pop()
            x = stack.pop()
            stack.append(ord(plane.plane[y][x]))

        elif char == " ":
            pass

        else:
            raise Exception(f"Invalid character: {char}")
        
        plane.move()
    
    return output

print(interpret(">987v>.v\nv456<  :\n>321 ^ _@"))