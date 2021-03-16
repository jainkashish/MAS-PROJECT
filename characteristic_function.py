import itertools


class Characteristic:
    def __init__(self, n):
        self.n = n  # no. of agents
        self.chf_table = {}  # Characteristic function table

    # returns all subsets from (0,n)
    def getSubsets(self):
        num = []  # stores id of each agent
        for x in range(0, self.n):
            num.append(x)
        for t in range(0, self.n):
            # itertools.combinations returns tuple
            for x in set(itertools.combinations(num, t+1)):
                self.chf_table[x] = 0  # intially all the values are 0

    # returns the characteristic function table
    def generate_ch_function(self):
        self.getSubsets()  # it generates all subsets
        # Example 1
        self.chf_table[(0,)] = 2
        self.chf_table[(1,)] = 3
        self.chf_table[(2,)] = 5
        self.chf_table[(0, 1)] = 7
        self.chf_table[(1, 2)] = 4
        self.chf_table[(0, 2)] = 6
        self.chf_table[(0, 1, 2)] = 5
        #answer is (0,1), (2)

        # Example 2
        # self.chf_table[(0,)] = 1
        # self.chf_table[(1,)] = 2
        # self.chf_table[(2,)] = 3
        # self.chf_table[(0, 1)] = 3
        # self.chf_table[(1, 2)] = 4
        # self.chf_table[(0, 2)] = 5
        # self.chf_table[(0, 1, 2)] = 6

        # answer is (0),(1),(2)

        # Example 3
        # self.chf_table[(0,)] = 1
        # self.chf_table[(1,)] = 2
        # self.chf_table[(2,)] = 2
        # self.chf_table[(0, 1)] = 4
        # self.chf_table[(0, 2)] = 3
        # self.chf_table[(1, 2)] = 4
        # self.chf_table[(0, 1, 2)] = 6

        # answer is (0),(1),(2) / (0,1,2)

        # for key, val in self.chf_table.items():
        #     sum = 0
        #     for x in key:
        #         sum += x
        #     self.chf_table[key] = sum
        # for key, val in self.chf_table.items():
        #     print(key)
        #     print(val)
        return self.chf_table
