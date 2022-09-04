n,m = 6,6
d_list = []
for i in range(int(n)):
    data = input().split()
    d = [int(data[0]),int(data[1])]
    d = sorted(d)
    d_list.append(d)
maxvalue = 0
for i in range(int(n)):
    data1 = d_list[i]
    c = 1
    for j in range(i+1,int(n)):
        data2 = d_list[j]
        if data1[1] < data2[0]:
            c += 1
    if c > maxvalue:
        maxvalue = c
print(maxvalue)





