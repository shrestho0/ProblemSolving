with open("day02/src/input2.txt") as f:
    # max_cubes = {"red": 12, "green": 13, "blue": 14} 
    red_m, green_m, blue_m = 12, 13, 14
    valid_ids = []
    for line in f.readlines():
        something, data = parse_input(line.strip())