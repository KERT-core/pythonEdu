numWine = int(input())

wineVal = [0] * (numWine+1)
dpWine = [0] * (numWine+1)
a = [0] * 3
for i in range(1, numWine+1):
    wineVal[i] = int(input())

dpWine[1] = wineVal[1]
dpWine[2] = wineVal[1] + wineVal[2]

for i in range(3, numWine+1):
    a[0] = dpWine[i-3]+wineVal[i-1]+wineVal[i]
    a[1] = dpWine[i-1]
    a[2] = dpWine[i-2] + wineVal[i]
    a.sort()
    dpWine[i] = a[2]

print(dpWine[numWine])



