
# Complete the isBalanced function below.
open_list = ["[","{","("] 
close_list = ["]","}",")"] 
def isBalanced(myStr):
    stack = [] 
    for i in myStr: 
        if i in open_list: 
            stack.append(i) 
        elif i in close_list: 
            pos = close_list.index(i) 
            if ((len(stack) > 0) and
                (open_list[pos] == stack[len(stack)-1])): 
                stack.pop() 
            else: 
                return "NO"
    if len(stack) == 0: 
        return "YES"
    else: 
        return "NO"                    

if __name__ == '__main__':
    
    t = int(input())

    for t_itr in range(t):
        s = input()
        print(isBalanced(s))
