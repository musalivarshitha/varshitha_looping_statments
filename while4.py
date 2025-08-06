n=int(input())
summ=0
while n>0:
    rem=n%10
    summ+=rem
    n//=10
print(summ)
