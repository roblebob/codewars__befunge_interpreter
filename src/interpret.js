const DEBUG = false;

class Plane {
  constructor(code) {
    this.plane = code.split("\n").map((line) => line.split(""));
    this.pos = [0, 0]; // [row, col]
    this.dir = [0, 1]; // [row, col]
  }

  get isFinished() {
    return this.currentChar === "@";
  }

  get currentChar() {
    return this.plane[this.pos[0]][this.pos[1]];
  }

  move() {
    this.pos = [this.pos[0] + this.dir[0], this.pos[1] + this.dir[1]];
    this.correctPos();
  }

  get isCorrectPos() {
    return (
      this.pos[0] >= 0 &&
      this.pos[1] >= 0 &&
      this.pos[0] < this.plane.length &&
      this.pos[1] < this.plane[this.pos[0]].length
    );
  }

  correctPos() {
    while (!this.isCorrectPos) {
      if (this.pos[0] === -1) this.pos[0] = this.plane.length - 1;
      else if (this.pos[0] === this.plane.length) this.pos[0] = 0;
      else if (this.pos[1] === -1) {
        this.pos[1] = this.plane[this.pos[0]].length - 1;
        this.pos[0]--;
      } else if (this.pos[1] === this.plane[this.pos[0]].length) {
        this.pos[1] = 0;
        this.pos[0]++;
      } else {
        throw new Error(`Invalid position ${this.pos}`);
      }
    }
  }

  print() {
    console.log(this.plane.map((line) => line.join("")).join("\n"));
  }
}

function interpret(code) {
  let _i = 0;
  const plane = new Plane(code);

  if (DEBUG) plane.print();

  let output = "";
  const stack = [];

  const printState = () => {
    console.log(_i++, ":");
    if (plane.currentChar === " ") return;
    console.log("  Pos:", plane.pos, "  Dir:", plane.dir);
    console.log("  Char:", plane.currentChar);
    console.log("  Stack:", JSON.stringify(stack));
    console.log("  Output:", output);
  };

  while (!plane.isFinished && _i < 50) {
    const char = plane.currentChar;
    if (DEBUG) printState();

    if (/\d/.test(char)) {
      if (DEBUG) console.log("                   Pushing", +char);
      stack.push(+char);
    } else {
      switch (char) {
        case "+":
          stack.push(stack.pop() + stack.pop());
          break;
        case "-":
          stack.push(-1 * stack.pop() + stack.pop());
          break;
        case "*":
          stack.push(stack.pop() * stack.pop());
          break;
        case "/": {
          const a = stack.pop();
          const b = stack.pop();
          stack.push(a === 0 ? 0 : Math.floor(b / a));
          break;
        }
        case "%": {
          const a = stack.pop();
          const b = stack.pop();
          stack.push(a === 0 ? 0 : b % a);
          break;
        }
        case "!":
          stack.push(stack.pop() === 0 ? 1 : 0);
          break;
        case "`":
          stack.push(stack.pop() < stack.pop() ? 1 : 0);
          break;

        case ">":
          plane.dir = [0, 1];
          break;
        case "<":
          plane.dir = [0, -1];
          break;
        case "^":
          plane.dir = [-1, 0];
          break;
        case "v":
          plane.dir = [1, 0];
          break;
        case "?":
          plane.dir = [
            [0, 1],
            [0, -1],
            [1, 0],
            [-1, 0],
          ][Math.floor(Math.random() * 4)];
          break;

        case "_":
          plane.dir = stack.pop() === 0 ? [0, 1] : [0, -1];
          break;
        case "|":
          plane.dir = stack.pop() === 0 ? [1, 0] : [-1, 0];
          break;

        case '"':
          plane.move();
          while (plane.currentChar !== '"') {
            stack.push(plane.currentChar.charCodeAt(0));
            plane.move();
          }
          break;

        case ":":
          stack.push(stack.length === 0 ? 0 : stack[stack.length - 1]);
          break;

        case "\\":
          if (stack.length < 2) {
            stack.push(0);
          } else {
            const a = stack.pop();
            const b = stack.pop();
            stack.push(a);
            stack.push(b);
          }
          break;

        case "$":
          stack.pop();
          break;

        case ".":
          output += stack.pop();
          break;

        case ",":
          output += String.fromCharCode(stack.pop());
          break;

        case "#":
          plane.move();
          break;

        case "p": {
          const y = stack.pop();
          const x = stack.pop();
          plane.plane[y][x] = String.fromCharCode(stack.pop());
          break;
        }
        case "g": {
          const y = stack.pop();
          const x = stack.pop();
          stack.push(plane.plane[y][x].charCodeAt(0));
          break;
        }
        case " ":
          break;
      }
    }
    plane.move();
  }
  return output;
}

//console.log('Factorial (8! = 40320):   ', interpret("08>:1-:v v *_$.@\n  ^    _$>\\:^"));

console.log("Quine:   ", interpret("01->1# +# :# 0# g# ,# :# 5# 8# *# 4# +# -# _@"));
