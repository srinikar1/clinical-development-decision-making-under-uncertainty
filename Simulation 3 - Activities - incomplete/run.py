import classes
import model
import stats
import fileIO
import statistics
import visualisation


#delete the data file

# fileIO.remove_file("/Users/srinivaskarri/Desktop/Python examples/Clinical # Trial Simulation/Activity_List.csv")
# fileIO.remove_file("/Users/srinivaskarri/Desktop/Python examples/Clinical # Trial Simulation/Block_Detail.csv")
# fileIO.remove_file("/Users/srinivaskarri/Desktop/Python examples/Clinical Trial Simulation/Block_List.csv")
# fileIO.remove_file("/Users/srinivaskarri/Desktop/Python examples/Clinical Trial Simulation/Iteration_List.csv")


#Setup the montecarlo simulation
s = model.create_clock()

# current_iteration = model.Clock.current_iteration
total_iterations = range(s.total_iterations)
duration = range(s.duration)

#Create an iteration object
iteration = classes.iteration("MC1", 0, 0)
# print (iteration)


for i in total_iterations:

    iteration.iteration = i

    #create the model
    model.create_model()

    data3 = str(("Iteration ID", "Iteration", "Current Day", "Name", "Start Day", "Duration", "End Day", "`Status", "Worked Days", "Daily Rate", "Accrued Cost"))

    data4 = str(data3).replace('(','').replace(')','').replace('\'','').replace('\"','')

    fileIO.write_to_file ("Block_Detail.csv",data4)


    for s in duration:

        # print (s)
        stats.update_blocks (s, iteration.id, iteration.iteration)

    #print ("--")
    #print ("*** Simulation Summary ***")
    #print ("--")
    #print ("*** Block List ***")
    for block in classes.block._registry:
            # print (block.name)
            data = iteration.id, iteration.iteration, block.name
            data2 = str(data).replace('(','').replace(')','').replace('\'','').replace('\"','')
            file_name = "Block_List.csv"
            fileIO.write_to_file (file_name, data2)

    #print ("--")
    #print ("*** Activity List ***")
    for act in classes.activity._registry:
            # print (act.name, act.start_day, act.duration)
            data = iteration.id, iteration.iteration, act.name, act.start_day, act.duration
            data2 = str(data).replace('(','').replace(')','').replace('\'','').replace('\"','')
            file_name = "Activity_List.csv"
            fileIO.write_to_file (file_name, data2)


    #print ("--")
    #print ("End of Iteration - ", i)
  

    for itr in classes.iteration._registry:
            #print (itr.id, itr.iteration, itr.total_cost)

            itr.total_cost = sum(b.accrued_cost for b in classes.block._registry)

            data = itr.id, itr.iteration, itr.total_cost
            data2 = str(data).replace('(','').replace(')','').replace('\'','').replace('\"','')
            file_name = "Iteration_List.csv"
            fileIO.write_to_file (file_name, data2)

visualisation.create_visualisation()