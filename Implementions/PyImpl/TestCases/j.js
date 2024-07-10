



class ZigZag{
    constructor(rows = []){
        this.rows = rows

        this.difference = 1
        this.currentRowInd = 0
    }

    addToRow(ch){
        this.rowsLength = len(this.rows)

        if ( (this.currentRowInd + this.difference) > this.rowsLength ){
            this.currentRowInd = this.rowsLength - 2
            this.difference *= -1
        } else if ( (this.currentRowInd + this.difference) < 0 ){
            this.currentRowInd = 0
            this.difference *= -1
        }
        
        thisCurrentRowObj = this.rows[this.currentRowInd]
        
        thisCurrentRowObj.addChar(ch)
        
        this.currentRowInd += this.difference
    
    }
}

class Row{
    constructor(){
        this.content = []
    }
    
    getAsString(){
        _contentString = this.contents.join()
        return _contentString
    }

    addChar(ch){
        this.content.append(ch)
    }
}


class _Solution{
    convert(s, numRows){
        thisZigZag = new ZigZag()
    
        for (let _=0; _<numRows.length; _++){
            r = new Row()
            thisZigZag.rows.push(r)
        }

        for (char of s){
            thisZigZag.addToRow(char)
        }
        
        res = ""
        
        for (row of thisZigZag.rows){
            res += row.getAsString()
        }

        return res
    }
}


class Solution{
    convert(s, numRows){
        sol = _Solution()
        
        res = sol.convert(s, numRows)
        return res
    }
}

// class Solution:
//     def convert(self, s: str, numRows: int):
//         sol = _Solution()
        
//         res = sol.convert(s, numRows)
//         return res

// class ZigZag:
//     def __init__(self, rows=[]):
//         self.rows = rows

//         self.difference = 1

//         self.currentRowInd = 0

//     def addToRow(self, ch):
//         self.rowsLength = len(self.rows)


//         if (self.currentRowInd + self.difference) > self.rowsLength:
//             self.currentRowInd = self.rowsLength - 2
//             self.difference *= -1

//         elif (self.currentRowInd + self.difference) < 0:
//             self.currentRowInd = 0
//             self.difference *= -1

//         self.thisCurrentRowObj = self.rows[self.currentRowInd]

//         self.thisCurrentRowObj.addChar(ch)

//         self.currentRowInd += self.difference
                
// class Row:
//     def __init__(self):
//         self.content = []

//     def getAsString(self):
//         _contentString = "".join(x for x in self.content)
//         return _contentString

//     def addChar(self, ch):
//         self.content.append(ch)
                

// class _Solution:
    
//     def convert(self, s: str, numRows: int):

//         thisZigZag = ZigZag()
    
//         for _ in range(numRows):
//             r = Row()
//             thisZigZag.rows.append(r)

        
//         for char in s:
//             # print(list(len(x.content) for x in thisZigZag.rows), "-")
//             thisZigZag.addToRow(char)
//             # print(list(len(x.content) for x in thisZigZag.rows), "--")
        
//         res = "".join(row.getAsString() for row in thisZigZag.rows)

//         return res
    
    
// class Solution:
//     def convert(self, s: str, numRows: int):
//         sol = _Solution()
        
//         res = sol.convert(s, numRows)
//         return res