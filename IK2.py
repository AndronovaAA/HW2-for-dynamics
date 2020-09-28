import numpy as np
def R_z(q):
    return np.array([[np.math.cos(q), -np.math.sin(q), 0, 0],
                     [np.math.sin(q), np.math.cos(q), 0, 0],
                     [0, 0, 1, 0],
                     [0, 0, 0, 1]])
def R_x(q):
    return np.array([[1, 0, 0, 0],
                     [0, np.math.cos(q), -np.math.sin(q), 0],
                     [0, np.math.sin(q), np.math.cos(q), 0],
                     [0, 0, 0, 1]])
def R_y(q):
    return np.array([[np.math.cos(q), 0, np.math.sin(q), 0],
                     [0, 1, 0, 0],
                     [-np.math.sin(q), 0, np.math.cos(q), 0],
                     [0, 0, 0, 1]])
def T_x(a):
    return np.array([[1, 0, 0, a],
                     [0, 1, 0, 0],
                     [0, 0, 1, 0],
                     [0, 0, 0, 1]])
def T_y(a):
    return np.array([[1, 0, 0, 0],
                     [0, 1, 0, a],
                     [0, 0, 1, 0],
                     [0, 0, 0, 1]])
def T_z(a):
    return np.array([[1, 0, 0, 0],
                     [0, 1, 0, 0],
                     [0, 0, 1, a],
                     [0, 0, 0, 1]])

def IK(T):
    L0 = 0
    L11 = 0.324
    L12 = 0.312
    L2 = 1.075
    L31 = 0.225
    L32 = 1.076
    L4 = 0.204
    L5 = 0.215



    #Calculating the position of a tool
    coord_tool = np.array([T[0, 3], T[1, 3], T[2, 3]])
    coord_tool = coord_tool

    R = np.array([[T[0,0], T[0,1], T[0,2]],
         [T[1,0], T[1,1], T[1,2]],
         [T[2, 0], T[2, 1], T[2, 2]]])


    coord_c = coord_tool - L5 * R[:,1]

    coord_c = np.transpose(coord_c)

    print (coord_c)

    theta1 = np.arctan2(coord_c[1], coord_c[0])

    L34 = L32 + L4
    p = np.sqrt(L31 ** 2+L34 ** 2)
    q = np.sqrt(coord_c[0] ** 2 + coord_c[1] ** 2)-L12
    s = np.sqrt((L11-coord_c[2]) ** 2 + q ** 2)

    ca = (L2 ** 2 + s ** 2 - p ** 2) / (2 * L2 * s)
    print(ca)

    alpha = np.arctan2(np.sqrt(1 - ca ** 2), ca)
    beta = np.arctan2(L11 - coord_c[2], q)
    theta2 = beta - alpha

    fi = np.arctan2(L34, L31)
    psi1 = (L2 ** 2 + p**2-s**2)/(2*L2*p)
    psi2 = np.arctan2(np.sqrt(1-psi1**2), psi1)
    theta3 = 3.14-fi-psi2

    H0_3 = np.dot(R_z(theta1), np.dot(T_z(L11), np.dot(T_x(L12), np.dot(R_y(theta2), np.dot(T_z(L2), np.dot(R_y(theta3), T_x(L31)))))))
    R3_6 = np.linalg.inv(H0_3) * T

    theta4 = np.arctan2(R3_6[1][0], R3_6[2][0])

    theta5 = np.arccos(R3_6[2][2])

    theta6 = np.arccos(-R3_6[2][0] / np.sin(theta5))

    theta = [theta1, theta2, theta3, theta4, theta5, theta6]

    return theta

H = np.array([[ 1,  0, 0,  2.891],
               [0, 1, 0,  0],
               [0,  0, 1, 0.549],
               [0,  0,  0,  1]])

print(IK(H))