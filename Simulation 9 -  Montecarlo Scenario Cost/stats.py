import numpy as np
import classes
import fileIO


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


def update_blocks (current_day, iteration_id, iteration, df_block_list, write_block_list):

    for b in classes.block._registry:

        classes.block.__start_block__(b, current_day)
        classes.block.__update_block__(b, current_day)
        classes.block.__end_block__(b, current_day)

        if write_block_list == True:
            #print (current_day)
            df_block_list.loc[len(df_block_list.index)] = [iteration_id, iteration, current_day, b.name, b.start_day, b.duration, b.end_day, b.status, b.worked_days, b.daily_rate, b.accrued_cost]
            fileIO.df_to_csv (df_block_list, "Block_List.csv")

    # if any block has failed (False) then stop the simulation

    for b in classes.block._registry:
        if b.status == "Failed":
            # print (iteration_id, iteration, b, current_day, b.name, b.status)
            return (b.status, b.name)
    return ("Continue", b.name)
    

def reset_model ():


    for item in classes.block._registry.copy():
        classes.block._registry.remove(item)

    for item in classes.activity._registry.copy():
        classes.activity._registry.remove(item)








