s=input('entre your str')
summ=0
ip=0
while ip<len(s):
    if s[ip] in 'aeiouAEIOU':
        summ+=ip
    ip+=1
print(summ)
