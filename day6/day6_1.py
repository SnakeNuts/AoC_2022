

def run():
    with open("day6_input.txt") as data:
        stream = data.readline().strip()
        index = 0
        while index < len(stream):
            marker = stream[index:index+4]
            index += 1
            marker_set = set(marker)
            if len(marker_set) == 4:
                print(marker, index + 3)
                break


if __name__ == "__main__":
    run()