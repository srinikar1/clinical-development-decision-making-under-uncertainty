class Node:
    _registry = [] # create a register of objects that we can iterate over

    def __init__(self, name, duration, cost, success):
        self._registry.append(self) #Add the newly created object to the register
        self.name = name
        self.duration = duration
        self.cost = cost
        self.success = success
        #self.connected_nodes = []

    #def connect_to(self, other_node):
        #self.connected_nodes.append(other_node)

class Connection:
    _registry = [] # create a register of objects that we can iterate over
    def __init__(self, name):
        self._registry.append(self) #Add the newly created object to the register
        self.name = name
        self.input_node = []
        self.output_node = []


    def connection(self, input_node, output_node):
        self.name = self
        self.input_node.append(input_node)
        self.output_node.append(output_node)



# create decision nodes
Market = Node("Market", "", "", "")
Phase3 = Node("Phase 3","", "", "")
Phase2 = Node("Phase2","", "", "")
Phase1 = Node("Phase 1","", "", "")
Preclinical = Node ("Preclinical","", "", "")


#Create connection types
Requires = Connection("Requires")

#Create the model
Requires.connection(Market, Phase3)
Requires.connection(Phase3, Phase2)
Requires.connection(Phase2, Phase1)
Requires.connection(Market, Preclinical)













# connect node1 to node2
#node2.connect_to(node1)
# check if node1 is connected to node2
#print(node2 in node1.connected_nodes)  # True






'''
In this example, the Node class has an attribute connected_nodes, which is a list that stores the nodes to which the current node is connected. The class also has a connect_to() method, which is used to connect the current node to another node. The method takes one parameter, which is the other node, and appends it to the connected_nodes list.

In the example, we created two nodes, node1 and node2, and connected node1 to node2. We then checked if node1 is connected to node2 and it returns true.

This is a simple example of how you can use an attribute and a method to model the relationship between two objects. You can also add more functionality to the class, such as a method to disconnect nodes, or to check if two nodes are connected to each other.

Another approach to model this relationship would be to use Graph data structure where edges between nodes represents the relationship.

You can also use a library such as networkx which provides a lot of functionalities related to graph data structure.

'''