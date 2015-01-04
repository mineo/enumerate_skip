#!/usr/bin/env python
# coding: utf-8
# Copyright (c) 2014 Wieland Hoffmann
# License: MIT, see LICENSE for details
__all__ = ["enumerate_manual", "enumerate_skip"]


class enumerate_adjust(object):
    def __init__(self, iterable, start=0):
        self.iterable = iterable
        self.shift = 0
        self.adjustment = None
        self.start = start

    def _adjust(self):
        self.shift += self.adjustment


class enumerate_skip(enumerate_adjust):
    """
    This class provides an enumerate-like interface that makes it possible to
    not increment the index after an (index, value) pair has been yielded. This
    can be useful when iterating over an iterable in a for-loop when not all
    values of the iterable are actually interesting.

    >>> from __future__ import division
    >>> it = enumerate_skip(range(10))
    >>> for index, obj in it:
    ...     print("{0}, {1}".format(index, obj))
    ...     if index > 5:
    ...         it.skip()
    0, 0
    1, 1
    2, 2
    3, 3
    4, 4
    5, 5
    6, 6
    6, 7
    6, 8
    6, 9
    """
    def __init__(self, *args, **kwargs):
        super(enumerate_skip, self).__init__(*args, **kwargs)
        self.adjustment = -1

    def __iter__(self):
        for index, obj in enumerate(self.iterable, self.start):
            yield index + self.shift, obj

    def skip(self):
        """
        Skip incrementing the index before yielding it together with the next
        value of the iterable.
        """
        self._adjust()


class enumerate_manual(enumerate_adjust):
    """
    This class provides an enumerate-like interface that makes it possible to
    only increment the index manually after an (index, value) pair has been
    yielded. This can be useful when iterating over an iterable in a for-loop
    when not all values of the iterable are actually interesting.

    >>> from __future__ import division
    >>> it = enumerate_manual(range(10))
    >>> for index, obj in it:
    ...     print("{0}, {1}".format(index, obj))
    ...     if obj >= 5:
    ...         it.advance()
    0, 0
    0, 1
    0, 2
    0, 3
    0, 4
    0, 5
    1, 6
    2, 7
    3, 8
    4, 9
    """
    def __init__(self, *args, **kwargs):
        super(enumerate_manual, self).__init__(*args, **kwargs)
        self.adjustment = 1

    def __iter__(self):
        index = self.start
        for obj in self.iterable:
            yield index + self.shift, obj

    def advance(self):
        """
        Increment the index that will be yielded together with the next value of
        the iterable.
        """
        self._adjust()
