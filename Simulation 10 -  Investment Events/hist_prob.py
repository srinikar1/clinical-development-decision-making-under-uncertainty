import numpy as np
import stats
import random


# This table shows the sample daily_rates associated with each phase, based on a daily rate



def decision(probability):
    return random.random() < probability



def prob_success(name):

    Preclinical_success = [1.0]
    Phase1_success = [1.0]
    Phase2_success =  [1.0]
    Phase3_success =  [1.0]
    Phase4_success = [1.0]
    Market_success = [1.0]


    Preclinical_success = [0.9]
    Phase1_success = [0.9]
    Phase2_success =  [0.70]
    Phase3_success =  [0.95]
    Phase4_success = [1]
    Market_success = [1]







    if name == "Preclinical":
        probability = Preclinical_success[0]
        val = decision(probability)
        return (val)

    elif name == "Phase1":
        probability = Phase1_success[0]
        val = decision(probability)
        return (val)

    elif name == "Phase2":
        probability = Phase2_success[0]
        val = decision(probability)
        return (val)

    elif name == "Phase3":
        probability = Phase3_success[0]
        val = decision(probability)
        return (val)

    elif name == "Phase4":
        probability = Phase4_success[0]
        val = decision(probability)
        return (val)


    elif name == "Market":
        probability = Market_success[0]
        val = decision(probability)
        return (val)

    return(0)
    
