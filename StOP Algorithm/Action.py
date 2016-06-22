from Generator import Generator

class Action(object):

    """An action has to be hashable (in order to be stored in a set)"""
    def __eq__(self, other):
        if isinstance(other, Action):
            return (self.value == other.value and self.parent_state == other.parent_state)
        else:
            return False

    def __init__(self, parent_state, value):
        self.parent_state = parent_state
        self.value = value
        self.m = {} #dictionnary of m, with the key being the d
