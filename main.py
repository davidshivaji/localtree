import os

import re

# test
os.chdir("/Users/shivaji/projects/crequests/requests")

# TODO: handle nested folders.

# [i for i in os.listdir() if not i.endswith(".py")]

modules = [item[:-3] for item in os.listdir('.') if item.endswith(".py")]
tree = dict.fromkeys(modules, [])



linecount = 0

# for string in list
for module in modules:
    dependencies = []
    with open(module + '.py', "r") as file:

        text = file.read()
        # if module == "models":
        #     print(text)

        # might as well count lines
        for line in text.split('\n'):
            linecount += 1
        # account for: from . import sessions
        # y = re.search("(from\s)\.(.+)")
        # matching the dot.
        # if something has no group 1, it's not a local import.
            z = re.search("(from\s)(\.\s|\.[^\s]+)*(.*)(import)\s([^\s]+)", line)
        # print(text)
        # if there's a match in
            if z:
                # print(z.groups())
                if z.groups()[1]:
                    if z.groups()[1] == ". ":
                        mod = z.groups()[4]
                    else:
                        # mod = ".auth" (in the case of models.py)
                        mod = z.groups()[1][1:]
                        # mod = 0

                # print(mod)
                # should fucking well have models and auth
                    dependencies.append(mod)
        # print(module, dependencies)
        # tree[module].append(mod)
            # print('niet')
        tree[module] = list(set(dependencies))
                # it should only be going if it's in there.

        # tree[module].append(8)
            # if line.startswith('from') or line.startswith('import'):
                # print(line)



# print(tree)
print('\n')
for item, value in tree.items():
    print(item, value)

print(linecount)


        # for line in file,
    # if there's a dot,
        # module = after that dot until a space
        # if module in files
