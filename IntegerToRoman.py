class Solution:
    
#     ADD/SUBSTITUTE OF 1
    ONES = ["","I","II","III","IV","V","VI","VII","VIII","IX"]
#     ADD/SUBSTITUTE OF 10
    TENS = ["","X","XX","XXX","XL","L","LX","LXX","LXXX","XC"]
#     ADD/SUBSTITUTE OF 100
    HUNS = ["","C","CC","CCC","CD","D","DC","DCC","DCCC","CM"]
#     ADD/SUBSTITUTE OF 1000
    THUS = ["","M","MM","MMM"]
    
    def intToRoman(self, num: int) -> str:
        th=(int)(num/1000)
        hun = (int)((num%1000)/100)
        ten = (int)((num%100)/10)
        ones = (int)(num%10)
        return self.THUS[th]+self.HUNS[hun]+self.TENS[ten]+self.ONES[ones]
        
        
