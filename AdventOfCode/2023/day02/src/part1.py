def parse_input(line):
    game_id, game_data = line.strip().split(":")
    game_rounds = game_data.split(";")
    current_round_gain = {"red": 0, "green": 0, "blue": 0}
    max_gain = {"red": 12, "green": 13, "blue": 14}
    for game in game_rounds:
        cubes = game.strip().split(",")
        for cube in cubes:
            ccoutn, ccolor = cube.strip().split(" ")
            ccoutn = int(ccoutn)
            if ccoutn > max_gain[ccolor]:
                return 0, {}

            current_round_gain[ccolor] += ccoutn

    return int(game_id.split(" ")[1]), current_round_gain


with open("day02/src/input2.txt") as f:
    # max_cubes = {"red": 12, "green": 13, "blue": 14}
    red_m, green_m, blue_m = 12, 13, 14
    valid_ids = []
    for line in f.readlines():
        something, data = parse_input(line.strip())
        if something:
            valid_ids.append(something)

        print()
    print(valid_ids, sum(valid_ids))

    # game_id, game_data = parse_input(line)
    # if not (
    #     game_data["red"] > required_cubes["red"]
    #     or game_data["blue"] > required_cubes["blue"]
    #     or game_data["green"] > required_cubes["green"]
    # ):
    #     valid_rounds.update({game_id: game_data})
    # print(valid_rounds.keys(), sum(valid_rounds.keys()))
    # print(find_games(valid_rounds, required_cubes))
