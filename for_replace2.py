l=eval(input('enter list'))
new=[]
for ip in range(len(l)):
    if l[ip]%2==0:
        new+=['even']
    else:
        new+=['odd']
print(new)
