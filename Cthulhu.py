import sys
import re
import random

class CthulhuInterpreter:
    def __init__(self):
        self.vars = {}

    def run_line(self, line):
        line = line.strip()

        if not line or line.startswith("#"):
            return None

        # Ritual summoning: variable assignment
        if line.startswith("summon"):
            m = re.match(r"summon\s+(\w+)\s*=\s*(.+)", line)
            if m:
                name, expr = m.groups()
                self.vars[name] = self.eval_expr(expr)
                return f"{name} awakened as {self.vars[name]}"

        # Chant: print value
        if line.startswith("chant"):
            expr = line[len("chant"):].strip()
            value = self.eval_expr(expr)
            print(value)
            return value

        # Fuse horrors
        if line.startswith("fuse"):
            parts = line.split()
            if len(parts) == 3:
                a, b = parts[1], parts[2]
                va, vb = self.eval_expr(a), self.eval_expr(b)
                return f"The fusion is {va}{vb}"

        # Banish variable
        if line.startswith("banish"):
            parts = line.split()
            if len(parts) == 2:
                var = parts[1]
                if var in self.vars:
                    del self.vars[var]
                    return f"{var} has been banished to the void"
                else:
                    return f"{var} was never summoned"

        # Whisper secrets
        if line.startswith("whisper"):
            expr = line[len("whisper"):].strip()
            value = str(self.eval_expr(expr))
            scrambled = "".join(random.sample(value, len(value)))
            print(f"(whisper) {scrambled}")
            return scrambled

        # Dream strange transformations
        if line.startswith("dream"):
            expr = line[len("dream"):].strip()
            value = self.eval_expr(expr)
            if isinstance(value, int):
                return f"In dream, {value} becomes {value ** 2} or maybe {value * 13}"
            if isinstance(value, str):
                return f"In dream, '{value}' is written backwards as '{value[::-1]}'"
            return f"The dream distorts {value}"

        # Madness: list variables
        if line.strip() == "madness":
            if not self.vars:
                return "Madness reveals... nothing."
            return "Madness reveals: " + ", ".join(
                f"{k}={v}" for k, v in self.vars.items()
            )

        # Ritual: strange math/string shuffle
        if line.startswith("ritual"):
            parts = line.split()
            if len(parts) == 3:
                a, b = self.eval_expr(parts[1]), self.eval_expr(parts[2])
                if isinstance(a, int) and isinstance(b, int):
                    return f"Ritual binds them: {a * b + random.randint(-5, 5)}"
                else:
                    s = str(a) + str(b)
                    scrambled = "".join(random.sample(s, len(s)))
                    return f"Ritual scrambles them into: {scrambled}"

        # Help command
        if line.lower() == "help":
            return self.help_text()

        return f"The Old Ones do not understand: {line}"

    def eval_expr(self, expr):
        expr = expr.strip()
        if expr in self.vars:
            return self.vars[expr]
        try:
            return eval(expr, {}, self.vars)  # Safe-ish eval
        except:
            return expr

    def help_text(self):
        return (
            "📜 *The Expanded Cthulhu Scrolls* 📜\n"
            "summon <name> = <expr>   → awaken a variable\n"
            "chant <expr>             → speak its value aloud\n"
            "fuse <a> <b>             → merge two horrors into one\n"
            "banish <name>            → forget a variable\n"
            "whisper <expr>           → speak scrambled secrets\n"
            "dream <expr>             → distort a value in dream logic\n"
            "madness                  → list all known variables\n"
            "ritual <a> <b>           → perform a strange binding\n"
            "help                     → show this scroll\n"
            "quit / exit              → escape the abyss\n"
        )


def repl():
    interp = CthulhuInterpreter()
    print("🐙 Welcome to the Cthulhu REPL. Type 'help' for guidance, 'quit' to escape.")
    while True:
        try:
            line = input("cthulhu> ")
        except EOFError:
            break
        if line.strip().lower() in ["quit", "exit"]:
            print("The void closes.")
            break
        result = interp.run_line(line)
        if result is not None:
            print("↯", result)


def run_file(filename):
    interp = CthulhuInterpreter()
    with open(filename, "r") as f:
        for line in f:
            result = interp.run_line(line)
            if result is not None:
                print("↯", result)


if __name__ == "__main__":
    if len(sys.argv) > 1:
        run_file(sys.argv[1])
    else:
        repl()
