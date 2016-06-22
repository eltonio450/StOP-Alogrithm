from Generator import Generator

class State(object):
    """The value describing a state has to be hashable ! A tuple for example is a good way to describe a state"""
   

    def __init__(self, value):
        self.value = value
        self.policy_list = [] #list of the id's for which the state belongs to the policy
        self.m = {} #dictionnary of m, with the key being the d
        self.r = {}
        self.actions_list = set()
        self.generated_actions = False #we don't generate the actions if we don't need it!

