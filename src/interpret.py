class Plane:
    def __init__(self, code):
        self.plane = [list(row) for row in code.split("\n")]
        self.pos = [0, 0]
        self.direction = 0
        self.output = ""
 
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
                # throw("Error")
                pass


def interpret(code):
    
    plane = Plane(code)
    
    plane.print()



interpret(">987v>.v\nv456<  :\n>321 ^ _@")