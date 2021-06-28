# Python ODE

import numpy as np

def model(y, t, params):

	S1 = y[0]
	S2 = y[1]
	S3 = y[2]

	alpha = params[0]
	K = params[1]
	n = params[2]
	k = params[3]

	derivs = [
	alpha*K**n/(K**n+S3**n)-k*S1,
	alpha*K**n/(K**n+S1**n)-k*S2,
	alpha*K**n/(K**n+S2**n)-k*S3]
	return derivs