#!/usr/bin/env python
# coding: utf-8
# @File Name: iterator_protocol.py
# @Author: Joshua Liu
# @Email: liuchaozhen@neusoft.com
# @Create Date: 2016-01-27 15:01:21
# @Last Modified: 2016-01-27 16:01:18
# @Description:
'''
    Problem: Building custom objects on which you would like to support iteration, but would like an easy way to implement the iterator protocol.

    Solution: Example
'''

class Node:
    def __init__(self, value):
        self._value = value
        self._children = []
    def __repr__(self):
        return 'Node({!r})'.format(self._value)
    def add_child(self, node):
        self._children.append(node)
    def __iter__(self):
        return iter(self._children)
    def depth_first(self):
        yield self
        for c in self:
            yield from c.depth_first()

if __name__ == '__main__':
    root = Node(0)
    child_1 = Node(1)
    child_2 = Node(2)
    root.add_child(child_1)
    root.add_child(child_2)
    child_1.add_child(Node(3))
    child_1.add_child(Node(4))
    child_2.add_child(Node(5))
    for ch in root.depth_first():
        print(ch)

'''
Outputs:
    Node(0)
    Node(1)
    Node(3)
    Node(4)
    Node(2)
    Node(5)

Now, see how `yield` works.

    Discussion:

    Python's iterator protocol requires __iter__() to return a special iterator object that implements a __next__() operation and uses a StopIteration exception to signal completion. However, implementing such objects can often be a messy affair. For example:
'''

class Node2:
    def __init__(self, value):
        self._value = value
        self._children = []
    def __repr__(self):
        return 'Node({!r})'.format(self._value)
    def add_child(self, other_node):
        self._children.append(other_node)
    def __iter__(self):
        return iter(self._children)
    def depth_first(self):
        return DepthFirstIterator(self)

class DepthFirstIterator(object):
    # depth-first traversal
    def __init__(self, start_node):
        self._node = start_node
        self._children_iter = None
        self._child_iter = None
    def __iter__(self):
        return self
    def __next__(self):
        # Return myself if just started; create an iterator for children
        if self._children_iter is None:
            self._children_iter = iter(self._node)
            return self._node

        # If processing a child, return its next item
        elif self._child_iter:
            try:
                nextchild = next(self._child_iter)
                return nextchild
            except StopIteration:
                self._child_iter = None
                return next(self)
        # Advance to the next child and start its iteration
        else:
            self._child_iter = next(self._children_iter).depth_first()
            return next(self)

'''
See the DepthFirstIterator class works in the same way as the generator version, but it's a mess because the iterator has to maintain a lot of complex state about where it is in the iteration process.

Frankly, nobody likes to write mind-bending code like that. Define your iterator as a generator and be done with it.
'''
root = Node2(0)
child_1 = Node2(1)
child_2 = Node2(2)
root.add_child(child_1)
root.add_child(child_2)
child_1.add_child(Node2(3))
child_1.add_child(Node2(4))
child_2.add_child(Node2(5))
for ch in root.depth_first():
    print(ch)
