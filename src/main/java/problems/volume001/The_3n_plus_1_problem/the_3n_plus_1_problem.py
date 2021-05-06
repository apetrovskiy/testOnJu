def calculate_cycle_length(number: int) -> int:
    result = []
    while number > 1:
        if number % 2 == 1:
            number = number * 3 + 1
            result.append(number)
        else:
            number /= 2
            result.append(number)
    result.append(number)
    print(result)
    return len(result)


def the_3n_plus_1_problem(i: int, j: int) -> int:
    begin = i if i < j else j
    end = j if i < j else i
    return max([calculate_cycle_length(x) for x in range(begin, end)])
