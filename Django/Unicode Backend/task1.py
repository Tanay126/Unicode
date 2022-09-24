def fun(n1,n2):
    output={}
    for num in range(n1,n2):
        bin_num=bin(num).replace("0b","")
        if bin_num.find('11')!=-1:
            output[num]=True
        else:
            output[num]=False
    return output

n1=input("Enter the start of the range:")
n2=input("Enter the end of the range:")
print(fun(int(n1),int(n2)))