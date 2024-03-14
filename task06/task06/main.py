from typing import List

class Solution:
    def sampleStats(self, count: List[int]) -> List[float]:
        n = len(count)

        maximum = float('-inf')
        minimum = float('inf')
        mode = 0
        s = 0
        total = 0
        for i in range(n):
            if count[i] != 0:
                # mode
                if count[i] > count[mode]:
                    mode = i

                # Max/min
                maximum = max(maximum, i)
                minimum = min(minimum, i)

                # sum
                s += count[i] * i
                total += count[i]

        # average
        mean = s / total

        # median
        median_count = total // 2
        count_so_far = 0
        median = 0
        if total % 2 == 0:
            first_middle = None
            second_middle = None
            for i in range(n):
                count_so_far += count[i]
                if count_so_far >= median_count:
                    if first_middle is None:
                        first_middle = i
                    if count_so_far > median_count:
                        second_middle = i
                        break
            median = (first_middle + second_middle) / 2
        else:
            for i in range(n):
                count_so_far += count[i]
                if count_so_far > median_count:
                    median = i
                    break

        return [minimum, maximum, mean, median, mode]

