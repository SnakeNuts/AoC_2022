from parse import *

stacks = dict()


def move(source: int, destination: int, count: int):
    # print(f"Moving {count} crates from {source} to {destination}")
    temp_stack = list()
    for i in range(count):
        # print("Moving...")
        top_crate = stacks[source].pop()
        temp_stack.append(top_crate)

    for i in range(count):
        stacks[destination].append(temp_stack.pop())


def run():
    with open("day5_data.txt") as data:
        finished_setup = False
        while not finished_setup:
            line = data.readline()
            if '[' not in line:
                finished = True
                break
            crate_count = (len(line)) // 4
            for i in range(crate_count):
                crate = line[i*4:(i*4)+4]
                if i not in stacks.keys():
                    stacks[i] = list()
                if crate.strip() != '':
                    crate_letter = parse("[{letter}]", crate.strip())
                    stacks[i].append(crate_letter['letter'])
                else:
                    stacks[i].append('')
        for stack in stacks.keys():
            stacks[stack].reverse()
            while '' in stacks[stack]:
                stacks[stack].remove('')

        # stacks read. let's get moving
        data.readline()  # skip empty line
        while True:
            instruction = data.readline().strip()
            if instruction == '':
                break
            result = parse("move {count:d} from {source:d} to {destination:d}", instruction)
            move(result['source']-1, result['destination']-1, result['count'])

        for stack_key in stacks.keys():
            print(stacks[stack_key].pop(), end='')


if __name__ == "__main__":
    run()

