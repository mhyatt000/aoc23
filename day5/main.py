SAMPLE = """
seeds: 79 14 55 13

seed-to-soil map:
50 98 2
52 50 48

soil-to-fertilizer map:
0 15 37
37 52 2
39 0 15

fertilizer-to-water map:
49 53 8
0 11 42
42 0 7
57 7 4

water-to-light map:
88 18 7
18 25 70

light-to-temperature map:
45 77 23
81 45 19
68 64 13

temperature-to-humidity map:
0 69 1
1 0 69

humidity-to-location map:
60 56 37
56 93 4
"""

from tqdm import tqdm
from concurrent.futures import ProcessPoolExecutor

class KEYMAP:

    maps = []

    def __init__(self, *rows):
        self.name = rows[0].strip(':')

        self.spread = {}
        for r in tqdm(rows[1:], desc=self.name, leave=False):
            bstart, astart, length = [int(x) for x in r.split()]
            d = {
                a: b
                for a, b in zip(
                    range(astart, astart + length), range(bstart, bstart + length)
                )
            }
            self.spread.update(d)

        KEYMAP.maps.append(self)

    def get(self, key):
        return self.spread.get(key, key)

    def __repr__(self):
        return f"<KEYMAP {self.name}>"


def main():

    """So, the lowest location number in this example is 35."""

    with open("puzzle.txt", "r") as file:
        sections = [r for r in file.read().split("\n\n") if r]
    # sections = [r for r in SAMPLE.split('\n\n') if r]

    sections = [[r for r in s.split('\n') if r] for s in sections]

    seeds = [int(x) for x in sections[0][0].split()[1:]]
    for sec in tqdm(sections[1:], desc='building keymaps...', leave=False):
        KEYMAP(*sec)

    print(KEYMAP.maps)

    for m in tqdm(KEYMAP.maps):
        with ProcessPoolExecutor() as ex:
            seeds = ex.map(m.get, seeds)

    print(min(seeds))


if __name__ == "__main__":
    main()
