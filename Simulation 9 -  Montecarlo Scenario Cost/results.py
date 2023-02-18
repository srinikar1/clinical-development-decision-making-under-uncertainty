import matplotlib.pyplot as plt
import csv
import numpy
import pandas as pd
import fileIO
import statistics
from scipy import stats


def create_simulation_histogram(df_iteration_list):

    df = df_iteration_list
    df = df.set_index('IterationID')

    df.TotalCost = df.TotalCost // 1000000

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

    print (A)

# Example located at https://www.statology.org/pandas-histogram-by-group/

    bins = numpy.linspace (min, max, 50)

    fig, [(ax0), (ax1)] = plt.subplots(nrows = 2,ncols = 1)
    fig.suptitle('Scenario Simulation Cost Distribution', fontsize=12)


    # plt.legend(loc='upper right')
    ax0.hist(A, bins, alpha=0.5, label='Market success')
    ax0.hist(B, bins, alpha=0.5, label='Preclinical failure')
    ax0.hist(C, bins, alpha=0.5, label='Phase 1 failure')
    ax0.hist(D, bins, alpha=0.5, label='Phase 2 failure')
    ax0.hist(E, bins, alpha=0.5, label='Phase 3 failure')
    ax0.hist(F, bins, alpha=0.2, label='Overall')
    ax0.tick_params(left = False, bottom = False)
    ax0.legend(fontsize=8, loc='center left')
    ax0.set_xlabel('Project Cost', fontsize=10)
    ax0.set_ylabel('Frequency', fontsize=10)

    ax1.hist(A, bins, alpha=0.5, label='Market success')
    ax1.tick_params(left = False, bottom = False)
    ax1.legend(fontsize=8, loc='center left')
    ax1.set_xlabel('Project Cost', fontsize=10)
    ax1.set_ylabel('Frequency', fontsize=10)
    
    mu, sigma = stats.norm.fit(A)
    best_fit_line = stats.norm.pdf(bins, mu, sigma)
    ax1.plot(bins, best_fit_line)
    
    print (mu)
    print (sigma)
    print(bins)




    plt.tight_layout()

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
    plt.barh(y=df['block.name'], width=df['block.worked_days'], left=df['block.start_day'])
    plt.savefig('Gantt Chart - Iteration 0.png')
    plt.close()
    fileIO.df_to_csv(df_block_list_gantt,'Block_List_Gantt - Iteration 0.csv')
    pass


def create_cash_flow_chart(df_cash_flow_list):


    df = df_cash_flow_list


    
# https://stackoverflow.com/questions/59232073/scatter-plot-with-3-variables-in-matplotlib


#Now create the yearly cashflow chart

    #print("xx",df)

    fileIO.df_to_csv(df,"Daily_Cash_Flow_List - Iteration 0.csv")

    N = 365

    df= df.groupby(df.index // N).sum()

    #rename the column
    df.rename(columns = {'Day':'Year'}, inplace = True)
    #df.Iteration = df.Iteration // N
    df.Year = df.index
    df["Cash flow"] = df["Cash flow"]
    df=df.drop("Iteration total cost", axis=1)
    #print (df)
    fileIO.df_to_csv(df,"Yearly_Cash_Flow_List - Iteration 0.csv")
    
    df.plot.scatter(x="Year",y=["Cash flow"])
    plt.ylabel('Cash flow, $')
    plt.xlabel('Year')
    plt.savefig('Yearly Cash Flow - Iteration 0.png')
    plt.close()


    pass










    pass
