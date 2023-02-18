import numpy as np
import classes
import fileIO
import gc

def sample_norm_dist(mean, stdev):
    # np.random.seed(0) # this sets the seed 
    s = np.random.normal(mean,stdev,1)
    return (s[0])

#this function determines of all the items in the list are true
#Return false if any blocks are not complete, return true if all blocks are complete
def all_complete(iterable):
    for item in iterable:
        if not item.status == "Complete":
            # print(item.name, item.status)
            return False
        return True


def update_blocks (current_day, iteration_id, iteration):
    # print ("Trace 1")


    for b in classes.block._registry:

        classes.block.__start_block__(b, current_day)
        classes.block.__update_block__(b, current_day)
        classes.block.__end_block__(b, current_day)
                    
        data = iteration_id, iteration, current_day, b.name, b.start_day, b.duration, b.end_day, b.status, b.worked_days, b.daily_rate, b.accrued_cost
        data2 = str(data).replace('(','').replace(')','').replace('\'','').replace('\"','')

        # print (data2)
        file_name = "Block_Detail.csv"
        
        # print (file_name)
        # fileIO.write_to_file (file_name, data2)


    # if any block has failed (False) then stop the simulation

    for b in classes.block._registry:
        if b.status == False:
            print (iteration_id, iteration, b, current_day, b.name, b.status)
            return (b.status)






def reset_model ():

#    for obj in gc.get_objects():
#        if isinstance(obj,classes.block):
#            print("deleting", obj)
#            del (obj)
        
#        elif isinstance(obj,activities.activity):
#            print("deleting", obj)
#            del (obj)

    for item in classes.block._registry.copy():
        classes.block._registry.remove(item)

    for item in classes.activity._registry.copy():
        classes.activity._registry.remove(item)


"""
    for item in classes.iteration._registry.copy():
        classes.activity._registry.remove(item)

"""


#    for block in classes.block._registry:
#            classes.block._registry.remove (block)
#
#    for act in activities.activity._registry:
#            activities.activity._registry.remove (act)

 






