import numpy as np
import stats


# This table shows the sample daily_rates associated with each phase, based on a daily rate



Preclinical_daily_rate = [-1000, -1500, -2500, -2800]
Phase1_daily_rate = [-2000, -1500, -2500, -2800]
Phase2_daily_rate =  [-7000, -6000, -4000, -8000]
Phase3_daily_rate =  [-5000, -6000, -5000, -7000]
Phase4_daily_rate = [-2000, -1500, -2500, -2800]
Market_daily_rate = [3000]



'''
Preclinical_daily_rate = [-000, 1500, 2500, 2800]
Phase1_daily_rate = [2000, 1500, 2500, 2800]
Phase2_daily_rate =  [7000, 6000, 4000, 8000]
Phase3_daily_rate =  [5000, 6000, 5000, 7000]
Phase4_daily_rate = [2000, 1500, 2500, 2800]
Market_daily_rate = [-3000]
'''

def daily_rate(name):

    if name == "Preclinical":
        daily_rate = sum(Preclinical_daily_rate)/len(Preclinical_daily_rate)
        SDV = np.std(Preclinical_daily_rate)
        sample_daily_rate = stats.sample_norm_dist(daily_rate, SDV)
        return (round(sample_daily_rate))

    elif name == "Phase1":
        daily_rate = sum(Phase1_daily_rate)/len(Phase1_daily_rate)
        SDV = np.std(Phase1_daily_rate)
        sample_daily_rate = stats.sample_norm_dist(daily_rate, SDV)
        return (round(sample_daily_rate))

    elif name == "Phase2":
        daily_rate = sum(Phase2_daily_rate)/len(Phase2_daily_rate)
        SDV = np.std(Phase2_daily_rate)
        sample_daily_rate = stats.sample_norm_dist(daily_rate, SDV)
        return (round(sample_daily_rate))

    elif name == "Phase3":
        daily_rate = sum(Phase3_daily_rate)/len(Phase3_daily_rate)
        SDV = np.std(Phase3_daily_rate)
        sample_daily_rate = stats.sample_norm_dist(daily_rate, SDV)
        return (round(sample_daily_rate))

    elif name == "Phase4":
        daily_rate = sum(Phase4_daily_rate)/len(Phase4_daily_rate)
        SDV = np.std(Phase4_daily_rate)
        sample_daily_rate = stats.sample_norm_dist(daily_rate, SDV)
        return (round(sample_daily_rate))


    elif name == "Market":
        daily_rate = sum(Market_daily_rate)/len(Market_daily_rate)
        SDV = np.std(Market_daily_rate)
        sample_daily_rate = stats.sample_norm_dist(daily_rate, SDV)
        return (round(sample_daily_rate))

    return(0)
    
