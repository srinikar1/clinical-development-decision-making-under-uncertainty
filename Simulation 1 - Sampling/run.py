from datetime import datetime, timedelta
import classes
import model



s = model.Scenario

start_day = model.Scenario.start_day
end_day = model.Scenario.start_day + model.Scenario.duration


# Iterate over the hours between the start and end date
current_day = start_day
while current_day < end_day:

    for b in classes.block._registry:
            classes.block.__update_end_day__(b, current_day)
            classes.block.__update_status__(b,current_day)
            print (current_day, b.name, b.start_day, b.duration, b.end_day, b.status, b.worked_days, b.daily_rate, b.accrued_cost)

    current_day = current_day
    current_day = current_day + 1
        
        
        
    
 

