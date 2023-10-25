from random import randint
a=[]
for i in range (10):
    a.append (randint(1,100))
    print (a)
for i in range  (9):
 for j in range (9-i):
        if a[j]>a[j+1]:
            a[j], a[j+1]=a[j+1], a[j]
print (a)
