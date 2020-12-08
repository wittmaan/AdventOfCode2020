import fileinput
from collections import defaultdict

sample_input = """light red bags contain 1 bright white bag, 2 muted yellow bags.
dark orange bags contain 3 bright white bags, 4 muted yellow bags.
bright white bags contain 1 shiny gold bag.
muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.
shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.
dark olive bags contain 3 faded blue bags, 4 dotted black bags.
vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.
faded blue bags contain no other bags.
dotted black bags contain no other bags."""


# --- Day 7: Handy Haversacks ---
# --- Part one ---


def detect_contents(dat: str):
    bag_dict = {}

    for line in dat.split("\n"):
        line = line.replace("bags", "bag")
        key, value = line[:-1].split(" contain ")
        sub_bag_dict = defaultdict(int)

        if value == "no other bag":
            bag_dict[key] = sub_bag_dict
        else:
            content_list = value.split(", ")
            for content in content_list:
                content_splitted = content.split()
                sub_key = " ".join(content_splitted[1:])
                sub_bag_dict[sub_key] = int(content_splitted[0])

            bag_dict[key] = sub_bag_dict
    return bag_dict


def collect_containing_bags(bag_dict, target="shiny gold bag"):
    result = set()
    for actual_bag, sub_bag_dict in bag_dict.items():
        if target in sub_bag_dict:
            result.add(actual_bag)
            result.update(collect_containing_bags(bag_dict=bag_dict, target=actual_bag))
    return result


sample_bag_dict = detect_contents(sample_input)
sample_count = len(collect_containing_bags(sample_bag_dict))
assert sample_count == 4

day7_input = "".join([_ for _ in fileinput.input()])
bag_dict_input = detect_contents(day7_input)
solution_part1 = len(collect_containing_bags(bag_dict_input))
print(f"solution part1: {solution_part1}")
assert solution_part1 == 272


# --- Part two ---


def count_containing_bags(bag_dict, target="shiny gold bag"):
    count = 0
    for actual_bag, actual_count in bag_dict[target].items():
        # print(f"actual_bag {actual_bag}, actual_count={actual_count}")
        count += actual_count * (count_containing_bags(bag_dict=bag_dict, target=actual_bag) + 1)
    return count


sample_counts = count_containing_bags(sample_bag_dict)
assert sample_counts == 32

solution_part2 = count_containing_bags(bag_dict_input)
solution_part2

print(f"solution part2: {solution_part2}")
assert solution_part2 == 172246
