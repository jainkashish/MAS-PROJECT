import node
import characteristic_function
import coalition
import shapley

if __name__ == "__main__":

    n = int(input("Enter Number of Nodes"))
    nodes = []  # it stores the information about n nodes

    # list of Node class objects for all agents
    for x in range(0, n):
        nodes.append(node.Node(x))

    # Implementing coalition formation algorithm

    # Step 1: Create characteristic function
    # creating object of Characteristic function class
    ch_fun_obj = characteristic_function.Characteristic(n)
    ch_function = ch_fun_obj. generate_ch_function()
    ch_fun_obj.print_ch_table()

    # Step 2: Finding the optimal coalition using the distributed algorithm
    # creating object of Coalition class
    coalition_obj = coalition.Coalition(n, ch_function)
    coalition_obj.find_optimal_coalition()
    optimal_coalition = coalition_obj.final_coalition
    coalition_obj.print_optimal_coalition()

    # Step 3: Distribute the payoff to agents within each coalition
    # creating object of Shapley class
    shapley_obj = shapley.Shapley(n, optimal_coalition, ch_function)
    shapley_obj.distribute_payoff()
    payoff = shapley_obj.payoff
    shapley_obj.print_payoff_table()
