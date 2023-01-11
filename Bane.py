import matplotlib.pyplot as plt
import math as m

g = -9.81
delta_t = 0.001
tid_slutt = 100
t = 0
starthøyde = 0
vinkel = int(input("utskytnings-vinkel (deg): "))
alpha = m.pi*(vinkel/180)
startfart = int(input("utskytnings-fart (m/s): "))
r = 0.02


    
x = []
y = []

def bane(t):
    while t <= tid_slutt:
        xv = m.cos(alpha)*startfart**(1-r*t)
        yv = m.sin(alpha)*startfart**(1-r*t)
        y_n = starthøyde+m.sin(alpha)*yv*t+0.5*g*t**2
        x_n = m.cos(alpha)*xv*t
        x.append(x_n)
        y.append(y_n)
        t = t+delta_t
        if y_n < 0:
            break
    return t
bane(t)
y_end = y[-2]-y[-1]
x_end = x[-2]-x[-1]
print("vinkel ved nedslag = ", m.atan(y_end/x_end)*(180/m.pi))
print("Banens maxima: ", max(y)," meter")
print("Lengde = ", max(x), "meter")

#mpl.axis(xlim=(0, 1000), ylim=(0, 1000))
plt.plot(x, y)
plt.xlim(0)
#plt.ylim(0,20)
plt.axis('equal')
plt.show()
