import PySimpleGUI as sg

sg.theme('LightBlue2')  # Set the theme

s=['1','2','3','4','5','6','7','8',' 9 ',' 10 ',' 11 ',' 12 ',' 13 ',' 14 ',' 15 ',' 16 ',' 17 ',' 18 ',' 19 ',' 20 ',' 21 ',' 22 ',' 23 ',' 24 ',' 25 ',' 26 ',' 27b']
a=[
'''
#1
'''
,
'''
#2
print('x y z w')
for x in range(2):
   for y in range(2):
      for z in range(2):
         for w in range(2):
            if (not(y<=x) or (z<=w) or not(z))==False:
               print(x, y, z, w)
'''
,
'''
#3
'''
,
'''
#4
'''
,
'''
#5
for i in range(1,100):
    num=(bin(i)[2:])
    if num.count('1')%2==0:
        chislo='10'+num[2:]+'0'

    if num.count('1')%2!=0:
        chislo='11'+num[2:]+'1'
    if int(chislo,2)>40:
        print (i, int(chislo,2))
        break
for z in range():
    print('')
'''
,
'''
#6
from turtle import *
left(90)
for i in range(7):
    forward(300)
    right(120)
pu()
for x in range(1,9):
    for y in range(1,10):
        goto(x*30,y*30)
        dot(2)
done()
'''
,
'''
#7
'''
,
'''
#8
count=0
for a in range (1,8):
    for b in range (8):
        for c in range (8):
            for d in range (8):
                for e in range (8):
                    s=str(a)+str(b)+str(c)+str(d)+str(e)
                    if s.count('6')==1:
                        if s.index('6')==len(s)-1 and int(s[len(s)-2])%2==0:
                            count+=1
                        if s.index('6')==0 and int(s[1])%2==0:
                            count+=1
                        if s.index('6')<len(s)-1 and s.index('6')>0 and int(s[s.index('6')-1])%2==0 and int(s[s.index('6')+1])%2==0:
                            count+=1
print(count)
'''
,
'''
#9
# загрузка текста из txt
text=t.split(";")
#result = [int(item) for item in text]
result = list(map(int, text))
x=0
y=x+6
counter=double_num=0

while True:
   n=0
   res6=result[x:y]
   for element in res6:
      if res6.count(element)>2:
         for yy in range(res6.count(element)): res6.remove(element) 
         # удаление значений больше 2 штук
      if res6.count(element)==2:
         n+=2   
         double_num=element 
         res6.remove(element)
         res6.remove(element)

   if n==2 and len(res6)==4:  
      if (sum(res6)/len(res6))<=(double_num*2): counter+=1

   print(counter)
   if y>=len(result):break         
   x=x+6
   y=x+6
'''
,
'''
#10
'''
'''
#11
'''
'''
#12
spisok=[]
for num in range(2,1000):
    if all(num%delit!=0 for delit in range(2,num)):
        spisok.append(num)
        
for y in range (100):
    if y*4+117 in spisok:
        print(y)
        break
'''
'''
#13
'''
'''
#14
for x in range(15):
    a15=1*15**4+2*15**3+3*15**2+x*15**1+5
    b15=1*15**4+x*15**3+2*15**2+3*15+3
    sum10=a15 + b15
    if sum10%14==0:
        print(x , sum10//14)
        break 
'''
'''
#15
for a in range(1,100):
    if all(((x%2==0) <= (x%3!=0)) or (x+a>=100) for x in range(1,1000)):
        print(a)
        break
'''
'''
#16
#sys.setrecursionlimit(2500)
itog1=itog2=1
for x1 in range(1,2024):
    itog1=itog1*x1
for x2 in range(1,2021):
    itog2=itog2*x2
print(itog1/itog2)
'''
'''
#17
with open('17.txt') as f:
    nums=[int(x) for x in f]
    maxi=[]
    s=[]
   
    for i in range(len(nums)):
      if nums[i]%10==3:
         maxi.append(nums[i])
    maximum=0
    for i in range(len(nums)-1):
        a=abs(nums[i])%10
        b=abs(nums[i+1])%10
        if ((a==3) and (b!=3)) or ((a!=3) and (b==3)):
        if (nums[i]**2+nums[i+1]**2) >= max(maxi)**2: 
            s.append(nums[i]+nums[i+1])
            if nums[i]**2+nums[i+1]**2>maximum:
                maximum=nums[i]**2+nums[i+1]**2
print(len(s), maximum)
'''
'''
#23
def f(x,y):
    if x>y or x==17:
        return 0
    elif x==y:
        return 1
    return f(x+1,y) +f(x*2,y)
print(f(1,10)*f(10,35))
'''
'''
#24
with open('24.txt') as f:
    s=f.readline().replace('C','S').replace('D','S').replace('F','S')
    s=s.replace('A','G').replace('O','G')
    s=s.replace('SG','*')
    k=kmax=0
    for i in s:
        if i=='*'
            k+=1
            kmax=max(k,kmax)
        else:k=0
print(kmax)
'''
'''
#25
for i in range(2023,10**10,2023):
    num=str(i)
    if num[0]=='1' and num[2:6]=='2139' and num[-1]=='4':
        print(i,i//2023)
'''
'''
#27B часть загрузки данных
cost_punkt=[]
data=[]
konteiners=0
with open('27_B.txt') as f:
    d=f.readlines()
    punkts=d[0]
    
for i in range (1,len(d)):
    data.append(d[i].split())
print(punkts)
def cost(metka):
    position0=int(data[metka][0])
    cost=0
    for y in range (0,len(data)):
        konteiners=round(int(data[y][1])/36)
        if round(int(data[y][1])/36) < int(data[y][1])/36:
            konteiners=(int(data[y][1])//36) + 1
        cost+=abs(int(data[y][0])-position0) * konteiners
    return cost

mini=1000000000
num_pu=0
count_i=0
print(punkts)
metka=int(punkts)//2
first=first_etalon=cost(metka)
second=second_etalon=cost(metka+1)
metka_up=0
metka_down=len(data)-1

while True:
    first_etalon=first
    second_etalon=second
        
    first=cost(metka)
    second=cost(metka+1)
    print(f"{first} \n{second}")
    if first>second:
        first_etalon=first
        second_etalon=second
        print(metka,">")
        metka_up=metka
        delta=(metka_down-metka_up)//2
        metka=metka + delta
        print(metka)
    if first<second:
        metka_down=metka
        print(metka,"<")
        delta=(metka_down-metka_up)//2
        metka=metka - delta
        print(metka)
'''
]
# Define the layout
layout = [[sg.Combo(s, default_value=s[0], s=(15,22), enable_events=True, readonly=True, k='-COMBO-', key='Combo'),
          sg.Output(s=(40,10), key='outputt')],
          [sg.Button('Process Input', font=('Arial', 12), button_color=('white', '#4CAF50'), key='process'),
           sg.Button('Someth', font=('Arial', 12), button_color=('white', '#4CAF50'), key='button')]]

# Create the window
window = sg.Window('ЕГЭ архив', layout)

# Event loop
while True:
    event, values = window.read()

    # Exit the app when the window is closed
    if event == sg.WINDOW_CLOSED:
        break

    # Process the input and update the output when the button is clicked
    if event == 'process':
        choice=a[int(values['Combo'])-1]
        #print(choice)
        #window['outputt'].update('')
        window['outputt'].update(choice)
    if event == 'button':
        break

# Close the window
window.close()
