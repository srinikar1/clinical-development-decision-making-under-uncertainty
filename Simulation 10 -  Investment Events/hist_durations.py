import numpy as np
import stats



def duration(name):

    Preclinical_Duration = [365, 365, 365, 365]
    Phase1_Duration = [210, 200, 150, 240]
    Phase2_Duration = [720, 800, 900, 600]
    Phase3_Duration = [1095, 1500, 1300, 1400]
    Phase4_Duration = [10, 10, 10, 10]
    Market_Duration = [2000, 2000, 2000, 2000]



    Preclinical_Duration = [365, 365]
    Phase1_Duration = [210, 210]
    Phase2_Duration = [720, 720]
    Phase3_Duration = [109, 109]
    Phase4_Duration = [100, 100]
    Market_Duration = [2000, 2000]



    if name == "Preclinical":
        duration = sum(Preclinical_Duration)/len(Preclinical_Duration)
        SDV = np.std(Preclinical_Duration)
        sample_duration = stats.sample_norm_dist(duration, SDV)
        return (round(sample_duration))

    elif name == "Phase1":
        duration = sum(Phase1_Duration)/len(Phase1_Duration)
        SDV = np.std(Phase1_Duration)
        sample_duration = stats.sample_norm_dist(duration, SDV)
        return (round(sample_duration))

    elif name == "Phase2":
        duration = sum(Phase2_Duration)/len(Phase2_Duration)
        SDV = np.std(Phase2_Duration)
        sample_duration = stats.sample_norm_dist(duration, SDV)
        return (round(sample_duration))

    elif name == "Phase3":
        duration = sum(Phase3_Duration)/len(Phase3_Duration)
        SDV = np.std(Phase3_Duration)
        sample_duration = stats.sample_norm_dist(duration, SDV)
        return (round(sample_duration))

    elif name == "Phase4":
        duration = sum(Phase4_Duration)/len(Phase4_Duration)
        SDV = np.std(Phase4_Duration)
        sample_duration = stats.sample_norm_dist(duration, SDV)
        return (round(sample_duration))

    elif name == "Market":
        duration = sum(Market_Duration)/len(Market_Duration)
        SDV = np.std(Market_Duration)
        sample_duration = stats.sample_norm_dist(duration, SDV)
        return (round(sample_duration))


    return(0)
    



