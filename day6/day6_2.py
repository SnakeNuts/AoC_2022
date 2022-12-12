

def run():
    with open("day6_input.txt") as data:
        stream = data.readline().strip()
        index = 0
        while index < len(stream):
            marker = stream[index:index+14]
            index += 1
            marker_set = set(marker)
            if len(marker_set) == 14:
                print(marker, index + 13)
                break


if __name__ == "__main__":
    run()