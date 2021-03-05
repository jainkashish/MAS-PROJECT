from node import *
from characteristic_function import *
from find_coalition import *

if __name__ == "__main__":
    n = int(input("Enter Number of Nodes"))
    nodes = []  # it stores the information about n nodes
    for x in range(0, n):
        nodes.append(Node(x))  
        
    v = characteristic_fun(n)
