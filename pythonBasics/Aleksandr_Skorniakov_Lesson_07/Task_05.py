from json import dump
import os

folder = 'data'
threshold = [0, 10 ** 2, 10 ** 3, 10 ** 4, 10 ** 5]
result = {}


def folder_data(curr_threshold, next_threshold):
    ext = [file.name.rsplit('.')[-1] for file in os.scandir(folder)
           if curr_threshold < file.stat().st_size < next_threshold]
    result.setdefault(next_threshold, (len(ext), list(dict.fromkeys(ext))))


if __name__ == '__main__':
    for i in range(len(threshold) - 1):
        folder_data(threshold[i], threshold[i + 1])

    with open(r'data\summary.json', 'w', encoding='utf-8') as f:
        dump(result, f, indent=4, ensure_ascii=False)
        f.write('\n')
