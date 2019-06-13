x=int(input())
y=[]
for i in range(x):
    y.append(input())
z=y[0]
x,c=0,0
y1=""
for i in range(len(z)):
    c=0
    for j in range(1,x):
          if z[i]==y[j][i]:
            c=c+1
    if c==x-1:
       y1=y1+z[i]
    else:
        break
print(y1)
