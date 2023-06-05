#Denna uträkning görs i bollbana.py och den ger s = 14 varv/sekund.

# Fil f�r simulering av bollr�relse. P� slutet finns �ven ett exempel d�r en straffspark simuleras.
import numpy as np
import matplotlib.pyplot as pp
from mpl_toolkits import mplot3d
from scipy.integrate import odeint

#BollODE: Funktion f�r att ber�kna h�gerledet i differential-
# ekvationen som styr bollens r�relse.
# 
def BollODE( S , t ):
    # Fysikaliska parametrar
    m=0.3056   # Bollens massa [kg]
    g=9.81     # Tyngdkraftsaccelerationen [m/s^2]
    r=0.105    # Bollens Radie [m]
    rho=1.2    # Luftensdensitet [kg/m^3]
    A=0.0375   # Tv�rsnittsarean [m^2]
    Cd=0.14    # Luftmotst�ndskoefficient.
    Cl=0.14    # Koefficient f�r Magnus kraft 
    omega=np.array([0 , -8.9 , 0]) # Rotationsmomentetvektor.
    
    
    
    # Tillst�ndsvektorn �r S=[ P ; V ], d�r P �r position och
    # V �r hastigheten. Notera fullst�ndigt vansinniga indexeringen.
    P=S[0:3]
    V=S[3:6]
    
    # Ber�kna nu de krafter som verkar p� bollen. F�rst ut �r
    # Tyngdkraften Fm.
  
    G=np.array([ 0 , 0 , -g])
    Fm=m*G
  
    # H�r kan du inf�ra de SciLab kommandon som kr�vs f�r att
    # Ber�kna den kraft luftmotst�ndet ger upphov till.
  
    Fd=np.array([0 , 0 ,  0])
    Fd= -1/2 * rho *  A * Cd * np.sqrt(S[3]**2 + S[4]**2 + S[5]**2) * V

    # Slutligen ber�knas Magnuskraften. H�r skall np.cross() anv�ndas
    # f�r att ber�kna vektorprodukten.
    
    Fl=np.array([0 , 0 ,  0])
    Fl = Cl * rho * A * (np.cross(omega, V ))
    print(np.abs(omega)/2*np.pi) # varv per sekund.

    
    # Kraften ger nu accelerationen, eller derivatan 
    # av hastighetsvektorn enligt Newtons lag F=m*a.
    
    F=Fm+Fd+Fl # Detta �r summan av krafterna som verkar p� bollen.
    A=F/m
    dS=np.zeros(6)
    dS[0:3]=V
    dS[3:6]=A
    return dS
   

# Det �r bara den del av bollbanan d�r z>0 som �r fysikaliskt rimlig. Vi skall 
# bara plotta den delen. H�r tar vi in (t,z(t)) och hittar de punkter som skall
# ritas upp. Eventuellt �r hela bollbanan fysikaliskt rimlig.
def HittaRelevantaVarden( z ):
    for k in range(np.size(t)):
        if z[k]<0:
            return k
    return np.size(t)-1



#=====================================================================
#
# H�r finns kod f�r att simulera bollbanan med BollODE som h�gerleds
# funktion som den �r definierad ovan. Vi ritar �ven upp bollbanan och
# skriver ut var bollen landar
#
# G�r kopior av denna f�r att l�sa de olika uppgifterna. 
#
P0=np.array([0,0,0])        # Utg�ngsposition
V0=np.array([17.32,0.45,11.51])  # Utg�ngshastighet
S0=np.zeros(6)
S0[0:3]=P0
S0[3:6]=V0                  # Starttillst�ndet

n=500                       # Vi s�ker l�sningen i intervallet 0<t<5 [s]. 
t=np.linspace(0,5,n)

BollBanan = odeint(BollODE, S0, t ) # Ber�knar nu l�sningen. Varje rad blir 
                                    # Tillst�ndet f�r en given tidpunkt. Allts�
                                    # S( t[k] ) = BollBanan[ k , : ]


fig = pp.figure()             # Nu g�r vi en 3D plot av bollbanan.
ax=pp.axes(projection='3d')
k=HittaRelevantaVarden(BollBanan[:,2])  # Hitta positiva z-v�rden
ax.plot3D(BollBanan[0:k+1,0],BollBanan[0:k+1,1],BollBanan[0:k+1,2],'blue')
ax.set_aspect('equal')
pp.xlabel('x [m]')
pp.ylabel('y [m]')
pp.title('Fotbollens bana');
print("Bollen landar vid x={} och y={} [m]".format(BollBanan[k,0],BollBanan[k,1]))
ax.plot3D(35.3*np.array([1,1,1,1]),7.32*np.array([-1,-1,1,1])/2,2.44*np.array([0,1,1,0]))
pp.show()


#===========================================================================
# 
# H�r finns parametrar sparade f�r den Straffspark som Roberto Carlos
# �r ber�md f�r. Det som eventuellt �r fel �r sid-spinnet i omega vektorn.
#
#  
#  // Fysikaliska parametrar
#  m=0.3056;                           # Bollens massa [kg]
#  r=0.105;                            # Bollens Radie [m]
#  g=9.81;                             # Tyngdkraftsaccelerationen [m/s^2]
#  rho=1.2;                            # Luftensdensitet [kg/m^3]
#  A=0.0375;                           # Tv�rsnittsarean [m^2]
#  Cd=0.14;                            # Luftmotst�ndskoefficient.
#  Cl=0.16;                            # Koefficient f�r Magnus kraft 
#  omega=np.array([0 , -8.9 , 0])      # Rotationsmomentetvektor.
#  V0=np.array([35.4 , -14.9 ,  4.13]) # Utg�ngshastighet

#
# H�r finns en kod-rad som ritar upp fotbollsm�let. Avdt�ndet till m�let
# �r 35.4 meter.
#
