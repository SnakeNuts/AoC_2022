

def run():
    overlap_count = 0
    with open("day4_data.txt") as data:
        for pair in data.readlines():
            assignments = pair.strip().split(',', 1)
            assignment_1_numbers = assignments[0].split('-', 1)
            assignment_2_numbers = assignments[1].split('-', 1)

            assignment_1_sections = list()
            for section in range(int(assignment_1_numbers[0]), int(assignment_1_numbers[1]) + 1):
                assignment_1_sections.append(section)

            assignment_2_sections = list()
            for section in range(int(assignment_2_numbers[0]), int(assignment_2_numbers[1]) + 1):
                assignment_2_sections.append(section)

            overlap = set.intersection(set(assignment_1_sections), set(assignment_2_sections))

            if len(overlap) > 0:
                overlap_count += 1

    print(overlap_count)


if __name__ == "__main__":
    run()