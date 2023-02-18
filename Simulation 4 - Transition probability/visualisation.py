import matplotlib.pyplot as plt
import csv


def create_visualisation():

    with open('Iteration_List.csv', newline='') as csv_file:
        reader = csv.reader(csv_file, delimiter=',')
        Iteration_List = list(reader)
        # print(Iteration_List)


    x = [float(row[2]) for row in Iteration_List[0:]]
    # print (x)

    plt.hist(x, bins=50)
    plt.gca().set(title='Total Cost Distribution', ylabel='Frequency', xlabel='Total Cost');
    plt.show()

