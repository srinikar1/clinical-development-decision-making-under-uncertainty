import classes
import hist_durations
import hist_costs

# Create the model here
Scenario = classes.Clock(1,"Scenario 1", 0, 100)

#Create the blocks
# Block Parameters (self, id, name, status, start_day, duration, end_day, worked days, accrued_cost):
Preclinical = classes.block(1,"Preclinical","Ready", 0, 0, 0, 0, 0, 0, [])
Phase_1 = classes.block(1,"Phase 1","Ready", 0, 0, 0, 0, 0, 0, [])
Phase_2 = classes.block(1,"Phase 2","Ready", 0, 0, 0, 0, 0,0, [])
Phase_3 = classes.block(1,"Phase 3","Ready", 0, 0, 0, 0, 0,0 , [])
Phase_4 = classes.block(1,"Phase 4","Ready", 0, 0, 0, 0, 0, 0, [])

Phase_1.prerequisites.append(Preclinical)
Phase_2.prerequisites.append(Phase_1)
Phase_3.prerequisites.append(Phase_2)
Phase_4.prerequisites.append(Phase_3)

#Initialise the blocks

