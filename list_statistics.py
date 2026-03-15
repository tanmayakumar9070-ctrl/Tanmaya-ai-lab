def min_in_lst(lst):
    min1=lst[0]
    print("We store the minimum eliment in the min",min)
    for i in range(len(lst)):
        if lst[i]<min1:
            min1=lst[i]
    return min1
def max_in_lst(lst):
    max1=lst[len(lst)-1]
    print("We store the max eliment in the min",max)
    for i in range(len(lst)):
        if lst[i]>max1:
            max1=lst[i]
    return max1
def average_in_lst(lst):
    l=len(lst)
    print("we store length of the lst in l:",l)
    sum1=0
    print("We declare a sum1 named variable and stored inside",sum1," which is used inside the for loop")
    for i in range(l):
        sum1+=lst[i]
    return float(sum1/l)
lst=[]
for i in range(5):
    n=int(input("enter Number:"))
    lst.append(n)
print ("list is:", lst)
print("Maximum of the list is",max_in_lst(lst))
print("Minimum of the list is",min_in_lst(lst))
print("Average of the list is",average_in_lst(lst))

