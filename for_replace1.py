s=input('entre string')
nw=''
for ip in range(len(s)):
    if s[ip] in 'aeiouAEIOU':
        nw+=str(ip)
    else:
        nw+=s[ip]
print(nw)
