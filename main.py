import node
import characteristic_function
import coalition

if __name__ == "__main__":
    n = int(input("Enter Number of Nodes"))
    nodes = []  # it stores the information about n nodes
    for x in range(0, n):
        nodes.append(node.Node(x))
    # creating object of Characteristic function class
    ch_fun_obj = characteristic_function.Characteristic(n)
    ch_function = ch_fun_obj. generate_ch_function()

    # creating object of Coalition class
    coalition_obj = coalition.Coalition(n, ch_function)
    coalition_obj.find_optimal_coalition()
