import os


"""
reads file and returns all values as an array
"""
def read_file(file):
    with open(file) as f:
        lines = f.readlines()
    return [line.strip("\n") for line in lines] 


def calc_position(input):
    depth = 0
    horizontal = 0
    for line in input:
        new_line = (line.rsplit())
        if new_line[0] == "forward":
            horizontal += int(new_line[1])
        elif new_line[0] == "down":
            depth += int(new_line[1])
        elif new_line[0] == "up":
            depth -= int(new_line[1])
    return horizontal, depth


def calc_position2(input):
    depth = 0
    horizontal = 0
    aim = 0
    for line in input:
        new_line = (line.rsplit())
        if new_line[0] == "forward":
            horizontal += int(new_line[1])
            depth += aim * int(new_line[1])
        elif new_line[0] == "down":
            aim += int(new_line[1])
        elif new_line[0] == "up":
            aim -= int(new_line[1])

    return horizontal, depth




if __name__ == "__main__":
    input = read_file(os.getcwd() + "\input\day2.txt")
    #threes = count_threes(input)
    horizontal, depth = calc_position(input)
    print(horizontal * depth)