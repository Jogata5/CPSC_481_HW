
from aima import search as s


class Node:
    def __init__(self, value):
        self.vertex = value
        self.next = None


class WolfGoatCabbage(s.Problem):
    def __init__(self, initial, goal=([{},{'F', 'W', 'G', 'C'}])):
        super().__init__(initial, goal)
        self.restricted_states = [{'W', 'G'}, {'G', 'C'}]
        self.bank_idx = {1, 2}

    
    def get_left(self, state):
        return state.index(0)
    
    def get_right(self, state):
        return state.index(1)
    
    def find_farmer(self, state):
        for idx, bank in enumerate(state):
            if 'F' in bank:
                return idx
        return 0
        
    def retricted(self, state):
        for bank in state:
            if set({'W', 'G'}, {'G', 'C'}) in bank:
                return True
        return False
        
        
    def actions(self, state):
        possible_actions = set({'F'}, {'F', 'C'}, {'F', 'W'}, {'F', 'G'})
        idx = self.find_farmer(state)
        self.bank_idx.remove(idx)
        idx2 = self.bank_idx.pop()
        
        subset = possible_actions.union(state[idx])
        
        if not self.retricted(state):
            state[idx2] + subset
            state[idx] - subset
            
        return state
    
    def goal_test(self, state):
        return state == self.goal
    
    def result(self, state, action):
        which_bank = self.find_farmer(state)
        new_state = list(state)

        delta = {{'F'}: -3, {'F', 'C'}: 3, {'F', 'W'}: -1, {'F', 'G'}: 1}
        neighbor = which_bank + delta[action]
        new_state[which_bank], new_state[neighbor] = new_state[neighbor], new_state[blank]

        return tuple(new_state)
    
        
        
        
    
    

if __name__ == '__main__':
    wgc = WolfGoatCabbage([{},{'F', 'W', 'G', 'C'}])
    solution = s.depth_first_graph_search(wgc).solution()
    print(solution)
    solution = s.breadth_first_graph_search(wgc).solution()
    print(solution)
