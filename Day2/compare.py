a=322 
b=223

list_a = list(str(a))
list_b = list(str(b))
c=len(str(a))
d=len(str(b))

j=0

if c != d:
    print "False"
else:
    for i in range(len(list_a)):
        while j<d:
           if i == list_b[j]:
            list_b.remove(list_b[j])
            break
           j=j+1
        j=0
