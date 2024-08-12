def linear(num, idx=1):
    if(idx == num+1):
        return 
    
    print(idx)
    linear(num,idx+1)

linear(5)
