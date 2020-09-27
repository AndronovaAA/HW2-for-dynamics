# coding=utf-8
import math
import numpy as np
from sympy import *
#import matplotlib as plt

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
def FK(q, l):
    T = np.dot(R_z(q[0]),
        np.dot(T_z(l[1]), np.dot(T_x(l[2]),
        np.dot(R_y(q[1]), np.dot(T_x(l[3]),
        np.dot(R_y(q[2]), np.dot(T_z(l[4]),
        np.dot(T_x(l[5]), np.dot(R_x(q[3]),
        np.dot(R_y(q[4]), np.dot(T_x(l[6]),
        R_x(q[5]))))))))))))

    return T

[q1, q2, q3, q4, q5, q6] = [pi/2, -pi/2, 0, -pi/2, 0, 0]
[l1, l2, l3, l4, l5, l6, l7] = [346, 324, 321, 1075, 225, 1280, 215]

print(FK([q1, q2, q3, q4, q5, q6], [l1, l2, l3, l4, l5, l6, l7]))