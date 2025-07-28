st=input()
s=0
a=0
d=0
for e in st:
    if not e.isalnum():
        s+=1
    elif e.isalpha():
        a+=1
    else:
        d+=1
        
print('number of special charecters',s)
print('number of alphas',a)
print('number of digits',d)
