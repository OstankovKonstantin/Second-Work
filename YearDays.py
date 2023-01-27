year = int(input("Введите год: "))
v = None
m = int(12)
d = int(31)
total = int(0)
if year % 4 != 0:
    v = False
elif year % 100 == 0:
    if year % 400 == 0:
         v = True
    else:
        v = False
else:
    v = True
for i in range(m):
    if ((i == 0) or (i == 2) or (i == 4) or (i == 6) or (i == 7) or (i == 9) or (i == 11)):
        d = int(32)
        for j in range(d):
            if (j<10):
                total = total + j
            elif (j >= 10):
                x = [int(a) for a in str(j)]
                for p in range(len(x)):
                    total = total + x[p]
    if ((i == 3) or (i == 5) or (i == 8) or (i == 10)):
         d = int(31)
         for j in range(d):
            if (j<10):
                total = total + j
            elif (j >= 10):
                x = [int(a) for a in str(j)]
                for p in range(len(x)):
                    total = total + x[p]
    if ((i == 1) and (v == True)):
        d = int(30)
        for j in range(d):
            if (j<10):
                total = total + j
            elif (j >= 10):
                x = [int(a) for a in str(j)]
                for p in range(len(x)):
                    total = total + x[p]
    if ((i == 1) and (v == False)):
        d = int(29)
        for j in range(d):
            if (j<10):
                total = total + j
            elif (j >= 10):
                x = [int(a) for a in str(j)]
                for p in range(len(x)):
                    total = total + x[p]
print(total)


