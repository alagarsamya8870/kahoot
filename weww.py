x=int(input())
y=[]
for i in range(0,x):  
    u=input()
    y.append(u)
list=[]
for i in zip(*y):
    if (i.count(i[0])==len(i)): 
        list.append(i[0])
    else:
        break
print(''.join(list))
