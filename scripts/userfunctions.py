import numpy as np


def single_angle_gap(xTest,yTest,xData,yData):
    xi = (xData - xData.min()) / xData.ptp()
    yi = (yData - yData.min()) / yData.ptp()
    
    xVal = (xTest - xData.min()) / xData.ptp()
    yVal = (yTest - yData.min()) / yData.ptp()
    
    dx = xi - xVal
    dy = yi - yVal
    
    if any((dx == 0) & (dy == 0)):
        gap = 0
        return gap
        
    theta = np.arctan(dy/dx)
    theta[dx<0] = theta[dx<0] + np.pi
    theta[(dx>0) & (dy<0)] = theta[(dx>0) & (dy<0)] + 2*np.pi
    theta[(dx==0) & (dy>0)] = np.pi/2
    theta[(dx==0) & (dy<0)] = 3*np.pi/2

    test = np.sort(theta)
    test = np.append(test,test[0] + 2*np.pi)
    gap = np.max(np.diff(test))*180/np.pi

    return gap


		
def angle_gap(xTest,yTest,xData,yData):
    
    dim = np.core.fromnumeric.shape(xTest)  
    
    if np.size(dim) == 0:
        gap = single_angle_gap(xTest,yTest,xData,yData)
        
        return gap
    
    
    gap = np.zeros(dim)
    
    
    if np.size(dim) == 1:
        for i in range(dim[0]):
            gap[i] = single_angle_gap(xTest[i],yTest[i],xData,yData)
            
        return gap
    
    
    for i in range(dim[0]):
        for j in range (dim[1]):
            gap[i,j] = single_angle_gap(xTest[i,j],yTest[i,j],xData,yData)

    return gap