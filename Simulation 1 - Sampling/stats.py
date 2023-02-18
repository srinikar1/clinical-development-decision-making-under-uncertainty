import numpy as np


def sample_norm_dist(mean, stdev):
    # np.random.seed(0) # this sets the seed 
    s = np.random.normal(mean,stdev,1)
    return (s[0])


# sampler = qmc.LatinHypercube(d=1, seed=42)    # d = dimension
# sample = sampler.random(n=1)
# print(sampler)