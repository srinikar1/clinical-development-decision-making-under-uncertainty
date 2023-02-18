import matplotlib.pyplot as plt
import csv
import numpy
import pandas as pd
import fileIO


def create_simulation_histogram(df_iteration_list):

    df = df_iteration_list
    df = df.set_index('IterationID')

    max = df['TotalCost'].max()
    min = df['TotalCost'].min()
    var = df['TotalCost'].var()
    std = df['TotalCost'].std()
    iterations = df['TotalCost'].count()

    A = df.loc[df['DevelopmentProgress'] == 'Market_success', 'TotalCost']
    B = df.loc[df['DevelopmentProgress'] == 'Preclinical_failure', 'TotalCost']
    C = df.loc[df['DevelopmentProgress'] == 'Phase1_failure', 'TotalCost']
    D = df.loc[df['DevelopmentProgress'] == 'Phase2_failure', 'TotalCost']
    E = df.loc[df['DevelopmentProgress'] == 'Phase3_failure', 'TotalCost']
    F = df['TotalCost']


# Example located at https://www.statology.org/pandas-histogram-by-group/

    bins = numpy.linspace (min, max, 50)

    # plt.legend(loc='upper right')
    plt.hist(A, bins, alpha=0.5, label='Market success')
    plt.hist(B, bins, alpha=0.5, label='Preclinical failure')
    plt.hist(C, bins, alpha=0.5, label='Phase 1 failure')
    plt.hist(D, bins, alpha=0.5, label='Phase 2 failure')
    plt.hist(E, bins, alpha=0.5, label='Phase 3 failure')
    plt.hist(F, bins, alpha=0.2, label='Overall')

    plt.title('Simulated Development Cost')
    plt.xlabel('Total Cost')
    plt.ylabel('Frequency')
    #plt.xticks(color='w')
    #plt.yticks(color='w')
    plt.tick_params(left = False, bottom = False)

    plt.legend(title='Status')
    # plt.show()
    plt.savefig('Simulated Development Cost.png')
    plt.close()
    
def create_simulation_summary(df_iteration_list):
    df = df_iteration_list
    df = df.set_index('IterationID')
    max = df['TotalCost'].max()
    min = df['TotalCost'].min()
    var = df['TotalCost'].var()
    std = df['TotalCost'].std()
    iterations = df['TotalCost'].count()

    #print ("Total iterations - " + str(iterations))
    #print ("Max total cost - " + str(max))
    #print ("Min total cost - " +str(min))
    #print ("Variance total cost - " + str(var))
    #print ("Standard deviation total cost - " + str(std))

    data5 = str('Simulation iterations - ' + str(iterations))
    data1 = str('Max of total cost for simulation ' + str(max))
    data2 = str('Min of total cost for simulation ' + str(min))
    data3 = str('Variance of total cost for simulation ' + str(var))
    data4 = str('Standard Deviation of total cost for simulation ' + str(std))

# Perhaps the stats should be developed for each of the failures?


    fileIO.write_to_file ("Simulation_results.csv", data5)
    fileIO.write_to_file ("Simulation_results.csv", data1)
    fileIO.write_to_file ("Simulation_results.csv", data2)
    fileIO.write_to_file ("Simulation_results.csv", data3)
    fileIO.write_to_file ("Simulation_results.csv", data4)
    
    pass

#https://www.datacamp.com/tutorial/how-to-make-gantt-chart-in-python-matplotlib

def create_gantt_chart(df_block_list_gantt):
    df = df_block_list_gantt
    plt.barh(y=df['block.name'], width=df['block.duration'], left=df['block.start_day'])
    plt.savefig('Gantt Chart.png')
    plt.close()
    fileIO.df_to_csv(df_block_list_gantt,'Block_List_Gantt.csv')
    pass


def create_cash_flow_chart(df_cash_flow_list):
    df = df_cash_flow_list
    df.plot(x="Day", y=["Total accrued cost"])
    plt.ylabel('Total accrued cost')
    plt.xlabel('Day')
    plt.savefig('Daily cash flow.png')
    plt.close()
    fileIO.df_to_csv(df_cash_flow_list,"Daily_Cash_Flow_List.csv")
  
#Now create the yearly cashflow chart

    N = 365
    df_yearly_cash_flow_list = df.groupby(df.index // N).sum()
    df = df_yearly_cash_flow_list
    df.plot.bar(y=["Cash flow"])
    plt.ylabel('Cash flow')
    plt.xlabel('Year')
    plt.savefig('Yearly Cash Flow.png')
    plt.close()
    fileIO.df_to_csv(df_yearly_cash_flow_list,"Yearly_Cash_Flow_List.csv")
    pass










    pass
