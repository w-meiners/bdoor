import numpy as np

def rand_messwerte(
    n, # Anzahl der Messpunkte
    x_0, x_1, # Messintervall
    a, b, # Koeffizienten der linearen Funktion
    epsilon=5e-2, # maximaler prozentualer Fehler in Prozent
):
    
    x_a,x_e = max(x_0,x_1), min(x_0,x_1)
    y_a,y_e = [a*x+b for x in (x_a,x_e)]
    
    lx = np.linspace(x_a,x_e,n)
    
    y_max = max(*[abs(v) for v in (y_a,y_e)])
    
    ly = (a*lx+b) + y_max*epsilon*(0.5-np.random.random(n))
    
    return zip(lx,ly)
    
