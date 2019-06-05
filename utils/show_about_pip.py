"""

Cмотрим путь к интерпретатору и список site.getsitepackages .

"""

import sys
import os
import site

print("\n\tКоротко о главном\n")
print("\t1. Путь к интерпретатору Python (Версия {}):".format(sys.version[:5]))
print("\t -> {}\n".format(sys.executable))

print("\t2. Смотрим site.getsitepackages\n")
# site.getsitepackages()
# ['/usr/local/lib/python2.7/dist-packages', '/usr/lib/python2...]
for item_list in site.getsitepackages():
    if os.path.isdir(item_list):
        dir_info = (len(os.listdir(item_list)))
    else:
        dir_info = 0

    print("\t -> {0} [{1}]".format(item_list, dir_info))
    if len(sys.argv) > 1 and sys.argv[1] == "list":
        for root, dirs, files in os.walk(item_list):
            temp = dirs + files
            for i in sorted(temp):
                print("\t .. {0}/{1}".format(item_list, i))
            print()
            break
print("\n")
