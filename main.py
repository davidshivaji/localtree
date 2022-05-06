import os
import json
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
            z = re.search("(from\s)(\.\s|\.[^\s]+)*(.*)(import)\s([^\s]+)", line)
            # if the line has a match
            if z:
                # if something has no group 1, it's not a local import.
                if z.groups()[1]:
                    if z.groups()[1] == ". ":
                        mod = z.groups()[4]
                    else:
                        mod = z.groups()[1][1:]

                    dependencies.append(mod)

        tree[module] = list(set(dependencies))


print(json.dumps(tree))
# for item, value in tree.items():
#     print(item, value)

print(linecount)

# now with that tree:

# what is the data structure?
# it's a fuckin tree.

# which ones contain cookies.

def whatuses(module):
    # which modules use
    return [key for key, value in tree.items() if module in value]

whatuses("sessions")
