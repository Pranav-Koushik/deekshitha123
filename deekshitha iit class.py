import numpy as np
A=np.array([[2,-3],[4,-6]])
a1=np.array([2,4])
a2=np.array([-3,-6])
b=np.array([8,9])
det_A = np.linalg.det(A)
x_num=[b,a1]
y_num=[a1,b]
if det_A!=0:
         print("unique sol")
elif (np.linalg.det(x_num)==0 and np.linalg.det(y_num)==0):
         print("infinte")
else:
         print("no sol")



