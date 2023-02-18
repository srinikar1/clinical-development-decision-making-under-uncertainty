import classes
import model
import stats
import fileIO
import results
import pandas as pd



#Setup globals
df_iteration_list = pd.DataFrame(columns=["IterationName", "IterationID", "TotalCost", "DevelopmentProgress"])
df_block_list = pd.DataFrame(columns=["Iteration ID", "Iteration", "Current Day", "Name", "Start Day", "Duration", "End Day", "`Status", "Worked Days", "Daily Rate", "Accrued Cost"])
df_block_list_gantt = pd.DataFrame(columns=["Iteration","block.id","block.name", "block.status", "block.start_day", "block.duration", "block.end_day", "block.worked_days",  "block.daily_rate", "block.accrued_cost"])
df_cash_flow_list = pd.DataFrame(columns=["Iteration","Day","Iteration total cost", "Cash flow"]) 


#Setup the montecarlo simulation
#create_clock(id, name, start_day, duration, total_iterations, current_iteration):
s = model.create_clock(model.Clock_id,model.Clock_name, model.Clock_start_day, model.Patent_protection, model.Simulation_iterations, model.Starting_iteration)

# current_iteration = model.Clock.current_iteration
total_iterations = range(s.total_iterations)
duration = range(s.duration)

#Create an iteration object
iteration = classes.iteration(model.Iteration_ID, model.Starting_iteration, model.Initial_cost, model.Iteration_Status)
# print (iteration)

for i in total_iterations:

    iteration.iteration = i

    model.create_model()

    for s in duration:

        #find total cost before blocks are updated
        #for itr in classes.iteration._registry:
        total_cost_start = sum(b.accrued_cost for b in classes.block._registry)
            
        iteration_status,block_name = stats.update_blocks (s, iteration.id, iteration.iteration, df_block_list, model.Write_block_list)
       
        # print (iteration_status)
        if iteration_status == "Failed":
                iteration.status = (block_name + "_failure")
                break 
        iteration.status = (block_name + "_success")
        #iteration.status = ("Interation_in_progress")

        #calculate total cost after blocks have been updated
        #for itr in classes.iteration._registry:
        total_cost_end = sum(b.accrued_cost for b in classes.block._registry)

        #calculate the cashflow
        cashflow = total_cost_end - total_cost_start

        for itr in classes.iteration._registry:
            itr.total_cost = itr.total_cost + cashflow

        if i == 0:    
            df_cash_flow_list.loc[len(df_cash_flow_list.index)] = [i,s, itr.total_cost, cashflow]

        if model.View_iteration_progress == True:
            print("Iteration - ", i , "Day - ", s) 

    #iteration.status = ("Iteration_complete")


    for block in classes.block._registry:
        if i == 0:
            df_block_list_gantt.loc[len(df_block_list_gantt.index)] = [iteration.iteration, block.id,block.name, block.status, block.start_day, block.duration, block.end_day, block.worked_days, block.daily_rate, block.accrued_cost]

    for itr in classes.iteration._registry:
            itr.total_cost = sum(b.accrued_cost for b in classes.block._registry)
            df_iteration_list.loc[len(df_iteration_list.index)] = [itr.id,itr.iteration,itr.total_cost,iteration.status]


results.create_simulation_histogram(df_iteration_list)
results.create_gantt_chart(df_block_list_gantt)
results.create_simulation_summary(df_iteration_list)
results.create_cash_flow_chart(df_cash_flow_list)
fileIO.df_to_csv(df_iteration_list,'Iteration_List.csv')



