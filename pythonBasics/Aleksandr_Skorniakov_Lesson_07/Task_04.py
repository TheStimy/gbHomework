import os

folder = 'data'
threshold = [0, 10 ** 2, 10 ** 3, 10 ** 4, 10 ** 5]
result = {}


def threshold_func(curr_threshold, next_threshold):
    result.setdefault(next_threshold, len([file for file in os.scandir(folder)
                                           if curr_threshold < file.stat().st_size < next_threshold]))


for i in range(len(threshold) - 1):
    threshold_func(threshold[i], threshold[i + 1])

print(result)
