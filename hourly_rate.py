
hrs = input('Enter hours:')
h=float(hrs)

rph = input('Enter rate per hour:')
hrate = float(rph)

if h>40:
    extrahrs = h-40
    extrarate = 1.5*hrate
    pay = 40*hrate + extrahrs*extrarate

else:
    pay = h*hrate

print(pay)
