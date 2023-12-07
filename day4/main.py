SAMPLE = """
Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11
"""

class Card:

    deck = []
    pile = 0

    keymap = {}

    def __init__(self, string):
        parts = string.split(':')
        self.number = int(parts[0].split()[1])
        self.row = parts[1]

        self.live = True
        Card.deck.append(self)

        self.keymap[self.number] = string

    def process(self):
        if not self.live:
            return

        a, b = [[int(x) for x in part.split() if x.isdigit()] for part in self.row.split('|')]
        i = len(set(a) &  set(b)) 

        # print(self.number, 'has', i)

        for j in range(i):
            Card(Card.keymap[self.number+j+1])

        self.live = False
        Card.pile += 1

    @classmethod
    def clean(self):
        Card.deck = [c for c in Card.deck if c.live]
        print(f'pile: {Card.pile} | deck: {len(Card.deck)} | keymap: {len(Card.keymap)}')


    @classmethod
    def pop(self):
        for _ in range(10000):
            c = Card.deck.pop() if Card.deck else None
            _ = c.process() if c else None
        print(f'pile: {Card.pile:_} | deck: {len(Card.deck)} | keymap: {len(Card.keymap)}')

def main():


    with open("puzzle.txt", "r") as file:
        rows = [r for r in file.read().split("\n") if r]

    # rows = [r for r in SAMPLE.split('\n') if r]

    total = 0
    for row in rows:
        a, b = [[int(x) for x in part.split() if x.isdigit()] for part in row.split('|')]
        i = len(set(a) &  set(b))
        points =  2**(i-1) if i > 1 else i
        total += points
    print(total)


    for row in rows:
        c = Card(row)

    while Card.deck:
        Card.pop()

    print(Card.pile)


if __name__ == "__main__":
    main()
