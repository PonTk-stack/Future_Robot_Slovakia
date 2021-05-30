import numpy as np

l_1=21#回転台から回転軸まで[mm]
l_2=88.5#リンク2[mm]
l_3=88.5#リンク３[mm]
l_4=153#ロボットハンド全長[mm]

theta_1= 45*np.pi/180#回転角1[rad]
theta_2 =10*np.pi/180#回転角２[rad]
theta_3=0*np.pi/180#回転角3[rad]
theta_4=0*np.pi/180#回転角4[rad]


C_1 = np.cos(theta_1)
C_2 = np.cos(theta_2)
C_3 = np.cos(theta_3)
C_4 = np.cos(theta_4)



S_1 = np.sin(theta_1)
S_2 = np.sin(theta_2)
S_3 = np.sin(theta_3)
S_4 = np.sin(theta_4)



P_r = np.empty([1,3])


P_r[0,0] =C_1*S_2*l_2+C_1*np.sin(theta_2 + theta_3)*l_3 + C_1*np.sin(theta_2+theta_3+theta_4)*l_4
P_r[0,1] = S_1*S_2*l_2 + S_1*np.sin(theta_2+theta_3)*l_3+S_1*np.sin(theta_2+theta_3+theta_4)*l_4
P_r[0,2] = l_1*C_2 + np.cos(theta_2+theta_3)*l_3 +np.cos(theta_2+theta_3 + theta_4)*l_4

print(P_r)
