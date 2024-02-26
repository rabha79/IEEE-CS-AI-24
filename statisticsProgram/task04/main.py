def get_numbers():
    while True:
        try:
            numbers = list(map(int, input("enter numbers: ").split()))
            return numbers
        except ValueError:
            print("please enter valid numbers")


def find_min(numbers):
    if not numbers:
        return print("it is empty")
    min_num = numbers[0]
    for num in numbers:
        if num < min_num:
            min_num = num
    return min_num


def find_max(numbers):
    if not numbers:
        return print("it is empty")
    max_num = numbers[0]
    for num in numbers:
        if num > max_num:
            max_num = num
    return max_num


def find_mean(numbers):
    if not numbers:
        return print("it is empty")
    sum = 0
    for num in numbers:
        sum += num
    mean = sum / len(numbers)
    return mean


def find_mode(numbers):
    if not numbers:
        return print("it is empty")
    counts = {}
    for num in numbers:
        counts[num] = counts.get(num, 0) + 1
    max_count = max(counts.values(), default=1)  # If no counts, default to 1
    if max_count == 1 or len(counts) == len(numbers):  # If all numbers are unique
        return None
    else:
        mode = [num for num, count in counts.items() if count == max_count]
        return mode if len(mode) > 1 else mode[0]


def find_median(numbers):
    if not numbers:
        return print("it is empty")
    sort_numbers = sorted(numbers)
    length = len(sort_numbers)
    if length % 2 == 0:
        return (sort_numbers[length // 2 - 1] + sort_numbers[length // 2]) / 2
    else:
        return sort_numbers[length // 2]


def find_range(numbers):
    if not numbers:
        return print("it is empty")
    return find_max(numbers) - find_min(numbers)


def find_variance(numbers):
    if not numbers:
        return print("it is empty")
    mean = find_mean(numbers)
    sum = 0
    for x in numbers:
        diff = mean - x
        sum += diff ** 2
    variance = round(sum / len(numbers), 2)
    return variance


def find_STD(numbers):
    if not numbers:
        return print("it is empty")
    std = find_variance(numbers)
    return round((std ** 0.5), 5)


def find_Quariles(numbers):
    if not numbers:
        return print("it is empty")
    sort_numbers = sorted(numbers)
    length = len(sort_numbers)
    q1 = length // 4
    q2 = length // 2
    q3 = 3 * length // 4
    quartiles = (sort_numbers[q1], sort_numbers[q2], sort_numbers[q3])
    return quartiles


def find_IQR(numbers):
    if not numbers:
        return print("it is empty")
    q1, q2, q3 = find_Quariles(numbers)
    return q3 - q1


try:
    numbers = get_numbers()
    print("Min:", find_min(numbers))
    print("Max:", find_max(numbers))
    print("Mean:", find_mean(numbers))
    print("Mode:", [find_mode(numbers)])
    print("Median:", find_median(numbers))
    print("Range:", find_range(numbers))
    print("Variance:", find_variance(numbers))
    print("Standard Deviation:", find_STD(numbers))
    print("Quartiles:", find_Quariles(numbers))
    print("Interquartile Range(IQR):", find_IQR(numbers))
except ValueError as e:
    print(e)
