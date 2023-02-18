import numpy as np
import stats

Preclinical_Duration = [10, 12, 14, 18]
Phase1_Duration = [16, 14, 12, 9]
Phase2_Duration = [24, 22, 35, 40]
Phase3_Duration = [40, 50, 66, 80]
Phase4_Duration = [10, 10, 10, 10]

def duration(name):
    if name == "Preclinical":
        duration = sum(Preclinical_Duration)/len(Preclinical_Duration)
        SDV = np.std(Preclinical_Duration)
        sample_duration = stats.sample_norm_dist(duration, SDV)
        return (round(sample_duration))

    elif name == "Phase 1":
        duration = sum(Phase1_Duration)/len(Phase1_Duration)
        SDV = np.std(Phase1_Duration)
        sample_duration = stats.sample_norm_dist(duration, SDV)
        return (round(sample_duration))

    elif name == "Phase 2":
        duration = sum(Phase2_Duration)/len(Phase2_Duration)
        SDV = np.std(Phase2_Duration)
        sample_duration = stats.sample_norm_dist(duration, SDV)
        return (round(sample_duration))

    elif name == "Phase 3":
        duration = sum(Phase3_Duration)/len(Phase3_Duration)
        SDV = np.std(Phase3_Duration)
        sample_duration = stats.sample_norm_dist(duration, SDV)
        return (round(sample_duration))

    elif name == "Phase 4":
        duration = sum(Phase4_Duration)/len(Phase4_Duration)
        SDV = np.std(Phase4_Duration)
        sample_duration = stats.sample_norm_dist(duration, SDV)
        return (round(sample_duration))

    return(0)
    



