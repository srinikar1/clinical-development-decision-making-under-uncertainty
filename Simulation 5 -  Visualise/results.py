import matplotlib.pyplot as plt
import csv
import numpy
import pandas
import fileIO


def create_visualisation():

    with open('Iteration_List.csv', newline='') as csv_file:
        reader = csv.reader(csv_file, delimiter=',')
        Iteration_List = list(reader)
        # print(Iteration_List)


    x = [float(row[2]) for row in Iteration_List[2:]]
    # print (x)

    plt.hist(x, bins=200)
    plt.gca().set(title='Total Cost Distribution', ylabel='Frequency', xlabel='Total Cost');
    plt.show()


#Take this to the next level using this https://ajaytech.co/kde-plots/ using a probability distribution function


def create_simulation_histogram():

    df = pandas.read_csv('Iteration_List.csv')
    df = df.set_index('IterationID')
    print (df)

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


    A = df.loc[df['DevelopmentProgress'] == 'Development_success', 'TotalCost']
    B = df.loc[df['DevelopmentProgress'] == 'Preclinical_failure', 'TotalCost']
    C = df.loc[df['DevelopmentProgress'] == 'Phase1_failure', 'TotalCost']
    D = df.loc[df['DevelopmentProgress'] == 'Phase2_failure', 'TotalCost']
    E = df.loc[df['DevelopmentProgress'] == 'Phase3_failure', 'TotalCost']
    F = df['TotalCost']


# Example located at https://www.statology.org/pandas-histogram-by-group/

    bins = numpy.linspace (min, max, 50)

    # plt.legend(loc='upper right')
    plt.hist(A, bins, alpha=0.5, label='Development success')
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





    