l1=[[1,2],[3,4]]
l2=[[4,3],[2,1]]
l3=[] #[[8,5]]
for i in range(len(l1)):#0<2
    l=[]#8 ,5
    for j in range(len(l1[i])):#2<2
        add=0 #0
        for k in range(len(l1[i])):#2<2
            add=add+(l1[i][k]*l2[k][j]) # 4+l1[0][1]+l2[1][1] ->0+(2*1)
        l.append(add)
    l3.append(l)
print(l3)