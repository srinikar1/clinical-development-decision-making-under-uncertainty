import stats
import hist_durations
import hist_costs

class block:
    _registry = [] # create a register of objects that we can iterate over

    def __init__(self, id, name, status, start_day, duration, end_day, worked_days, daily_rate, accrued_cost, prerequisites):
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
        self.prerequisites = prerequisites
    
    def __update_end_day__(self,current_day):
        # self.duration = stats.sample_norm_dist(self.mean_duration,self.duration_sdv)
            self.end_day = self.start_day + self.duration

  
    def __update_status__(self,current_day):
        if current_day < self.start_day:
            self.status = "Waiting"
        elif current_day >= self.start_day and current_day < self.end_day:
            self.status = "Running"
            self.worked_days = self.worked_days + 1
            self.accrued_cost = self.worked_days * self.daily_rate
        elif current_day >= self.end_day:
            self.status = "Completed"


class Clock:
    def __init__(self, id, name, start_day, duration):
        self.id = id
        self.name = name
        self.start_day = start_day
        self.duration = duration

