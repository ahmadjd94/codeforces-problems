from collections import OrderedDict
import re


hello = re.sub("h{1,}e{1}l{2,}o{1,}","hello",input())
print(hello)

keys = OrderedDict({"h":0,"e":1,"$":2,"o":3})

target_keys = [i for i in keys.keys()]

#
for i in range(len(target_keys)):
    for r in range(len(hello)):
        if target_keys[i] == hello[r]:
            keys[hello[r]] = r
        else:
            continue

print(keys)


