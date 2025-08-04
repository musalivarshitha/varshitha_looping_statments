s=input()
for ip in range(len(s)):
    if s[ip] in 'aeiouAEIOU':
        print(ip)
