import stats
import hist_durations
import hist_costs

class block:
    _registry = [] # create a register of objects that we can iterate over

    def __init__(self, id, name, status, start_day, duration, end_day, worked_days, daily_rate, accrued_cost, requires):
        self._registry.append(self) #Add the newly created object to the register
        self.id = id
        self.name = name
        self.status = status
        self.start_day = start_day
        self.duration = hist_durations.duration(self.name)
        self.end_day = end_day
        self.worked_days = worked_days
        self.daily_rate = hist_costs.daily_rate(self.name)
        self.accrued_cost = accrued_cost
        self.requires = []
    
    def __requires__(self, other_node):
        self.requires.append(other_node)
    
    def __start_block__(self, current_day):
        #check if the block has pre-requisites and if it does not, then set status is starting
        all_complete = True # if there aren't any blocks in the prerequsites then the block is ready to start

        #Block without prerequisites
        if len(self.requires) == 0 and self.status == "Ready":
            self.status = "Starting"
            # print (self.name, "is starting")
        
        elif len(self.requires) > 0 and stats.all_complete(self.requires) == False:
            self.status = "Waiting"
            #self.start_day = current_day
 
        elif len(self.requires) > 0 and stats.all_complete(self.requires) == True and self.status == "Waiting":
            self.status = "Starting"
            self.start_day = current_day

            

    def __update_block__ (self, current_day):
        if self.status == "Starting":
            self.status = "Running"
            # print (self.name, "is running")

        if self.status == "Running" and self.worked_days < self.duration:
            self.worked_days = self.worked_days + 1
            self.accrued_cost = self.daily_rate 
            # print (self.name, "is running and has worked 1 day")

    def __end_block__ (self, current_day):
        if self.status == "Running" and self.worked_days == self.duration:
            self.status = "Complete"
            self.accrued_cost = 0
            # print (self.name, "is complete")




class Clock:
    def __init__(self, id, name, start_day, duration):
        self.id = id
        self.name = name
        self.start_day = start_day
        self.duration = duration

