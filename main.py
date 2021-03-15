import node
import characteristic_function
import find_coalition

if __name__ == "__main__":
    n = int(input("Enter Number of Nodes"))
    nodes = []  # it stores the information about n nodes
    for x in range(0, n):
        nodes.append(node.Node(x))

    v = characteristic_function.characteristic_fun(n)
    # x = find_coalition.find_optimal_coalition(n)

# for i in x:
#     for j in i:
#         print(j)
