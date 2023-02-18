import classes
import hist_durations
import hist_costs
import stats



def create_clock(id, name, start_day, duration, total_iterations, current_iteration):
    # Create the model here
    Clock = classes.Clock(id,name, start_day, duration, total_iterations, current_iteration)
    return Clock


def create_model():

    stats.reset_model()

    #Create the blocks
    # Block Parameters (self, id, name, status, start_day, duration, end_day, worked days, accrued_cost):
    Preclinical = classes.block(1,"Preclinical","Ready", 0, 0, 0, 0, 0, 0, [], [])
    Phase_1 = classes.block(1,"Phase1","Ready", 0, 0, 0, 0, 0, 0, [],[])
    Phase_2 = classes.block(1,"Phase2","Ready", 0, 0, 0, 0, 0,0, [], [])
    Phase_3 = classes.block(1,"Phase3","Ready", 0, 0, 0, 0, 0,0 , [], [])
    #Phase_4 = classes.block(1,"Phase 4","Ready", 0, 0, 0, 0, 0, 0, [],[])
    Market = classes.block(1,"Market","Ready", 0, 0, 0, 0, 0, 0, [],[])

    Phase_1.requires.append(Preclinical)
    Phase_2.requires.append(Phase_1)
    Phase_3.requires.append(Phase_2)
    #Phase_4.requires.append(Phase_3)
    Market.requires.append(Phase_3)




