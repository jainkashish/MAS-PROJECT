class Coalition:

    def __init__(self, n, ch_function):
        self.n = n  # no. of agents n
        self.final_coalition = []  # stores the final sets of coalition
        self.discard = set()  # stores the agents which is now the part of final coalition
        self.chf_table = ch_function  # characteristic function table

    # forms the final optimal coalition
    def find_optimal_coalition(self):
        # when an agent forms a coalition, it is added to the discard set
        # the loop runs until all the agents become part of some coalition
        while(len(self.discard) != self.n):
            self.find_coalition()

    # it compares the optimal coalitions of each agent i and returns the most optimal among them
    def find_coalition(self):
        global payoff
        global optimal
        payoff = 0
        optimal = set()
        for x in range(self.n):
            if x in self.discard:
                continue
            # all the agents broadcast their most optimal coalition and the most optimal among them is chosen
            t_payoff, t_optimal = self.calculate_si(x)
            if (t_payoff > payoff):
                payoff = t_payoff
                optimal = t_optimal
        # all the elements which have become part of this coalition are added to the discard set
        for x in optimal:
            self.discard.add(x)
        # join the most optimal coalition to the final optimal coalition
        self.final_coalition.append(optimal)

    # gives the most optimal coalition and its value for an agent i
    def calculate_si(self, i):
        global payoff  # stores the payoff of the optimal coalition
        global optimal  # stores the most optimal coalition for the agent i
        payoff = 0
        optimal = set()
        # print("for i ", i)
        # iterate through all coalitions that include i
        for coalition, _ in self.chf_table.items():
            d = set(coalition)  # typecasting tuple to set
            if i in coalition and len(d.intersection(self.discard)) == 0:
                if (self.chf_table[coalition]/(len(coalition)) > payoff):
                    optimal = coalition
                    payoff = self.chf_table[coalition]/len(coalition)

        # print("the payoff is ", payoff)
        # print("the optimal is ", optimal)
        return payoff, optimal

    # it prints the optimal coalition table
    def print_optimal_coalition(self):
        print("Final optimal coalition: ")
        for coalition in self.final_coalition:
            print(coalition)
        print('\n')
