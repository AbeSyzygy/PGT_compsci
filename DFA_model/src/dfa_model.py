class dfa: 
    def __init__(self, Q, q, sigma, d, F):
        self.Q = Q
        self.q = q
        self.sigma = sigma
        self.d = d
        self.F = F

        self.is_accept = False

    def get_current_state(self, current_state, char):
        return self.d[(self.Q[current_state], char)]

    def read_string(self, input_string):
        self.is_accept = False

        current_state = self.q # this is still an index
        for char in input_string:
            print(self.Q[current_state] + "(" + char + ") --> ", end="")
            if char not in self.sigma:
                print("N/A \n\'" + char + "\' is not a part of this automaton's alphabet")
                self.is_accept = False
                return False
            current_state = self.get_current_state(current_state, char)
            print(self.Q[current_state])

        if current_state in self.F:
            self.is_accept = True
            return True

def dfa_read_string(dfa, string):
    
    dfa_accept = dfa.read_string(string)
    if dfa_accept:
        print("______\n\nACCEPT\n______\n")
    else:
        print("______\nREJECT\n______\n")

def main():

    # Assign dfa constructor arguments for...:

    # //////// dfa_week1_ex2_1: //////// 

    # Q = ["1", "2", "3", "4"]
    # q = 1
    # sigma = ["a", "b"]
    # d = {
    #     ("1", "a"):1,   # --> 2
    #     ("1", "b"):3,   # --> 4

    #     ("2", "a"):2,   # --> 3
    #     ("2", "b"):0,   # --> 1

    #     ("3", "a"):3,   # --> 4
    #     ("3", "b"):1,   # --> 2

    #     ("4", "a"):3,   # --> 4
    #     ("4", "b"):3    # --> 4
    # }
    # F = [1]

    # //////////////////////////////////

    # //////// dfa_week1_ex2_2: //////// 

    # Q = ["q", "p", "r"]
    # q = 0
    # sigma = ["0", "1", "2"]
    # d = {
    #     ("q", "0"):0,   # --> q
    #     ("q", "1"):1,   # --> p
    #     ("q", "2"):2,   # --> r

    #     ("p", "0"):1,   # --> p
    #     ("p", "1"):2,   # --> r
    #     ("p", "2"):0,   # --> q

    #     ("r", "0"):2,   # --> r
    #     ("r", "1"):0,   # --> q
    #     ("r", "2"):1,   # --> p
    # }
    # F = [0]

    # //////////////////////////////////

    # //////// dfa_week1_ex3_1: //////// 

    Q = ["q_0", "X", "\\", "\\#w", "\\#w#", "\\#w#\\"]
    q = 0
    sigma = ["\\", "#", "a", "b"]
    d = {
        ("q_0", "\\"):      2,  # 0 --> \
        ("q_0", "#"):       1,  # 0 --> X
        ("q_0", "a"):       1,  # 0 --> X
        ("q_0", "b"):       1,  # 0 --> X

        ("X", "\\"):        1,  # 1 --> X
        ("X", "#"):         1,  # 1 --> X
        ("X", "a"):         1,  # 1 --> X
        ("X", "b"):         1,  # 1 --> X

        ("\\", "\\"):       1,  # 2 --> X
        ("\\", "#"):        3,  # 2 --> \#w
        ("\\", "a"):        1,  # 2 --> X
        ("\\", "b"):        1,  # 2 --> X

        ("\\#w", "\\"):     1,  # 3 --> X
        ("\\#w", "#"):      4,  # 3 --> \#w#
        ("\\#w", "a"):      3,  # 3 --> \#w
        ("\\#w", "b"):      3,  # 3 --> \#w

        ("\\#w#", "\\"):    5,  # 4 --> \#w#\
        ("\\#w#", "#"):     1,  # 4 --> X
        ("\\#w#", "a"):     1,  # 4 --> X
        ("\\#w#", "b"):     1,  # 4 --> X

        ("\\#w#\\", "\\"):  1,  # 5 --> X
        ("\\#w#\\", "#"):   1,  # 5 --> X
        ("\\#w#\\", "a"):   1,  # 5 --> X
        ("\\#w#\\", "b"):   1,  # 5 --> X
    }
    F = [5]

    # //////////////////////////////////


    # Automaton sequence stored for formal definition
    M = [Q, q, sigma, d, F]


    dfa_model = dfa(M[0], M[1], M[2], M[3], M[4])
    
    STRING = "\\#abbabaaaabkbbabababaabaabbba#\\"

    dfa_read_string(dfa_model, STRING)

main()