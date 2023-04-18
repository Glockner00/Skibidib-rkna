# This is a script that uses Bezier curves to draw a nice 
# representation of the letter 'd'. The script is incomplete 
# in several ways. 

import numpy as np
import matplotlib.pyplot as pp
from scipy.interpolate import CubicSpline

#
# Here you should define your subroutine DrawBezierCurve(). The cubic Bezier
# curve is defined by 4 control points. The curve should interpolate P1 and P4. 

def DrawBezierCurve( P1,P2,P3,P4,n):
    t=np.linspace(0,1,n)
    x=1
    
    P1 = np.array(P1)
    P2 = np.array(P2)
    P3 = np.array(P3)
    P4 = np.array(P4)
    
    # reshape the the valies into an np array with the size of 1 elemnt 100 times.
    return (1 - t.reshape(n,1))**3 * P1 + 3 * (1 - t.reshape(n,1))**2 * t.reshape(n,1) * P2 + 3 * (1 - t.reshape(n,1)) * t.reshape(n,1)**2 * P3 + t.reshape(n,1)**3 * P4



#
# Create a vector of points to use for defining straight line segments.
#23, 20 = p1

Points=np.array([ [70.0, 23.0, 23.0, 23.0,  23.0,  23.0,  23.0,  0.0,   0.0,   46.0, 46.0, 70.0] ,
                  [ 4.0,  0.0, 20.0, 35.0, 107.0, 125.0, 195.0, 213.0, 222.0, 225.0, 28.0, 13.0] ])

#
# Create a matrix that can be used to store the control points for the 
# Bezi'er curves. In the exercise you will successively add more points
# into this matrix.
#

Control=np.array([ [ 0.0 ] , 
                   [ 0.0 ] ])

# segment 1
P1 = [46, 28]
P2 = [46, 12]
P3 = [60, 10]
P4 = [70, 13]

# segment 2
P5 = [0, 213]
P6 = [10, 213]
P7 = [23, 213]
P8 = [23, 195]

# segment 3
P9 = [23, 107]
P10 = [10, 107]
P11 = [-10, 95]
P12 = [-10, 71]

# segment 4
P13 = [-10, 71]
P14 = [-10, 59]
P15 = [10, 35]
P16 = [23, 35]

# segment 5
P17 = [23, 125]
P18 = [0, 125]
P19 = [-20, 93]
P20 = [-20, 71]

# segment 6
P21 = [-20, 71]
P22 = [-20, 59]
P23 = [0, 20]
P24 = [23, 20]



pp.plot(DrawBezierCurve(P1, P2, P3, P4, 100)[:, 0], DrawBezierCurve(P1, P2, P3, P4, 100)[:, 1])
pp.plot(DrawBezierCurve(P5, P6, P7, P8, 100)[:, 0], DrawBezierCurve(P5, P6, P7, P8, 100)[:, 1])
pp.plot(DrawBezierCurve(P9, P10, P11, P12, 100)[:, 0], DrawBezierCurve(P9, P10, P11, P12, 100)[:, 1])
pp.plot(DrawBezierCurve(P13, P14, P15, P16, 100)[:, 0], DrawBezierCurve(P13, P14, P15, P16, 100)[:, 1])
pp.plot(DrawBezierCurve(P17, P18, P19, P20, 100)[:, 0], DrawBezierCurve(P17, P18, P19, P20, 100)[:, 1])
pp.plot(DrawBezierCurve(P21, P22, P23, P24, 100)[:, 0], DrawBezierCurve(P21, P22, P23, P24, 100)[:, 1])
# Code that can be used to cerate an "italic style" d. 
# Points[0,:]=Points[0,:]+0.07*Points[1,:]
# Control[0,:]=Control[0,:]+0.07*Control[1,:]

# Now draw the line segments of the 'd'

pp.plot( Points[0, [11,0,1,2] ],Points[1, [11,0,1,2] ],'k', color = "red" )
pp.plot( Points[0, [3,4] ], Points[1, [3,4] ],'k', color = "blue")
pp.plot( Points[0, [5,6] ], Points[1, [5,6] ],'k', color = "green")
pp.plot( Points[0, [7,8,9,10] ], Points[1, [7,8,9,10] ],'k', color = "black")

pp.xlim([-70.0,80.0])
pp.ylim([-10.0,250.0])

pp.show()

# Here is room to add the curve segments for the other exercises. In all cases
# add the points you need to either Points or Control above. Then pick out the 
# 4 control points for the curve you want to draw, e.g. P1=Points[:,3] and make
# a subroutine call DrawBezierCurve(P1,P2,P3,P4)

# Finally we set the proper axis-limits and make the plot visible.

# pp.set_aspect('equal', 'box')
# pp.xlim([-70.0,80.0])
# pp.ylim([-10.0,250.0])
# pp.show()