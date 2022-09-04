# class calculator 
y = int(input("podaj y: "))
x = int(input("podaj x: "))
pyt = str(input("wpisz + jak chcesz dodać a - jak odjąć a jak pomnożyć * a jak podzielić / : "))
def dod(x,y):
    wynik = x + y
    print(wynik)

if pyt == "+" :
    dod(y,x)
elif pyt == "-" :
    print(y-x)
elif pyt == "*" :
    print (y*x)
elif pyt == "/" :
    print (y/x)
