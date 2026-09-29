class Solution:
    def reconstructQueue(self, people: list[list[int]]) -> list[list[int]]:
        
        people.sort(key=lambda x: (-x[0], x[1]))

        stack = []

        for x in people:
            stack.insert(x[1], x)

        return stack