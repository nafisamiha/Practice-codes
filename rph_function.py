def computepay(r,h):
    if h<=40:
        pay=r*h
    else:
        xtime=h-40
        xrate=r+r*0.5
        pay=r*40 + xrate*xtime
    return pay

r=input('Rate : ')
h=input('Time : ')
r=float(r)
h=int(h)
pay=computepay(r,h)
print('Pay',pay)
