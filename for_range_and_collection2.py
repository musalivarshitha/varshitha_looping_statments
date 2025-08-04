s=input()
summ=0
for ip in range(len(s)):
    if s[ip].isalpha()and s[ip].lower() not in 'aeiou':
        summ+=ip
print(summ)
