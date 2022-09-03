# booked = []
# overlaps = []
# data1 = []
# for i in range(5):
#     data = input()
#     data = data.split(',')
#     data1.append(data)
# for i in range(5):
#     data2 = data1[i]
#     start = int(data2[0])
#     end = int(data2[1])
#     if any(s < end and start < e for s,e in overlaps):
#         print(False)
#         continue
#     for s,e in booked:
#         if s < end and start < e:
#             overlaps.append((max(s,start),min(e,end)))
#     booked.append((start,end))
#     print(True)

n=5
s = "1"
for i in range(1,n):
    m = len(s)
    t = []
    j = 0
    while j < m:
        start = j
        s1 = ""
        while  j < m and s[start] == s[j]:
            j += 1
        t.append(str(j - start) + s[start])
    s = ''.join(t)
print(s)
