n,m = input().split()
data_list = []
for i in range(int(n)):
    data = input().split()
    d = [int(data[0]),int(data[1])]
    d = sorted(d)
    data_list.append(d)
maxvalue = 0
for i in range(int(n)):
    data1 = data_list[i]
    c = 1
    for j in range(i+1,int(n)):
        data2 = data_list[j]
        if data1[1] < data2[0]:
            c += 1
    if c > maxvalue:
        maxvalue = c
print(maxvalue)





