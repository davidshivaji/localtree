import os

import re

# test
os.chdir("/Users/shivaji/projects/crequests/requests")

# TODO: handle nested folders.

# [i for i in os.listdir() if not i.endswith(".py")]

modules = [item[:-3] for item in os.listdir('.') if item.endswith(".py")]
tree = dict.fromkeys(modules, [])

tree



linecount = 0

for module in modules:
    with open(module + '.py', "r") as file:

        text = file.read()

        # might as well count lines
        for line in text.split('\n'):
            linecount += 1
        # account for: from . import sessions
        # y = re.search("(from\s)\.(.+)")
        # matching the dot.
        # if something has no group 1, it's not a local import.
            z = re.search("(from\s)(\.\s|\.[^\s]+)*(.*)(import)\s([^\s]+)", line)
            # print(text)
            if z:
                # print(z.groups()[1])
                if z.groups()[1]:
                    if z.groups()[1] == ". ":
                        mod = z.groups()[4]
                    else:
                        mod = z.groups()[1][1:]

                    # print(mod)
        tree[module].append(mod)
                    print(z.groups())
                # take the second group and check in modules
        # tree[module].append(8)
            # if line.startswith('from') or line.startswith('import'):
                # print(line)



print(tree)

print(linecount)


        # for line in file,
    # if there's a dot,
        # module = after that dot until a space
        # if module in files
