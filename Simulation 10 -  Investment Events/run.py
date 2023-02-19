import dataframes
import classes
import model
import stats
import fileIO
import results
import pandas as pd



View_iteration_progress = True
Write_block_list = False # This dramatically slows down the simulation, leave to False


df_iteration_list, df_block_list,df_block_list_gantt,df_cash_flow_list = dataframes.create_model_dataframes()
scenario = model.create_scenario()
clock = model.create_clock()


for iteration in range(clock.total_iterations):

    model.create_model() #initialise the task model

    for day in range(clock.duration):

        #find total cost before blocks are updated
        total_cost_start = sum(b.accrued_cost for b in classes.block._registry)
  
        #update all the blocks
        iteration_status,block_name = stats.update_blocks (day, scenario.id, scenario.scenario, df_block_list, Write_block_list)
       
        # STOP the iteration if the block has failed
        if iteration_status == "Failed":
                iteration.status = (block_name + "_failure")
                break 
        scenario.status = (block_name + "_success")
        #iteration.status = ("Interation_in_progress")

        #calculate total cost after blocks have been updated
        total_cost_end = sum(b.accrued_cost for b in classes.block._registry)

        #calculate the cashflow
        cashflow = total_cost_end - total_cost_start

        scenario.total_cost = scenario.total_cost + cashflow

        if scenario.scenario == 0:    #Create the cashflow list for only the first scenario
            df_cash_flow_list.loc[len(df_cash_flow_list.index)] = [iteration,day, scenario.total_cost, cashflow]

        if View_iteration_progress == True:
            print("Scenario", scenario.scenario, "Iteration", iteration , "Day", day) 


    for block in classes.block._registry:
        if iteration == 0: #only create the gantt chart for the first iteration
            df_block_list_gantt.loc[len(df_block_list_gantt.index)] = [scenario.scenario, block.id,block.name, block.status, block.start_day, block.duration, block.end_day, block.worked_days, block.progress, block.daily_rate, block.accrued_cost]


    for scr in classes.scenario._registry:
            scr.total_cost = sum(b.accrued_cost for b in classes.block._registry)
            df_iteration_list.loc[len(df_iteration_list.index)] = [scr.id,scr.scenario,scr.total_cost,scr.status]


results.create_simulation_histogram(df_iteration_list)
results.create_gantt_chart(df_block_list_gantt)
results.create_simulation_summary(df_iteration_list)
results.create_cash_flow_chart(df_cash_flow_list)
fileIO.df_to_csv(df_iteration_list,'Iteration_List.csv')