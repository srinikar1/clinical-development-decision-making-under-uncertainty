import stats
import hist_durations
import hist_costs
import hist_prob
import classes





class block:
    _registry = [] # create a register of objects that we can iterate over

    def __init__(self, id, name, status, start_day, duration, end_day, worked_days, daily_rate, accrued_cost, requires, activities):
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
        self.activities = []
    
    def __requires__(self, other_node):
        self.requires.append(other_node)
    
    def __start_block__(self, current_day):
        #check if the block has pre-requisites and if it does not, then set status is starting
        all_complete = True # Assume all complete is true to begin with

        #Block without prerequisites
        if len(self.requires) == 0 and self.status == "Ready":
            self.status = "Starting"
       
        #Block with prerequisites that are incomplete
        elif len(self.requires) > 0 and stats.all_complete(self.requires) == False:
            self.status = "Waiting"
           
        #Block with prerequisites that are complete and was waiting, then start
        elif len(self.requires) > 0 and stats.all_complete(self.requires) == True and self.status == "Waiting":
            self.status = "Starting"
            self.start_day = current_day


    #Start the bloack and set the planned end day
    def __update_block__ (self, current_day):
        if self.status == "Starting":
            self.status = "Running"
            self.end_day = self.start_day + self.duration

            #If the block is market then set the end day to the remiaing days of patent
            if self.name == "Market":
                self.duration = 6570 - self.start_day
                self.end_day = self.start_day + self.duration
            

        #Update the running block with the worked time and accrued cost
        if self.status == "Running" and self.worked_days < self.duration:
            self.worked_days = self.worked_days + 1
            self.accrued_cost = self.daily_rate *  self.worked_days 


    def __end_block__ (self, current_day):

        if self.status == "Running" and self.worked_days == self.duration:
            self.worked_days = self.worked_days
            self.status = "Complete"
            self.end_day = current_day

            # Determine if the block was successful.
            success = hist_prob.prob_success (self.name)
            if success == True:
                self.status = "Complete"
            elif success == False:
                self.status = "Failed"


    def __del__(self):
        pass

# Activities are created when the task starts and added to the task activities
class activity:

    _registry = [] # create a register of objects that we can iterate over

    def __init__(self, id, name, status, start_day, duration):
        self._registry.append(self) #Add the newly created object to the register
        self.id = id
        self.name = name
        self.status = status
        self.start_day = start_day
        self.duration = duration

    def __del__(self):
        pass


class iteration:
    _registry = [] # create a register of objects that we can iterate over

    def __init__ (self, id, iteration, total_cost, status):
        self._registry.append(self) #Add the newly created object to the register
        self.id = id
        self.iteration = iteration
        self.total_cost = total_cost
        self.status = status

class Clock:
    _registry = [] # create a register of objects that we can iterate over

    def __init__(self, id, name, start_day, duration, total_iterations, current_iteration):
        self._registry.append(self) #Add the newly created object to the register
        self.id = id
        self.name = name
        self.start_day = start_day
        self.duration = duration
        self.total_iterations = total_iterations
        self.current_iteration = current_iteration

