n=25
l=[]
sum=0
for i in range(0,n):
    ele=int(input("Enter element:"))
    sum+=ele
    l.append(ele)
mean=sum/n
print("The mean is :",mean)
l.sort()
median=l[n//2]
print("Median is :",median)

max_list=[]
d={}
for i in l:
    d[i]=d.get(i,0)+1
max_val=max(d.values())
for key in d.keys():
    if d[key]==max_val:
        max_list.append(key)

print("The mode is/are :",max_list)
    
