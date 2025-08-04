s=input()
summ=0
for eip in range(0,len(s),2):
    if s[eip] in '02468':
        summ+=eip
print(summ)
