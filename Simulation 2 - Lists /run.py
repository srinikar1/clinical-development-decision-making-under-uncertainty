import classes
import model
import stats
import fileIO


s = model.Clock

start_day = model.Clock.start_day
end_day = model.Clock.start_day + model.Clock.duration

print ("simulation starting on", start_day)
print ("simulation ending on", end_day)

# Iterate over the hours between the start and end date
current_day = start_day

fileIO.write_to_file (str(("Current Day", "Name", "Start Day", "Duration", "End Day", "`Status", "Worked Days", "Daily Rate", "Accrued Cost", "Total Cost")).replace('(','').replace(')','').replace('\'','').replace('\"',''))

total_cost = 0
while current_day < end_day:
 
            
        for b in classes.block._registry:
            classes.block.__start_block__(b, current_day)
            classes.block.__update_block__(b, current_day)
            classes.block.__end_block__(b, current_day)

            total_cost = b.accrued_cost + total_cost
            
            data = current_day, b.name, b.start_day, b.duration, b.end_day, b.status, b.worked_days, b.daily_rate, b.accrued_cost, total_cost

            

            data2 = str(data).replace('(','').replace(')','').replace('\'','').replace('\"','')
            print (data2)
            fileIO.write_to_file (data2)
            

        current_day = current_day + 1



        
        
    
 

