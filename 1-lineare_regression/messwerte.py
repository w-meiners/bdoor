import numpy as np

def rand_lin_messwerte(n, x_0, x_1, a, b, epsilon=5e-2):
    """ Erzeuge zufällig verteilte lineare 'Messwerte'
        n: Anzahl der Messwerte
        x_0, x_1: Messintervall, x_0 <= x < x_1
        a,b: Koeffizienten der linearen Funktion
             y = a*x+b
        epsilon: Maximaler Fehler der y-Werte
    
    """
    x_a,x_e = min(x_0,x_1), max(x_0,x_1)
    y_max = max(*[abs(a*x+b) for x in (x_0,x_1)])
    
    lx = np.linspace(x_a,x_e,n)
    
    ly = (a*lx+b) + y_max*epsilon*(0.5-np.random.random(n))
    
    return (lx,ly)

def rand_pot_messwerte(n, x_0, x_1, c, kappa, epsilon=5e-2):
    """ Erzeuge zufällig verteilte Messwerte auf einer 
        Potenzfunktion
            y = c*x**kappa
        Dabei ist 
        n: Anzahl der Messwerte
        x_0, x_1: Messintervall, x_0 <= x <= x_1
        c: Koeffizient der Potenzfunktion
        kappa: Exponent der Potenzfunktion
        epsilon: Maximaler Fehler der y-Werte    
    """
    lx, ly = rand_lin_messwerte(n, np.log(x_0), np.log(x_1), kappa, np.log(c), epsilon)
    return (np.exp(lx), np.exp(ly))