class Generator(object):
    """Abstract Class with the functions to be filled by heritage"""
    def __init__():
        pass
        


    """Returns a list of all the possible actions given a state."""
    def get_actions(self, state):
        pass

    def get_children_nodes(self, action):
        pass

    def sample_transition(self, action):
        pass
    def sample_reward(self, state):
        pass

    """The branching factor corresponds to the number of couples (action, transition) possible.
    If this number cannot be easily calculated, please return an upper bound.
    """ 
    def bf(self, state):
        pass

    """Returns a pessimistic branching factor for the MDP, ie the worst case branching factor""" 
    def pessimistic_action_number(self, initial_state, depth):
        pass

    def pessimistic_children_number(self, initial_state, depth):
        pass
    