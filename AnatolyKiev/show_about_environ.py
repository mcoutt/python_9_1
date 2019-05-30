import os

# print(list(os.environ.keys()))

print("\n\tShow os.environ['PWD']")
print("\t-->", os.environ['PWD'])

print("\n\tShow os.environ['SHELL']")
print("\t-->", os.environ['SHELL'])

path_str = os.environ['PATH']
# /home/anatoly/.local/bin::/home/anatoly/.local/bin:/home/anatoly/.local/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games
path_list = path_str.split(os.pathsep)
# os.pathsep = ":" / ";"
print("\n\tShow os.environ['PATH']")
for item in path_list:
    print("\t ->", item)

print("")
