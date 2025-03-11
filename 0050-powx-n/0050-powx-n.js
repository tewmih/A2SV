/**
 * @param {number} x
 * @param {number} n
 * @return {number}
 */
var myPow = function(x, n) {
    let product=1;
    if(n<0){
        x=1/x;
        n=-n;
    }
    while(n>0){
        if(n%2==1){
            product*=x;
        }
        x*=x;
        n=Math.floor(n/2);
    }
  return product;
};