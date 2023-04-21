def f(x,spisok):
if x in spisok:
print('Простое')
else:
print("составное")
x=int(input())
spisok=[]
for num in range(2,x+1):
if all(num%delit!=0 for delit in range(2,num)):
spisok.append(num)
print(f(x,spisok))
