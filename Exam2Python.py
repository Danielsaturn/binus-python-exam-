y2h = 0
_t = 18


for x in range (5):
    
    x = float(input("Tolong masukan value x: "))
    
    if (x%2==1):
        y2h = _t-x
    elif (_t>x):
        _t = _t/x
    else:
        y2h=y2h+1
    
    print(x, y2h)
