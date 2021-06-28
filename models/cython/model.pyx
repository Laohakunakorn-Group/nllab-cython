# Cythonized ODEs from antimony file

import numpy as np
cimport numpy as np
cimport cython
from libc.math cimport exp
from libc.math cimport sqrt
from libc.math cimport pow

@cython.cdivision(True) # Zero-division checking turned off
@cython.boundscheck(False) # Bounds checking turned off for this function
@cython.wraparound(False)  # turn off negative index wrapping for entire function
def model(np.ndarray[np.float64_t,ndim=1] y, double t, np.ndarray[np.float64_t,ndim=1] params):

	cdef double S1 = y[0]
	cdef double S2 = y[1]
	cdef double S3 = y[2]

	cdef double alpha = params[0]
	cdef double K = params[1]
	cdef double n = params[2]
	cdef double k = params[3]

	cdef double derivs[3]

	derivs = [
	alpha*pow(K,n)/(pow(K,n)+pow(S3,n))-k*S1,
	alpha*pow(K,n)/(pow(K,n)+pow(S1,n))-k*S2,
	alpha*pow(K,n)/(pow(K,n)+pow(S2,n))-k*S3]
	return derivs