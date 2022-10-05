import os, time
from math import floor, log, pow

s = time.time()

def get_size(root):
    size = 0
    for path, _ , files in os.walk(root):
        for f in files:
            fp = os.path.join(path, f)
            size += os.path.getsize(fp)
    return size


def convert_size(size_bytes):
    if size_bytes == 0:
        return "0B"
    size_name = "B", "KB", "MB", "GB", "TB"
    i = int(floor(log(size_bytes, 1024)))
    p = pow(1024, i)
    s = round(size_bytes / p, 2)
    return f"{s} {size_name[i]}"


def del_dir(path):
    for root, _ , files in os.walk(path):
        for file in files:
            os.remove(os.path.join(root, file))

list_of_cache = []

prev = "    "

total = 0

for (root, dirs, files) in os.walk('C:/Users/ricchfrvr', topdown=True):
    if 'cache' in root and prev not in root:
        prev = root
        root = root.replace(os.path.sep, '/')
        list_of_cache.append((root, convert_size(get_size(root)), get_size(root)))
        total += get_size(root)
        # del_dir(root)


e = time.time()

from operator import itemgetter
from tabulate import tabulate
# print(tabulate(sorted(list_of_cache, key=itemgetter(2))))
# print('total', convert_size(total))
# print(e-s)

# TODO: 'node_modules' not in root