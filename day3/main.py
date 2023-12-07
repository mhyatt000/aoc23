SAMPLE = """
467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598..
"""

ANS = 4361

"""
If you can add up all the part numbers in the engine schematic...
any number adjacent to a symbol, even diagonally, is a "part number"
"""

import re


class Node:
    numbered = []
    symboled = []

    def __init__(self, i, j, value=None):
        if not value:
            return

        self.i = i
        self.j = j

        try:
            value = int(value)
            Node.numbered.append(self)
        except:
            Node.symboled.append(self)

        self.value = value

    def ispart(self, gear=None):
        assert type(self.value) is int

        digits = len(str(self.value))

        irange = list(range(self.i - 1, self.i + 2))
        jrange = list(range(self.j - (digits + 1), self.j + 1))
        from itertools import product

        p = list(product(irange, jrange))

        if gear == None:
            for s in Node.symboled:
                if any([(s.i, s.j) == x for x in p]):
                    return True
            return False
        else:
            if any([(gear.i, gear.j) == x for x in p]):
                return True
        return False

    def gear_ratio(self):
        if self.value != "*":
            return 0
        ratios = [node.value for node in Node.numbered if node.ispart(self)]
        return ratios[0] * ratios[1] if len(ratios) == 2 else 0

    def __repr__(self):
        return f"<Node: {self.value} @ {(self.i, self.j)}>"


def main():
    with open("puzzle.txt", "r") as file:
        rows = [r for r in file.read().split("\n") if r]

    # rows = [r for r in SAMPLE.split('\n') if r]

    nums = [str(i) for i in range(10)]
    out = []

    for i, row in enumerate(rows):
        partial = ""
        sub = []
        for j, c in enumerate(row):
            if c in nums:
                partial += str(c)
            else:
                if partial:
                    Node(i, j, partial)
                    partial = ""
                _ = Node(i, j, c) if not c == "." else 0

        if partial:
            Node(i, j, partial)
        out.append(sub)

    # for i,o in enumerate(out):
    # for j,x in enumerate(o):
    # Node(i,j,x)

    total = 0
    for num in Node.numbered:
        if num.ispart():
            total += num.value

    print(total)

    print(sum([gear.gear_ratio() for gear in Node.symboled]))


if __name__ == "__main__":
    main()
