

class Register {
    constructor(funds) {
        this.funds = funds

        this.occurencyTypes = ['ONE HUNDRED', 'TWENTY', 'TEN', 'FIVE', 'ONE', 'QUARTER', 'DIME', 'NICKEL','PENNY']

        this.currenciesAndValues = [
            [ 'ONE HUNDRED', 100.00],
            [ 'TWENTY', 20.00],
            [ 'TEN',    10.00],
            [ 'FIVE',   5.00 ],
            [ 'ONE',   1.00],
            [  'QUARTER',0.25],
            [  'DIME',  0.10],
            [ 'NICKEL',  0.05],
            [ 'PENNY', 0.01]
          ];

        var _y = this.transformRegBal()
        this.fundsDict = _y[0]
        this.totalBalance = _y[1]
    }

    transformRegBal(){
        var thisTotal = 0
        var objToReturn = {

        }

        for(var x of this.funds){
            objToReturn[x[0]] = x[1]
            thisTotal += x[1]
        }

        return [objToReturn, thisTotal]
    }

    calcChange(price, cash){
        var change = cash - price

        if(change > this.totalBalance){
            return {
                status: "INSUFFICIENT_FUNDS", change: []
            }
        } else if(change == this.totalBalance){
            return {
                status: "CLOSED", change: this.funds
            }
        }

        


    }

}
  
  function checkCashRegister(price, cash, cid) {
    var myReg = new Register(cid)

    return myReg.calcChange(price, cash)

    var change = cash - price;
  
    // Transform CID array into drawer object
    
    console.log(register, "fokfok")
  
    // Handle exact change
    if (register.total === change) {
      return 'Closed';
    }
  
    // Handle obvious insufficent funds
    if (register.total < change) {
      return 'Insufficient Funds';
    }
  
    // Loop through the denomination array
    var change_arr = occurencyTypes.reduce(function(acc, curr) {
      var value = 0;
      // While there is still money of this type in the drawer
      // And while the denomination is larger than the change reminaing
      while (register[curr.name] > 0 && change >= curr.val) {
        change -= curr.val;
        register[curr.name] -= curr.val;
        value += curr.val;
  
        // Round change to the nearest hundreth deals with precision errors
        change = Math.round(change * 100) / 100;
      }
      // Add this denomination to the output only if any was used.
      if (value > 0) {
          acc.push([ curr.name, value ]);
      }
      return acc; // Return the current Change Array
    }, []); // Initial value of empty array for reduce
  
    // If there are no elements in change_arr or we have leftover change, return
    // the string "Insufficient Funds"
    if (change_arr.length < 1 || change > 0) {
      return "Insufficient Funds";
    }
  
    // Here is your change, ma'am.
    console.log(change_arr)
    return change_arr;
  }

  checkCashRegister(3.26, 100, [["PENNY", 1.01], ["NICKEL", 2.05], ["DIME", 3.1], ["QUARTER", 4.25], ["ONE", 90], ["FIVE", 55], ["TEN", 20], ["TWENTY", 60], ["ONE HUNDRED", 100]])