import numpy as np


def sample_norm_dist(mean, stdev):
    # np.random.seed(0) # this sets the seed 
    s = np.random.normal(mean,stdev,1)
    return (s[0])

#this function determines of all the items in the list are true
#Return false if any blocks are not complete, return true if all blocks are complete
def all_complete(iterable):
    for item in iterable:
        if not item.status == "Complete":
            print(item.name, item.status)
            return False
        return True

