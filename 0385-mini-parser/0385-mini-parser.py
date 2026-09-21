# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def __init__(self, value=None):
#        """
#        If value is not specified, initializes an empty list.
#        Otherwise initializes a single integer equal to value.
#        """
#
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def add(self, elem):
#        """
#        Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
#        :rtype void
#        """
#
#    def setInteger(self, value):
#        """
#        Set this NestedInteger to hold a single integer equal to value.
#        :rtype void
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        The result is undefined if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        The result is undefined if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """

class Solution:
    def deserialize(self, s: str) -> NestedInteger:


        if s[0] != '[':
            return NestedInteger(int(s))

        stack = []
        i = 0

        while i < len(s):

            if s[i] == '[':
                stack.append(NestedInteger())
                i += 1

            elif s[i] == ']':
                current = stack.pop()

                if stack:
                    stack[-1].add(current)
                else:
                    return current

                i += 1

            elif s[i] == ',':
                i += 1

            else:
                sign = 1

                if s[i] == '-':
                    sign = -1
                    i += 1

                num = 0

                while i < len(s) and s[i].isdigit():
                    num = num * 10 + int(s[i])
                    i += 1

                stack[-1].add(NestedInteger(sign * num))