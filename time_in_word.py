import num2words as n2w

# Complete the timeInWords function below.
def timeInWords(h, m):
    timeDict={
        15:"quarter",
        45:"quarter",
        30:"half",
        00:"o'"
    }
    timeVal=""
    
    if m in timeDict:
        timeVal=timeDict[m]
        #print(timeVal)
        
    if timeVal=="o'":
        k=n2w.num2words(h)
        print(k+" "+timeVal+" "+"clock")
        return
    
    if m>30:
        val="to"
        h+=1
        tp=60-m
        tp=n2w.num2words(tp)
        if tp.find('-')!=-1:
            tp=tp.replace('-'," ")
        #print(tp)
        h=n2w.num2words(h)
        if timeVal=="":
            print(tp+" "+"minute "+val+" "+h)
        if timeVal!="":
            print(timeVal+" "+val+" "+h)
        return
    
    if m<=30:
        val="past"
        #if m
        #tp=30-m
        if m!=0:
            tp=n2w.num2words(m)
            if tp.find('-')!=-1:
                tp=tp.replace('-'," ")
        #print(tp)
        h=n2w.num2words(h)
        if timeVal=="":
            print(tp+" "+"minute "+val+" "+h)
        if timeVal!="":
            print(timeVal+" "+val+" "+h)
        return

def inputHour():
    h=int(input())
    if h>=1 and h<=12:
        inputMinute(h)
    else:
        inputHour()

def inputMinute(h):
    m=int(input())
    if m>=0 and m<60:
        timeInWords(h, m) 
    else:
        inputMinute(h)
if __name__=='__main__':        
  inputHour()
