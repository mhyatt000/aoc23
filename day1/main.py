from tqdm import tqdm

matches = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

def _sub(x):
    """matches by first character, not by number order"""


    for i, m in enumerate(matches):
        x = x.replace(m, f"{i+1}")
    return x


def sub(x):
    """super inneficient... should prob use re"""
    partial = ""
    for a in x:
        partial += a
        partial = _sub(partial)
    return partial


def subbwd(x):
    """super inneficient... should prob use re"""
    partial = ""
    for a in x[::-1]:
        partial = a+partial
        partial = _sub(partial)
    return partial


def main():
    with open("puzzle.txt", "r") as f:
        data = [x for x in f.read().split("\n") if x]

    nums = [str(x) for x in range(10)]
    filterdigits = lambda X: [x if x in nums else None for x in X ] 

    first = [filterdigits(sub(s))[0] for s in tqdm(data)]
    last = [filterdigits(subbwd(s))[-1] for s in tqdm(data)]

    digits = [[x for x in [a,b] if type(x) is str] for a,b in zip(first,last)]

    digits = [[d[0]] + d for d in digits if len(d)]
    print(digits)
    total = sum([int(f"{d[0]}{d[-1]}") for d in digits])

    print(total)


# 55447

if __name__ == "__main__":
    main()
