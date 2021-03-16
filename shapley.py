class Shapley:

    def __init__(self, n, optimal_coalition, characteristic_function):
        self.n = n  # the number of agents
        self.payoff = {}  # map to store individual payoff of agents within a coalition
        # optimal set of coalitions obtained via distributed algorithm
        self.optimal_coalition = optimal_coalition
        self.ch_table = characteristic_function

    # this returns the value of factorial of x
    def factorial(self, x):
        return 1 if (x == 1 or x == 0) else x * self.factorial(x - 1)

    # calculates the shapley value of an agent in cur_coalition
    def calc_shapley(self, agent, cur_coalition):
        # Example
        # 0 1 2 3
        # {0,1,2} {3}
        # shapley( {0,1,2} , 0 ) = v(0) - v() + v(0,1) - v(1) + v(0,2) - v(2) + v(0,1,2) - v(1,2)
        num = len(cur_coalition)  # the number of agents in cur_coalition
        # factorial of the number of agents in cur_coalition
        f_num = self.factorial(num)
        global total
        total = 0
        for coalition, ch_val in self.ch_table.items():
            global d
            d = set(coalition)  # typecasting tuple to set
            if agent in d:
                d.remove(agent)
                # rem is the chf value excluding the agent
                rem = self.ch_table[tuple(d)]
                # print("agent is ", agent)
                # print("val is ", ch_val)
                # print("rem is ", rem)
                total += ch_val - rem  # val is the chf value including the agent
        return total/f_num

    # it distributes the payoff within a coalition of agent
    def distribute_payoff(self):
        # for each agent in each optimal coalition, calc_shapley function is called
        for cur_coalition in self.optimal_coalition:
            for agent in cur_coalition:
                self.payoff[agent] = self.calc_shapley(agent, cur_coalition)

    # prints the payoff table
    def print_payoff_table(self):
        print("Payoff table: ")
        for coalition, ch_val in self.payoff.items():
            print("For agent ", coalition)
            print("Payoff is ", ch_val)
