import os

def read_file(file):
    with open(file) as f:
        #print(f)
        lines = f.readlines()
        #print(lines)
    return [line.strip("\n") for line in lines] 


def is_larger(input):
    count = 0
    for i in range(1,len(input)):
        if int(input[i]) > int(input[i-1]):
            count += 1
    return count


def count_threes(input):
    counts = []
    for i in range(len(input) -2):
        counts.append( int(input[i]) + int(input[i + 1]) + int(input[i + 2]))
    return counts



if __name__ == "__main__":
    input = read_file(os.getcwd() + "\input\day1.txt")
    threes = count_threes(input)
    result = is_larger(threes)
    print(result)