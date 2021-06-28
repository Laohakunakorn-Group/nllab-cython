# Simulate the Cython model
# using ODEs for the repressilator as an example

from scipy.integrate import odeint
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import os

#here = "/app" # Docker image mount point. 
here = os.getcwd() # Use this if running locally.
PATH_TO_OUTPUT = here+"/output/" # Path for output data, plots
FILENAME = "repressilator_cython.csv" # Filename for output data

# Solve ODEs 
from models.cython import model as R3 # import the cython model

y0 = np.array([0,0,1])
params = np.array([1,1,4,0.5])
TMAX = 100 
NSTEPS = 1000

time = np.linspace(0,TMAX,NSTEPS)
sol = odeint(R3.model, y0, time, args=(params,)) # Scipy solver

# Plot and save plot
for i in range(sol.shape[1]):
    plt.plot(time,sol[:,i], label='S'+str(i));
plt.xlabel('t'); plt.ylabel('concs'); plt.legend()   
plt.savefig(PATH_TO_OUTPUT+'plot_cython.pdf',transparent=True)
#plt.show() 

# Save data
df = pd.DataFrame(sol)
df.to_csv(PATH_TO_OUTPUT+FILENAME, index=None)