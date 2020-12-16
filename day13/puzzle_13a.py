



from functools import reduce

def chinese_remainder(n, a):
    sum = 0
    prod = reduce(lambda a, b: a * b, n)
    for n_i, a_i in zip(n,a):
        p = prod / n_i
        sum += a_i * mul_inv(p, n_i) * p
    return sum % prod

def mul_inv(a, b):
    b0 = b
    x0, x1 = 0,1
    if b == 1: return 1
    while a > 1 :
        q = a // b
        a, b = b, a % b
        x0, x1 = x1 - q * x0, x0
    if x1 < 0: x1 += b0
    return x1


PUZZLE_DAY = '13'


def y(bus_set):
    return bus_set[0] * bus_set[2] - bus_set[1]

def ys_equal(bus_sets):
    return len(set([y(a) for a in bus_sets])) == 1

def calculate(bus_set, target_y):
    multiplier = (target_y + bus_set[1]) // bus_set[0]
    return multiplier

def ys_list(bus_sets):
    return [y(a) for a in bus_sets]

def main(input_mode, test_mode = False):
    if test_mode:
        input_file = f'puzzle_{PUZZLE_DAY}_test.txt'
    else:
        input_file = f'puzzle_{PUZZLE_DAY}_input.txt'

    with open(input_file) as fp:
        lines = fp.readlines()

    # # Part 1
    # earliest_time = int(lines[0])
    # buses = [int(x) for x in lines[1].split(',') if x != 'x']

    # print(buses)


    # time_to_bus = {}
    # for bus in buses:
    #   near_time = (earliest_time // bus) * bus

    #   if near_time <= earliest_time:
    #       next_time = near_time + bus
    #       time_to_bus[bus] = next_time
    #   else:
    #       next_time = near_time
    #   print(bus, near_time, next_time)

    # min_time, min_bus = 0, 0
    # for bus, time in time_to_bus.items():
    #   if time < min_time or min_time == 0:
    #       min_time = time
    #       min_bus = bus

    # print(f'min_time {min_time}, bus {bus}')
    # time_to_wait  = min_time - earliest_time
    # print("Multiple: ", time_to_wait * min_bus)

    
    # 1797391531030110 too high
    # 279739153103011 wrong
    # 179739153103011 too low
    # 100030606600000 too low
    # Part 2
    buses = lines[1].split(',')
    bus_to_index  = []
    max_bus = 0
    for i, bus in enumerate(buses):
        if bus == 'x':
            pass
        else:
            bus_to_index.append([int(bus), i])
            if int(bus) > max_bus:
                max_bus = int(bus)

    print(bus_to_index)
    n = [k[0] for k in bus_to_index]
    a = [-k[1] for k in bus_to_index]
    # n=[3,5,7]
    # a=[2,3,2]
    print(chinese_remainder(n,a))
    # 534035653563209

if __name__ == '__main__':
    input_mode = 'standard'
    test_mode = True
    main(input_mode, test_mode)
