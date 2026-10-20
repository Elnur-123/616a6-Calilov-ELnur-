numbers=[4,2,7,4,9,2,5,7,8]
b=[]
for i in numbers:
    if numbers.count(i)==1:
            b.append(i)
print(b)            