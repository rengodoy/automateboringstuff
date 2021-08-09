"""
A list is a value that contains multiple values: [42, 3.14, ‘hello']
The values in a list are also called items.
You can access items in a list with its integer index.
The indexes start at 0, not 1.
You can also use negative indexes: -1 refers to the last item, -2 refers to the second to last item, and so on.
You can get multiple items from the list using a slice.
The slice has two indexes. The new list's items start at the first index and go up to, but doesn't include, the second index.
The len() function, concatenation, and replication work the same way on lists that they do with strings.
You can convert a value into a list by passing it to the list() function.

A for loop technically iterates over the values in a list.
The range() function returns a list-like value, which can be passed to the list() function if you need an actual list value.
Variables can swap their values using multiple assignment: a, b = b, a
Augmented assignment operators like += are used as shortcuts.

Methods are functions that are "called on" values.
The index() list method returns the index of an item in the list.
The append() list method adds a value to the end of a list.
The insert() list method adds a value anywhere inside a list.
The remove() list method removes an item, specified by the value, from a list.
The sort() list method sorts the items in a list.
The sort() method's reverse=True keyword argument can make the sort() method sort in reverse order.
These list methods operate on the list "in place", rather than returning a new list value.

Strings can do a lot of the same things lists can do, but strings are immutable.
Immutable values like strings and tuples cannot be modified "in place".
Mutable values like lists can be modified in place.
Variables don't contain lists, they contain references to lists.
When passing a list argument to a function, you are actually passing a list reference.
Changes made to a list in a function will affect the list outside the function.
The \ line continuation character can be used to stretch Python instruction across multiple lines.



copy.copy vs copy.deepcopy
>>> import copy
>>> b = copy.copy(bacon)
>>> b.append('a')
>>> b
[3.14, 11, 'cat', True, 99, 'a']
>>> bacon
[3.14, 11, 'cat', True, 99]
>>> bacon.append([2,3,4])
>>> bacon
[3.14, 11, 'cat', True, 99, [2, 3, 4]]
>>> b = copy.copy(bacon)
>>> b.append('a')
>>> b
[3.14, 11, 'cat', True, 99, [2, 3, 4], 'a']
>>> bacon
[3.14, 11, 'cat', True, 99, [2, 3, 4]]
>>> bacon[5].append(99)
>>> bacon
[3.14, 11, 'cat', True, 99, [2, 3, 4, 99]]
>>> b
[3.14, 11, 'cat', True, 99, [2, 3, 4, 99], 'a']
>>> b = copy.deepcopy(bacon)
>>> b
[3.14, 11, 'cat', True, 99, [2, 3, 4, 99]]
>>> bacon[5].append(3)
>>> bacon
[3.14, 11, 'cat', True, 99, [2, 3, 4, 99, 3]]
>>> b
[3.14, 11, 'cat', True, 99, [2, 3, 4, 99]]


"""

import copy

def eggs(cheese, milk):
    cheese.append('Hello')
    milk += milk
 
 

spam = [1, 2, 3, 5]
spam2 = copy.deepcopy(spam)
bread = 5
eggs(spam, bread)
print(spam)
print(bread)
eggs(spam, bread)
print(spam)
print(bread)
print(spam2)
eggs(spam2, 1)
print(spam2)