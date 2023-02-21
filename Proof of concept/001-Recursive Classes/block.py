import uuid # usered to generate a unique IC
from datetime import date, datetime, timedelta
import fileIO
import pandas as pd
import os
import re

# https://realpython.com/python-class-constructor/

class Block:
    _registry = [] # create a register of objects that we can iterate over
    def __init__(self, id, name):
        self._registry.append(self) 
        #self.id = uuid.uuid4()
        self.id = "Block ID"
        self.name = name
        print (self.name)

    def update_Block():
        pass


class Portfolio(Block):
    def __init__(self, id, name, portfolio):
        super().__init__(id, name)
        self.portfolio = portfolio

    def update_Portfolio():
        pass


class Compound(Portfolio):
    def __init__(self, id, name, portfolio, compound):
        super().__init__(id, name, portfolio)
        self.compound = compound

    def update_Compound():
        pass


class TherapeuticArea(Compound):
    def __init__(self, id, name, portfolio, compound, TA):
        super().__init__(id, name, portfolio, compound)
        self.TA = TA
    
    def update_TerapeuticArea():
        pass


class Task(TherapeuticArea):
    def __init__(self, id, name, portfolio, compound, TA, status, start_day, actual_start_day, duration, progress, revenue, cost):
        super().__init__(id, name, portfolio, compound, TA)
        self.status = status
        self.start_day = start_day
        self.actual_start_day = actual_start_day
        self.duration = duration
        self.progress = progress
        self.revenue = revenue
        self.cost = cost
    

    def update_Task(s, i, d):

        for b in Block._registry:

            if isinstance(b, Task):

                if d < b.start_day:
                    b.status = "Waiting"

                elif d == b.start_day:
                    b.status = "Running"
                    b.actual_start_day = d
                    b.progress = int(((d - b.actual_start_day) / b.duration) *100)


                elif d > b.start_day and d < (b.actual_start_day + b.duration):
                    b.status = "Running"
                    b.progress = int(((d - b.actual_start_day) / b.duration) *100)

                elif d == (b.actual_start_day + b.duration):
                    b.status = "Complete"
                    b.progress = int(((d - b.actual_start_day) / b.duration) * 100)
                    
                elif d > (b.actual_start_day + b.duration):
                    b.status = "Archived"
                    
                if b.status == "Running" or b.status == "Complete":
                    df_Task_list.loc[len(df_Task_list.index)] = [s,i,d,b.id, b.name, b.portfolio, b.compound, b.TA, b.status, b.start_day, b.actual_start_day, b.duration, b.progress, b.revenue, b.cost]
        pass


# ---------------------------------------------

class Montecarlo(Block):
    def __init__(self, id, name, start_day, current_day, interval_duration, intervals, iterations, scenarios):
        super().__init__(id, name)
        self.start_day = date.today()
        self.current_day = current_day
        self.interval_duration = interval_duration
        self.intervals = intervals
        self.iterations = iterations
        self.scenarios = scenarios
        print (self.name, self.start_day, self.interval_duration, self.intervals, self.iterations, self.scenarios)


    def update_Montecarlo():
        pass


#Create the Model
# b.name, b.portfolio, b.compound, b.TA, b.status, b.start_day, b.actual_start_day, b.duration, b.progress, b.revenue, b.cost
Phase1 = Task("Phase1", "Phase1", "Portfolio A", "Compound 178", "Hypertension","Ready", 0, 0, 365, 0, 0, 0)
Phase2 = Task("Phase2", "Phase2", "Portfolio A", "Compound 178", "Hypertension", "Ready", 365, 0, 365, 0, 0, 0)
Phase3 = Task("Phase3", "Phase3", "Portfolio A", "Compound 178", "Hypertension", "Ready", 730, 0, 365, 0, 0, 0)




Monte = Montecarlo("", "MC1", "","", "1", 6750, 2, 1)
       

#Setup the data outputs

df_Task_list = pd.DataFrame(columns=["MC", "Iteration", "Interval", "id", "name", "portfolio", "compound", "TA", "status", "start_day", "actual_start_day", "duration", "progress", "revenue", "cost"])


# Loop through scenarion
for s in range(Monte.scenarios):
    for i in range(Monte.iterations):
        for d in range(Monte.intervals):
            Task.update_Task(s, i, d)
            TherapeuticArea.update_TerapeuticArea()
            Compound.update_Compound
            Portfolio.update_Portfolio
            Block.update_Block()
            pass
        print("Iteration - ",i)

    pass
pass

#Print the data outputs
fileIO.df_to_csv(df_Task_list, "Tasks.csv")
















