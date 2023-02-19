import pandas as pd

#Setup dataframes


def create_model_dataframes():
    
    df_iteration_list = pd.DataFrame(columns=["IterationName", "IterationID", "TotalCost", "DevelopmentProgress"])
    df_block_list = pd.DataFrame(columns=["Iteration ID", "Iteration", "Current Day", "Name", "Start Day", "Duration", "End Day", "`Status", "Worked Days", "Progress", "Daily Rate", "Accrued Cost"])
    df_block_list_gantt = pd.DataFrame(columns=["Iteration","block.id","block.name", "block.status", "block.start_day", "block.duration", "block.end_day", "block.worked_days", "block.prgress", "block.daily_rate", "block.accrued_cost"])
    df_cash_flow_list = pd.DataFrame(columns=["Iteration","Day","Iteration total cost", "Cash flow"])
    
    
    return (df_iteration_list, df_block_list,df_block_list_gantt,df_cash_flow_list)
