import classes
import model
import stats
import fileIO
import results
import pandas as pd




#Model Parameters
Clock_id = 1
Clock_name = "Clock 1"
Clock_start_day = 1
Patent_protection = 18*365 # years
Simulation_iterations = 1 # number of simulations
Write_block_list = False # This dramatically slows down the simulation, leave to False
View_iteration_progress = True

#Iteration Settings
Iteration_ID = "MC1"
Starting_iteration = 0
Initial_cost = 0
Iteration_Status = "Ready"

#Setup globals
df_iteration_list = pd.DataFrame(columns=["IterationName", "IterationID", "TotalCost", "DevelopmentProgress"])
df_block_list = pd.DataFrame(columns=["Iteration ID", "Iteration", "Current Day", "Name", "Start Day", "Duration", "End Day", "`Status", "Worked Days", "Daily Rate", "Accrued Cost"])
df_block_list_gantt = pd.DataFrame(columns=["Iteration","block.id","block.name", "block.status", "block.start_day", "block.duration", "block.end_day", "block.daily_rate", "block.accrued_cost"])
df_cash_flow_list = pd.DataFrame(columns=["Iteration","Day","Total accrued cost", "Cash flow"]) 


#Setup the montecarlo simulation
#create_clock(id, name, start_day, duration, total_iterations, current_iteration):

s = model.create_clock(Clock_id,Clock_name, Clock_start_day, Patent_protection, Simulation_iterations, Starting_iteration)

# current_iteration = model.Clock.current_iteration
total_iterations = range(s.total_iterations)
duration = range(s.duration)

#Create an iteration object
iteration = classes.iteration(Iteration_ID, Starting_iteration, Initial_cost, Iteration_Status)
# print (iteration)

for i in total_iterations:

    iteration.iteration = i
    


    #create the model
    model.create_model()

    for s in duration:

        #find total cost at the start of the duration
        for itr in classes.iteration._registry:
            itr.total_cost_start = sum(b.accrued_cost for b in classes.block._registry)
            
        
        iteration_status,block_name = stats.update_blocks (s, iteration.id, iteration.iteration, df_block_list, Write_block_list)

       
        # print (iteration_status)
        if iteration_status == "Failed":
                iteration.status = (block_name + "_failure")
                break 
        iteration.status = (block_name + "_success")

        #calculate total cost cost at the end of the duration

        for itr in classes.iteration._registry:
            itr.total_cost = sum(b.accrued_cost for b in classes.block._registry)

        #calculate the cashflow
        cashflow = itr.total_cost - itr.total_cost_start


        df_cash_flow_list.loc[len(df_cash_flow_list.index)] = [i,s,itr.total_cost, cashflow]

        if View_iteration_progress == True:
            print("Iteration - ", i , "Day - ", s) 



    for block in classes.block._registry:
        if block.worked_days > 0:
                df_block_list_gantt.loc[len(df_block_list_gantt.index)] = [iteration.iteration, block.id,block.name, block.status, block.start_day, block.duration, block.end_day, block.daily_rate, block.accrued_cost]

    #for act in classes.activity._registry:
            # print (act.name, act.start_day, act.duration)
            #data = iteration.id, iteration.iteration, act.name, act.start_day, act.duration
            #data2 = str(data).replace('(','').replace(')','').replace('\'','').replace('\"','')
            #file_name = "Activity_List.csv"
            #fileIO.write_to_file (file_name, data2)

    for itr in classes.iteration._registry:
            itr.total_cost = sum(b.accrued_cost for b in classes.block._registry)
            df_iteration_list.loc[len(df_iteration_list.index)] = [itr.id,itr.iteration,itr.total_cost,iteration.status]

# visualisation.create_visualisation()
results.create_simulation_histogram(df_iteration_list)
results.create_gantt_chart(df_block_list_gantt)
results.create_simulation_summary(df_iteration_list)
results.create_cash_flow_chart(df_cash_flow_list)
fileIO.df_to_csv(df_iteration_list,'Iteration_List.csv')


