import numpy as np
import matplotlib.pyplot as plt

def DrawBezierCurve(P1, P2, P3, P4, n):
    t = np.linspace(0, 1, n)
    
    P1 = np.array(P1)
    P2 = np.array(P2)
    P3 = np.array(P3)
    P4 = np.array(P4)
    
    # reshape the the valies into an np array with the size of 1 elemnt 100 times.
    p_t = (1 - t.reshape(n,1))**3 * P1 + 3 * (1 - t.reshape(n,1))**2 * t.reshape(n,1) * P2 + 3 * (1 - t.reshape(n,1)) * t.reshape(n,1)**2 * P3 + t.reshape(n,1)**3 * P4

    plt.plot(p_t[:, 0], p_t[:, 1], label='Beziér curve')
    # plot all the control points.
    plt.scatter([P1[0], P2[0], P3[0], P4[0]], [P1[1], P2[1], P3[1], P4[1]], color='red', label='Control points')
    
    # Plot dotted lines between control points
    plt.plot([P1[0], P2[0]], [P1[1], P2[1]], '--', color='gray')
    plt.plot([P2[0], P3[0]], [P2[1], P3[1]], '--', color='gray')
    plt.plot([P3[0], P4[0]], [P3[1], P4[1]], '--', color='gray')
    
    plt.legend()
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Cubic Beziér curve and control points')
    plt.show()

P1 = [0, 0]
P2 = [0, 1.2]
P3 = [3, 2]
P4 = [4, 1.5]

DrawBezierCurve(P1, P2, P3, P4, 100)