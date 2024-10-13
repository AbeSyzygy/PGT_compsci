class dfa: 
    def __init__(self, Q, q, sigma, d, F):
        self.Q = Q
        self.q = q
        self.sigma = sigma
        self.d = d
        self.F = F

    def get_current_state(self, current_state, char):
        return self.d[(self.Q[current_state], char)]

    def read_string(self, input_string):
        is_accept = False

        current_state = self.q # this is still an index
        for char in input_string:
            print(self.Q[current_state] + "(" + char + ") --> ", end="")
            if char not in self.sigma:
                print(char + "is not a part of alphabet")
                return False
            current_state = self.get_current_state(current_state, char)
            print(self.Q[current_state])

        if current_state in self.F:
            print()
            return True

def dfa_read_string(dfa, string):
    
    dfa_accept = dfa.read_string(string)
    if dfa_accept:
        print("ACCEPT")
    else:
        print("REJECT")

def main():

    # Assign dfa constructor arguments for:
    # //////// dfa_week1_ex2: //////// 
    Q = ["1", "2", "3", "4"]
    q = 1
    sigma = ["a", "b"]
    d = {
        ("1", "a"):1,   # --> 2
        ("1", "b"):3,   # --> 4

        ("2", "a"):2,   # --> 3
        ("2", "b"):0,   # --> 1

        ("3", "a"):3,   # --> 4
        ("3", "b"):1,   # --> 2

        ("4", "a"):3,   # --> 4
        ("4", "b"):3    # --> 4
    }
    F = [1]

    # Automaton sequence stored for formal definition
    M = [Q, q, sigma, d, F]


    dfa_week1_ex2 = dfa(M[0], M[1], M[2], M[3], M[4])
    # //////////////////////////////////
    
    STRING = "ababbabaabbaabbaab"

    dfa_read_string(dfa_week1_ex2, STRING)

main()