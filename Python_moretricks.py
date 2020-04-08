# FP - CASE STUDY
# Q: LONELY INTEGER

"""


def lonely_int(list):

    uniqueList = []
    # uniqueList = (x for x in list if x not in uniqueList)
    for i in list:
        if i not in uniqueList:
            uniqueList.append(i)
    # print(uniqueList)
    # return uniqueList

    lonelyList = []
    for i in uniqueList:
        count = 0
        for j in list:

            if i == j:
                count += 1
                # print(i, j, count)
        if count == 1:
            lonelyList.append(i)
        else:
            pass
    return lonelyList


list1 = [1,1,5,4,3,3,5,6,7,2,7,6,2]
uniqueList1 = lonely_int(list1)
print(uniqueList1)
"""


# EFFICIENT PYTHON CODING

# 1. LOOPING OVER A RANGE
import argparse
import os

"""
for i in [0, 1, 2, 3, 4, 5]:
    print(i**2)

for i in range(6):
    print(i**2)
"""

# LOOPING OVER A COLLECTION

colors = ['red', 'green', 'blue', 'yellow']
"""

for i in range(len(colors)):
    print(colors[i], end='n, ')

for color in colors:
    print(color)
"""

# LOOPING BACKWARDS

"""
for i in range(len(colors)-1, -1, -1):
    print(colors[i])

for i in reversed(colors):
    print(i)
"""

# LOOPING OVER A COLLECTION AND INDICIES:
"""
for i in range(len(colors)):
    print(i, '--->', colors[i])

for i, color in enumerate(colors):
    print(i, '--->', colors[i])
"""

# LOOPING OVER TWO COLLECTIONS:

names = ['raymond', 'rachel', 'matthews']

"""
n = min(len(names), len(colors))
for i in range(n):
    print(names[i], '--->', colors[i])

for name, color in zip(names, colors):
    print(name, '--->', color)
"""

# "izip" IS NOT WORKING FOR MR


# LOOPING IN SORTED ORDER
"""
for color in sorted(colors):
    print(color)

for color in sorted(colors, reverse=True):
    print(color)
"""


# CUSTOM SORT ORDER:
"""
def compare_length(c1, c2):
    if len(c1) < len(c2): return -1
    if len(c2) > len(c2): return 1
    return 0

print(sorted(colors, cmp=compare_length))

print(sorted(colors, key=len))
"""

# CALL A FUNCTION UNTIL A SENTINEL VALUE
"""
blocks = []
for block in iter(partial(f.read, 32), ''):
    blocks.append(block)
"""

# DISTINGUISHING MULTIPLE EXIT POINTS IN LOOP:
"""
def find(seq, target):
    found = False
    for i, value in enumerate(seq):
        if value == tgt:
            found = True
            break
        if not found:
            return -1
        return i


def find2(seq, target):

    for i, value in enumerate(seq):
        if value == tgt:
            break
    else:
        return -1
    return i
"""

# looping over dictionary keys:

d = {'raymond': 'red', 'rachel': 'green', 'matthews': 'blue'}

"""
for j in d:
    print(j)

for k in d.keys():
    if k.startswith('r'):
        del d[k]            #RuntimeError: dictionary changed size during iteration
print(d)

d = {k: d[k] for k in d if not k.startswith('r')}
print(d)
"""


# looping over dictionary keys and values:

"""
for k in d:
    print(k, '-->', d[k])

for k, v in d.items():
    print(k, '-->', v)

for k, v in d.iteritems():      #AttributeError: 'dict' object has no attribute 'iteritems'
    print(k, '-->', v)
"""

# Construct A DICTIONARY:
"""
dd = dict(zip(names, colors))
print(dd)

d = dict(enumerate(names))
print(d)

# O/P: {'raymond': 'red', 'rachel': 'green', 'matthews': 'blue'}
"""
import collections
from collections import defaultdict
# COUNTING WITH DICTIONARIES:

"""
d = {}
for color in colors:
    if color not in d:
        d[color] = 0
    d[color] += 1
print(d)


d = {}
for color in colors:
    d[color] = d.get(color, 0) + 1
print(d)


d = defaultdict(int)
for color in colors:
    d[color] += 1
print(d)
"""

# GROUPING WITH DICTIONARIES:

names = ['raymond', 'rachel', 'matthew', 'roger', 'betty', 'melissa',
         'judith', 'charlie']

"""

d={}
for name in names:
    key = len(name)
    if key not in d:
        d[key] = []
    d[key].append(name)
# print(d)


d={}
for name in names:
    key = len(name)
    d.setdefault(key, []).append(name)
# print(d)


d = defaultdict(list)
for name in names:
    key = len(name)
    d[key].append(name)
    print(d)

"""

# IS A DICTIONARY POPITEM() ATOMIC?
'''
d1 = {}
while d:
    key, value = d.popitem()
    print(key, '-->', value)
print(d, d1)
'''

# LINKING DICTIONARIES:
'''
from collections import ChainMap

defaults = {'color': 'red', 'user': 'guest'}
parser = argparse.ArgumentParser()
parser.add_argument('-u', '--users')
parser.add_argument('-c', '--color')
namespace = parser.parse_args([])
command_line_args = {k: v for k, v in vars(namespace).items() if v}
# print(parser, '\n',  namespace, '\n', command_line_args)
'''

'''
d = defaults.copy()
# print(d)
d.update(os.environ)
# print(d)
d.update(command_line_args)
# print(d)
d = ChainMap(command_line_args, os.environ, defaults)
print(d)
'''

# CONCATENATING STRINGS:
'''
s = names[0]
for name in names[1:]:
    s += ',' + name
print(s)


print(','.join(names))
'''

# UPDATING SEQUENCES:

'''
from collections import deque

names = ['raymond', 'rachel', 'matthew', 'roger', 'betty', 'melissa', 'judith', 'charlie']

del names[0]
names.pop(0)
names.insert(0, 'mark')

names = deque(['raymond', 'rachel', 'matthew', 'roger', 'betty', 'melissa', 'judith', 'charlie'])


del names[0]
print(names)
names.popleft()
print(names)
names.appendleft('mark')
print(names)
'''


# USING DECORATORS TO FACTOR-OUT ADMINISTRATIVE LOGIC:
'''
import urllib
from pip._internal import cache

def web_lookup(url, saved={}):
    if url in saved:
        return saved[url]
    page = urllib.urlopen(url).read()
    saved[url] = page

@cache
def web_look(url):                    #TypeError: 'module' object is not callable
    return urllib.urlopen(url).read()
'''

# HOW TO OPEN AND CLOSE FILES:
'''
f = open('D:\Python projects\PyQT.py')
try:
    data = f.read()
finally:
    f.close()

with open('D:\Python projects\PyQT.py') as f:
    data = f.read()
'''

# LIST COMREHENSION AND GENERATOR EXPRESSION:
'''
result = []
for i in range(10):
    s = i**2
    result.append(s)
print(sum(result))


print(sum([i**2 for i in range(10)]))


print(sum(i**2 for i in range(10)))
'''
