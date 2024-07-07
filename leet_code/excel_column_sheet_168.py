class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        dictionary = {i: chr(i + 64) for i in range(1, 27)}

        result = []
        while columnNumber:
            n = columnNumber % 26
            if n == 0:
                n = 26
            result.append(dictionary[n])
            columnNumber = columnNumber // 26
            if dictionary[n] == 'Z' and columnNumber == 1:
                break
        result.reverse()
        r = ''.join(result)
        return r

class SolutionBest:
    def convertToTitle(self, columnNumber: int) -> str:
        x=""
        while columnNumber > 0:
            x=chr(65+(columnNumber-1)%26) + x
            columnNumber = (columnNumber-1) // 26
        return x


def add(b):
    if b == 3:
        return b
    if b != 3:
        b += 1
        return add(b)





if __name__ == '__main__':
    # c = SolutionBest()
    # print(c.convertToTitle(2147483647))
    print(add(-100))

