import control as cnt
import numpy as np
import scipy.linalg as la
import sys

"""Solves for the steady state kalman gain and error covariance matrices.

Keyword arguments:
sys -- discrete state-space model
Q -- process noise covariance matrix
R -- measurement noise covariance matrix

Returns:
Kalman gain, error covariance matrix.
"""

A = np.reshape(np.fromstring(sys.argv[1], sep = ','), (2, 2))

C = np.reshape(np.fromstring(sys.argv[2], sep = ','), (1, 2))

Q = np.fromstring(sys.argv[3], sep = ',')
Q = np.diag(np.square(Q))

R = np.fromstring(sys.argv[4], sep = ',')
R = np.diag(np.square(R))

m = A.shape[0]

observability_rank = np.linalg.matrix_rank(cnt.obsv(A, C))
if observability_rank != m:
    print("Warning: Observability of %d != %d, unobservable state",
          observability_rank, m)

# Compute the steady state covariance matrix
P_prior = la.solve_discrete_are(a=A.T, b=C.T, q=Q, r=R)

S = C.dot(P_prior).dot(C.T) + R
K = P_prior.dot(C.T).dot(np.linalg.inv(S))
P = (np.eye(m) - K * C) * P_prior
L = A.dot(K)
print('\n'.join(','.join('%0.4f' %x for x in y) for y in L))
#print(P)
#return K, P
