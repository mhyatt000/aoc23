from tqdm import tqdm

SAMPLE = """
Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green
"""
ans = 8

SAMPLE2 = """
Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green
"""


RULE = "12 red, 13 green, 14 blue "


def split_into_games(sample):
    return sample.strip().split("\n")


def remove_game_label(game):
    return game.split(": ")[1] if ":" in game else game


def split_into_rounds(game_data):
    return game_data.split("; ")


def create_color_count_dict(round):
    color_counts = round.split(", ")
    round_dict = {}
    for color_count in color_counts:
        count, color = color_count.split(" ")
        round_dict[color] = int(count)
    return round_dict


def process_sample(sample):
    games = split_into_games(sample)
    parsed_games = []
    for game in games:
        game_data = remove_game_label(game)
        rounds = split_into_rounds(game_data)
        round_dicts = [create_color_count_dict(round) for round in rounds]
        parsed_games.append(round_dicts)
    return parsed_games

def impossible(round, rule):
    """ returns trrue if a round is impossible """
    
    # any color is higher than the allotted colors
    for color,v in round.items():
        if v > rule[color]:
            return True

    return False

def main():
    with open("puzzle.txt", "r") as f:
        data = f.read()

    sample = process_sample(data)
    rule = process_sample(RULE)[0][0]

    total = sum(range(1,len(sample)+1))
    print(total)

    for i, game in enumerate(sample):
        for round in game:
            if impossible(round, rule):
                total -= (i+1)
                break

    print(rule)
    print(total)

    print('part2')

    powers = []
    for i, game in enumerate(sample):
        pow = {c:max([round.get(c,0) for round in game]) for c in rule.keys()}.values()
        from functools import reduce 
        power = reduce(lambda x,y: x*y, pow,  1)
        powers.append(power)

    print(sum(powers))
    

if __name__ == "__main__":
    main()
