

class Register{
    constructor(funds){
        this.funds = funds;

        this.divideFunds()
    }

    divideFunds(){
        this.dividedFunds = {
            //Round all the values to integers, make sure they are divided correctly, change them to be a dict conatining a divisor number and the floored and divided one

            "PENNY": { 
                value: 0.01,
                available: Math.floor(this.funds[0][1] / 0.01)
            },
            "NICKEL": {
                value: 0.05,
                available: Math.floor(this.funds[1][1] / 0.05),
            },
            "DIME": {
                value: 0.1,
                available: Math.floor(this.funds[2][1] / 0.1)
            },
            "QUARTER": { 
                value: 0.25,
                available: Math.floor(this.funds[3][1] / 0.25),
            },

            "ONE": {
                value: 1,
                available: Math.floor(this.funds[4][1] / 1)
            },

            "FIVE": {
                value: 5,
                available: Math.floor(this.funds[5][1] / 5)
            },
            "TEN": {
                value:10, 
                available: Math.floor(this.funds[6][1] / 10)
            },
            "TWENTY": { 
                value:20, 
                available: Math.floor(this.funds[7][1] / 20) 
            } ,
            "ONE HUNDRED": {
                value:100, 
                available:Math.floor(this.funds[8][1] / 100)
            }
        }
    }

    calcGetTotalFunds(funds=this.funds){
        var total = 0
        for (var f of funds){
            total += f[1]
        }
        return total
    }

    giveOutChangeInKey(key, change){
        var obj = [key]
        var changeTemp = 0 
        var thisFunds = this.dividedFunds[key];

        var thisFundsAvailableTotal = thisFunds.available * thisFunds.value;

        if (change > thisFundsAvailableTotal){
            return [[key, thisFundsAvailableTotal], change-thisFundsAvailableTotal]
        } else {
            if(change > thisFunds.value){
                console.log("fifjifjoifj")
            }
            return [[0,0], 0]
        }

    }

    calcChange(price, cash){
        var change = cash - price
        var changeToReturn = []

        console.log(change)

        var totalChangeCollected = 0
        var totalFundsInReg = this.calcGetTotalFunds(this.funds)

        if(totalFundsInReg < change){
            return {status: "INSUFFICIENT_FUNDS", change: []}
        }

        for(var k of Object.keys(this.dividedFunds).reverse()){
            var _thisAvailableTotalFunds = this.dividedFunds[k].available * this.dividedFunds[k].value;
            
            if(totalChangeCollected >= change){
                console.log(19)
                break
            }

            var thisKeyVal = this.giveOutChangeInKey(k, change)
            console.log(change, "aoaoidjfoij")
            change -= thisKeyVal[1]
            console.log(change, "kfpofkopfk")

            changeToReturn.push(thisKeyVal[0])
            totalChangeCollected += thisKeyVal[0][1]

            //console.log(k, this.giveOutChangeInKey(k, change))
        }

        console.log(changeToReturn, "ofoi")
        changeToReturn =  this.removeZeros(changeToReturn)
        
        if(totalChangeCollected == totalFundsInReg){
            return {status: "CLOSED", change: changeToReturn}
        } 

        return {status: "OPEN", change: changeToReturn} 
    }

    removeZeros(change){
        var toRet = change.filter(x => x[1]!=0)
        
        return toRet
    }
}


function checkCashRegister(price, cash, cid) {
    var reg = new Register(cid);

    console.log(reg)

    let change = reg.calcChange(price, cash);

    console.log(change)
    return change;
  }
  
checkCashRegister(3.26, 100, [["PENNY", 1.01], ["NICKEL", 2.05], ["DIME", 3.1], ["QUARTER", 4.25], ["ONE", 90], ["FIVE", 55], ["TEN", 20], ["TWENTY", 60], ["ONE HUNDRED", 100]])
//checkCashRegister(19.5, 20, [["PENNY", 1.01], ["NICKEL", 2.05], ["DIME", 3.1], ["QUARTER", 4.25], ["ONE", 90], ["FIVE", 55], ["TEN", 20], ["TWENTY", 60], ["ONE HUNDRED", 100]]);