""""
Dictionaries contain key-value pairs. Keys are like a list's indexes.
Dictionaries are mutable. Variables hold references to dictionary values, not the dictionary value itself.
Dictionaries are unordered. There is no "first" key-value pair in a dictionary.
The keys(), values(), and items() methods will return list-like values of a dictionary's keys, vaues, and both keys and values, respectively.
The get() method can return a default value if a key doesn't exist. eggs.get('key', 'retun if the key doesn't exist')
The setdefault() method can set a value if a key doesn't exist.
The pprint module's pprint() "pretty print" function can display a dictionary value cleanly. The pformat() function returns a string value of this output.
"""


import requests
import pprint
url = 'https://automatetheboringstuff.com/files/rj.txt'
r = requests.get(url, allow_redirects=True)
with open('rj.txt', 'wt') as rj:
    rj.write(r.content)
    rj.close()


with open('rj.txt', 'rt') as rj:
    message = rj.read()
    rj.close()
#message = r.content

count = {}

for char in message.lower():
    count.setdefault(char, 0)
    count[char] += 1


print(pprint.pformat(count))

