import matplotlib.pyplot as plt
import math as m

#Planet = str(input("Velg hvilken planet simuleringen gjelder for: Jorda/Månen"))
starthøyde = int(input("Starthøyde (m):               "))
vinkel = int(input("Utskytnings-vinkel (deg):     "))
startfart = float(input("Utskytnings-fart (m/s):       "))

g = -9.81 # Tyngdekraftens akselerasjon
delta_t = 0.001 # Tidsoppløsning
tid_slutt = 100 # maks simulering tid
t = 0 # Start-tid for simulering
alpha = m.pi*(vinkel/180) # konverterer vinkel fra grader til radianer (for å bruke trig i math)
r = 0.02 # Luftmotstandskoeffisient (eksperimentell)
flytid = [] # åpen liste for lagring av siste t-verdi via .append

    
x = [] # Liste for x-posisjoner i simuleringen 
y = [] # Liste for y-posisjoner i simuleringen

# Posisjonsberegnings funksjon
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
            flytid.append(t)
            break
    return t

# Starter banefunksjonen (simuleringen)
bane(t) 

# Beregning av nedslagsvinkel
y_end = y[-2]-y[-1] 
x_end = x[-2]-x[-1]

# Beregning av farten i y-retning
slutthastighet_y = (y[-1]-y[-10])/(9*delta_t)

# Printer resultat
print(" ")
print("--------------------- RESULTATER ---------------------")
print("Vinkel ved nedslag:          ", m.atan(y_end/x_end)*(180/m.pi))
print("Høyde:                       ", max(y),"meter")
print("Lengde:                      ", max(x), "meter")
print("Tid i luften:                ", flytid, "sekunder")
print("Slutthastighet y:            ", -slutthastighet_y, " m/s")
print("------------------------------------------------------")

# Plotter banen
plt.plot(x, y)
plt.axis(xmin=0, ymin=0)
plt.axis('equal')
plt.show()
