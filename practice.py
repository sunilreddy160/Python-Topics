lst = [10,5,20,15,30,8]
a=0
for i in lst:
    if i>a:
        a=i
b=0
for j in lst:
    if j>b and j<a:
        print(b)