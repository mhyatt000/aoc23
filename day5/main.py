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

from concurrent.futures import ThreadPoolExecutor

from tqdm import tqdm


class KEYMAP:
    maps = []

    def __init__(self, *rows):
        self.name = rows[0].strip(":")
        extract = lambda r: [int(x) for x in r.split()]
        self.rows = [extract(r) for r in rows[1:]]
        KEYMAP.maps.append(self)
        self.f = lambda b, a, l, x: b + (x - a) if a <= x < a + l else None

    def process(self, x):
        result = [self.f(*r, x) for r in self.rows]
        result = [r for r in result if r != None]
        return result[0] if len(result) else x


    # def _make(self):
        # F = []
        # for r in tqdm(self.rows[1:], desc=self.name, leave=False):
            # b, a, l = [int(x) for x in r.split()]
            # f = lambda a, b, l, x: b + (x - a) if a <= x < a + l else x
            # f = lambda x: x + r[0] - r[1] if (x >= r[1] and x < (r[1] + r[2])) else x
            # F.append(f)
        # self.g = lambda x: [f(x) for f in F if f(x) != x]

    def clear(self):
        """for space purposes"""
        del self.spread

    def get(self, key):
        return self.process(key)
        return self.spread.get(key, key)

    def __repr__(self):
        return f"<KEYMAP {self.name}>"


def main():
    """So, the lowest location number in this example is 35."""

    with open("puzzle.txt", "r") as file:
        sections = [r for r in file.read().split("\n\n") if r]
    # sections = [r for r in SAMPLE.split("\n\n") if r]

    sections = [[r for r in s.split("\n") if r] for s in sections]

    seeds = [int(x) for x in sections[0][0].split()[1:]]
    seeds = [(a,b) for a,b in zip(seeds[::2],seeds[1::2])]

    for sec in tqdm(sections[1:], desc="building keymaps...", leave=False):
        KEYMAP(*sec)

    print(KEYMAP.maps)

    def mygenerator(a, b):
        for num in range(a, a + b):
            yield num

    total = sum([s[1] for s in seeds])

    lowest = None
    prog = tqdm(total=total)
    for (a,b) in seeds:

        def job(seed):
            for m in KEYMAP.maps:
                seed = m.get(seed) 
            prog.update()
            return seed

        with ThreadPoolExecutor() as ex:
            seeds = ex.map(job, mygenerator(a,b))

        candidate = min(seeds)
        lowest = min(candidate, lowest) if type(lowest) is int else candidate

    print(lowest)


if __name__ == "__main__":
    main()
