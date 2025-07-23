s=input('entre the string')
a='aeiouAEIOU'
c=0
for e in s:
    if e.isalpha()and e not in a:
        c+=1
print(c)
    
