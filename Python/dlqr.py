import numpy as np
import scipy.linalg as la
import sys

"""Solves for the optimal discrete-time LQR controller.

x(n+1) = A * x(n) + B * u(n)
J = sum(0, inf, x.T * Q * x + u.T * R * u)

Keyword arguments:
A -- numpy.matrix(states x states), The A matrix.
B -- numpy.matrix(inputs x states), The B matrix.
Q -- numpy.matrix(states x states), The state cost matrix.
R -- numpy.matrix(inputs x inputs), The control effort cost matrix.

Returns:
numpy.matrix(states x inputs), K
"""

# P = A.T * P * A - (A.T * P * B) * np.linalg.inv(R + B.T * P * B) *
#     (B.T * P.T * A) + Q

A = np.reshape(np.fromstring(sys.argv[1], sep = ','), (2, 2))

B = np.reshape(np.fromstring(sys.argv[2], sep = ','), (2, 1))

Q = np.fromstring(sys.argv[3], sep = ',')
Q = np.diag(1.0 / np.square(Q))

R = np.fromstring(sys.argv[4], sep = ',')
R = np.diag(1.0 / np.square(R))

P = la.solve_discrete_are(a=A, b=B, q=Q, r=R)

F = np.linalg.inv(R + B.T.dot(P).dot(B)).dot(B.T).dot(P).dot(A)
print('\n'.join(','.join('%0.4f' %x for x in y) for y in F))
