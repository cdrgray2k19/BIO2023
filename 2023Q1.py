n = int(input())
fib = []
f = 1
s = 2
fib.append(f)
while s <= n:
    fib.append(s)
    temp = s
    s += f
    f = temp
sumNum = []
justUsed = False
for i in range(len(fib)-1, -1, -1):
    if justUsed:
        justUsed = False
        continue
    if n >= fib[i]:
        n -= fib[i]
        sumNum.append(str(fib[i]))
        if n == 0:
            break
        justUsed = True
print(" ".join(sumNum))