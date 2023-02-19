import classes
import stats


def create_clock():
    Clock_id = 1
    Clock_name = "Clock 1"
    Clock_start_day = 1
    #duration = 18*365 # in days
    duration = 18*365 # in days (stick to 1000)
    total_iterations = 2 # number of simulations, has to be a minimum of 2
    current_iteration = 0

    Clock = classes.Clock(Clock_id,Clock_name,Clock_start_day,duration, total_iterations,current_iteration)
    
    return Clock


def create_scenario():
    Scenario_ID = "MC1"
    Scenario = 0
    Initial_cost = 0
    Scenario_status = "Ready"

    Scenario = classes.scenario(Scenario_ID, Scenario, Initial_cost, Scenario_status)

    return Scenario
    

def create_model():
    
    stats.reset_model()

    #Create the blocks
    # Block Parameters (self, id, name, status, start_day, duration, end_day, worked days, accrued_cost):

    Preclinical = classes.block(1,"Preclinical","Ready", 0, 0, 0, 0, 0, 0, 0, [], [])
    Phase_1 = classes.block(1,"Phase1","Ready", 0, 0, 0, 0, 0, 0, 0, [],[])
    Phase_2 = classes.block(1,"Phase2","Ready", 0, 0, 0, 0, 0, 0,0, [], [])
    Phase_3 = classes.block(1,"Phase3","Ready", 0, 0, 0, 0, 0, 0,0 , [], [])
    #Phase_4 = classes.block(1,"Phase 4","Ready", 0, 0, 0, 0, 0, 0, 0, [],[])
    Market = classes.block(1,"Market","Ready", 0, 0, 0, 0, 0, 0, 0, [],[])

    Phase_1.requires.append(Preclinical)
    Phase_2.requires.append(Phase_1)
    Phase_3.requires.append(Phase_2)
    #Phase_4.requires.append(Phase_3)
    Market.requires.append(Phase_3)

    pass




