
from aima import search as s


class Node:
    def __init__(self, value):
        self.vertex = value
        self.next = None


class WolfGoatCabbage:
    def __init__(self, initial, goal=({},{'F', 'W', 'G', 'C'})):
        self.initial = initial
        self.goal = goal
    
    def get_left(self, state):
        return state.index(0)
    
    def get_right(self, state):
        return state.index(1)
    
    def actions(self, state):
        possible_actions = [{'F'}, {'F', 'C'}, {'F', 'W'}, {'F', 'G'}]
        return possible_actions
    
    def goal_test(self, state):
        return state == self.goal
    
        
        
        
    
    

if __name__ == '__main__':
    wgc = WolfGoatCabbage([{'F', 'W', 'G', 'C'}])
    solution = s.depth_first_graph_search(wgc).solution()
    print(solution)
    solution = s.breadth_first_graph_search(wgc).solution()
    print(solution)
