import classes
import model
import stats
import fileIO
import statistics
import results


#Model Parameters
Clock_id = 1
Clock_name = "Clock 1"
Clock_start_day = 1
Patent_protection = 18*365 # years
Simulation_iterations = 500 # number of simulations
Starting_iteration = 0 # do not change
View_iterations = True # See simulation progress
Write_iteration_list = True
Write_block_detail = False

#Iteration Settings
Iteration_ID = "MC1"
Starting_iteration = 0
Initial_cost = 0
Iteration_Status = "Ready"



#Setup the montecarlo simulation
#create_clock(id, name, start_day, duration, total_iterations, current_iteration):

s = model.create_clock(Clock_id,Clock_name, Clock_start_day, Patent_protection, Simulation_iterations, Starting_iteration)

# current_iteration = model.Clock.current_iteration
total_iterations = range(s.total_iterations)
duration = range(s.duration)

#Create an iteration object
iteration = classes.iteration(Iteration_ID, Starting_iteration, Initial_cost, Iteration_Status)
# print (iteration)


data5 = str(("IterationName", "IterationID", "TotalCost", "DevelopmentProgress"))
data6 = str(data5).replace('(','').replace(')','').replace('\'','').replace('\"','').replace(' ','')
file_name5 = "Iteration_List.csv"

fileIO.write_to_file (file_name5, data6)


for i in total_iterations:

    iteration.iteration = i

    #create the model
    model.create_model()

    data3 = str(("Iteration ID", "Iteration", "Current Day", "Name", "Start Day", "Duration", "End Day", "`Status", "Worked Days", "Daily Rate", "Accrued Cost"))
    data4 = str(data3).replace('(','').replace(')','').replace('\'','').replace('\"','')

    if Write_block_detail == "True":
        fileIO.write_to_file ("Block_Detail.csv",data4)


    for s in duration:

        # print (s)
        iteration_status,block_name = stats.update_blocks (s, iteration.id, iteration.iteration, Write_block_detail)
        # print (iteration_status)
        if iteration_status == "Failed":
                # print ("Simulation ended due to phase failure")
                iteration.status = (block_name + "_failure")
                break 

        iteration.status = "Development_success"


    #print ("--")
    #print ("*** Simulation Summary ***")
    #print ("--")
    #print ("*** Block List ***")
    for block in classes.block._registry:
            # print (block.name)
            data = iteration.id, iteration.iteration, block.name
            data2 = str(data).replace('(','').replace(')','').replace('\'','').replace('\"','').replace(' ','')
            file_name = "Block_List.csv"
            #fileIO.write_to_file (file_name, data2)

    #print ("--")
    #print ("*** Activity List ***")
    for act in classes.activity._registry:
            # print (act.name, act.start_day, act.duration)
            data = iteration.id, iteration.iteration, act.name, act.start_day, act.duration
            data2 = str(data).replace('(','').replace(')','').replace('\'','').replace('\"','')
            file_name = "Activity_List.csv"
            #fileIO.write_to_file (file_name, data2)


    #print ("--")
    #print ("End of Iteration - ", i)
  
    for itr in classes.iteration._registry:
            #print (itr.id, itr.iteration, itr.total_cost)

            itr.total_cost = sum(b.accrued_cost for b in classes.block._registry)

            data = itr.id,itr.iteration,itr.total_cost,iteration.status
            data2 = str(data).replace('(','').replace(')','').replace('\'','').replace('\"','').replace('\"','').replace(' ','')
            file_name = "Iteration_List.csv"
            if View_iterations == True:
                print (data2)
            if Write_iteration_list == True:
                fileIO.write_to_file (file_name, data2)

# visualisation.create_visualisation()
results.create_simulation_histogram()