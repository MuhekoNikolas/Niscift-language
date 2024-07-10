


class ZigZag:
    def __init__(self, rows=[]):
        self.rows = rows

        self.difference = 1

        self.currentRowInd = 0

    def addToRow(self, ch):
        self.rowsLength = len(self.rows)


        if (self.currentRowInd + self.difference) > self.rowsLength:
            self.currentRowInd = self.rowsLength - 2
            self.difference *= -1

        elif (self.currentRowInd + self.difference) < 0:
            self.currentRowInd = 0
            self.difference *= -1

        self.thisCurrentRowObj = self.rows[self.currentRowInd]

        self.thisCurrentRowObj.addChar(ch)

        self.currentRowInd += self.difference
                
class Row:
    def __init__(self):
        self.content = []

    def getAsString(self):
        _contentString = "".join(x for x in self.content)
        return _contentString

    def addChar(self, ch):
        self.content.append(ch)
                

class Solution:
    
    def convert(self, s: str, numRows: int) -> str:

        thisZigZag = ZigZag()
    
        for _ in range(numRows):
            r = Row()
            thisZigZag.rows.append(r)

        
        for char in s:
            # print(list(len(x.content) for x in thisZigZag.rows), "-")
            thisZigZag.addToRow(char)
            # print(list(len(x.content) for x in thisZigZag.rows), "--")
        
        res = "".join(row.getAsString() for row in thisZigZag.rows)

        return res
    
    
sol = Solution()
res = sol.convert("A", 4)
print(res)