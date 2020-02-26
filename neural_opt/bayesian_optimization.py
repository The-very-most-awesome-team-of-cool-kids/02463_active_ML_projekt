from objective_function import objective_function
import numpy as np
import GPyOpt
import random
import time


from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
import numpy as np
from numpy.random import multivariate_normal

# set seed
seed = 4200
np.random.seed(seed)
random.seed(seed)

# learning rate
learning_rate = tuple(np.arange(0.0001,0.01 ,0.0001, dtype= np.float))
#optimizer (SGD, Adam)
optimizer_dict = {0: "SGD", 1: "ADAM"}
optimizer = (0, 1)

#zero padding: 0 = false, 1 = true
zero_padding_dict = {0: False, 1: True}
zero_padding = (0,1)


# define the dictionary for GPyOpt

domain = [{'name': 'learning_rate', 'type': 'discrete', 'domain': learning_rate},
            {'name': 'optimizer', 'type': 'categorical', 'domain': optimizer}]


#optimization
opt = GPyOpt.methods.BayesianOptimization(f = objective_function,   # function to optimize
                                              domain = domain,         # box-constrains of the problem
                                              acquisition_type = 'EI' ,      # Select acquisition function MPI, EI, LCB
                                             )


opt.acquisition.exploration_weight = 0.3

t_opt = time.time()
opt.run_optimization(max_iter = 20) 
print("-"*30)
print("Optimization finished!")
print(f"Time used for optimization: {time.time()-t_opt} seconds")

x_best = opt.X[np.argmin(opt.Y)]
print(f"Best accuracy was obtained at {opt.fx_opt*-1} %")
print("The best parameters obtained: learning rate=" + str(x_best[0]) + ", optimizer=" + str(optimizer_dict[x_best[1]]))

# plots
# GPyOpt.plotting.plots_bo.plot_acquisition(opt)
# GPyOpt.plotting.plots_bo.plot.convergence(opt)
