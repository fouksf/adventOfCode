

input = list(map(int, open("2021/7/input.txt", "r").read().split(",")))


def calculate_fuel_for_position(crab_positions, position):
    return sum(list(map(lambda p: abs(position - p) ,crab_positions)))


def calculate_fuel_for_position_v2(crab_positions, position):
    return sum(list(map(lambda p: sum(range(0, abs(position - p) + 1)), crab_positions)))


def find_cheapest_position(crab_positions):
    min_fuel = calculate_fuel_for_position_v2(crab_positions, 1101)
    print(min_fuel)
    for position in range(min(crab_positions), max(crab_positions)):
        consumption = calculate_fuel_for_position_v2(crab_positions, position)
        if consumption < min_fuel:
            min_fuel = consumption
    return min_fuel

print(find_cheapest_position(input))