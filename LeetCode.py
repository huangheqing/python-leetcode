class LeetCode(object):
    a = 5

    def findComplement(self, num):
        i = 1
        while (i <= num):
            i = i << 1
        return (i - 1) ^ num

    def findWordsCanBeTypedUseSingleRowOfKeyboard(self, words):
        ret = []
        firstRow = ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p']
        secondRow = ['a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l']
        thirdRow = ['z', 'x', 'c', 'v', 'b', 'n', 'm']

        for word in words:
            if self.findInAList(word, firstRow):
                ret.append(word)
            if self.findInAList(word, secondRow):
                ret.append(word)
            if self.findInAList(word, thirdRow):
                ret.append(word)
        return ret

    def findInAList(self, word, keyBoardRow):
        isInSameRow = False
        for letter in word:
            if letter not in keyBoardRow and letter.lower() not in keyBoardRow:
                return False
            isInSameRow = True
        return isInSameRow

    def fizzBuzz412(self, n):
        ret = []
        for i in range(1, n + 1):
            if i % 3 == 0 and i % 5 == 0:
                ret.append("FizzBuzz")
            elif i % 3 == 0:
                ret.append("Fizz")
            elif i % 5 == 0:
                ret.append("Buzz")
            else:
                ret.append(str(i))
        return ret

    def reverseString344(self, s):
        return s[::-1]

    def islandPerimeter463(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        ret = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 0:
                    if i - 1 >= 0 and grid[i - 1][j] == 1:
                        ret += 1
                    if j - 1 >= 0 and grid[i][j - 1] == 1:
                        ret += 1
                    if j + 1 <= len(grid[i]) - 1 and grid[i][j + 1] == 1:
                        ret += 1
                    if i + 1 <= len(grid) - 1 and grid[i + 1][j] == 1:
                        ret += 1
                if grid[i][j] == 1 and i == 0:
                    ret += 1
                if grid[i][j] == 1 and j == 0:
                    ret += 1
                if grid[i][j] == 1 and j == (len(grid[i]) - 1):
                    ret += 1
                if grid[i][j] == 1 and i == (len(grid) - 1):
                    ret += 1
        return ret


a = LeetCode()
# print a.findWordsCanBeTypedUseSingleRowOfKeyboard(["Hello", "Alaska", "Dad", "Peace"])
print a.islandPerimeter463([[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]])
