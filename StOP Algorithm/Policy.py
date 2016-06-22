from State import State

class Policy(object):
    """description of class"""
    def __init__(self, id):
        self.actions = {}

    def set_parameters(self, id, depth):
        self.id = id
        self.depth = depth
        self.lb = None
        self.ub = None

    """Given a state s, returns the action indicated by the policy"""
    def action(self, state):
        if state in self.action.keys():
            return action[state.value][0]
        else:
            raise Exception("This policy does not contain this state.")

    def position(self, state):
        if state in self.action.keys():
            return action[state.value][1]
        else:
            return self.depth #WARNING: if the policy does not contain the node, returns the depth of the policy, ie is a leaf


    def add_state(self, state, action, position):
        self.actions[state.value] = (action, position)
        state.policy_list.add(self.id) #not necessary