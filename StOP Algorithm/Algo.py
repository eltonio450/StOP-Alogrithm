from Generator import Generator
from State import State 
from Policy import Policy
from math import *

class Algo(object):
    """description of class"""
    """Overall, the policies are stored as a list, where as the states are stored as a set"""

    """A state value has to be hashable !"""

    def __init__(self):
        pass

    

    def set_parameters(self, Generator: generator, State: initial_state, epsilon, gamma, delta):
        self.generator = generator
        self.init = initial_state
        self.policies_list = []
        self.ordered_policy_list = [] #policies ordered by lower bound
        self.policies_ub = []
        self.policies_lb = []
        self.state_list = {}
        self.delta = delta
        self.epsilon = epsilon
        self.gamma = gamma
        self.ready = True
    

    def add_policy(self, pol, lb, ub, last_policy_id):
        if lpi != len(self.policies_list):raise Exception("The number of policies is not consistent with the id.")
        self.policies_list.append(pol)
        #self.policies_lb.append(lb)
        #self.policies_ub.append(ub)
        return last_policy_id + 1

    """Calculation of m as performed in the article"""
    def m(d, delta):
        t1 = log(1/delta)/2
        t2 = (1-self.gamma**d)/(self.gamma**d)
        return ceil(t1*t2**2)

    def run(self):
        if not self.ready:raise Exception("StOP Parameters have not been filled")
        
        d_star = ceil(log(6/((1-self.gamma)*self.epsilon))/log(1/self.gamma))

        self.state_list[self.init.value] = self.init
        lpi = 0 #last policy id

        """Must be corrected. Action list is know in the state""" 
        for action in self.generator.get_actions(self.init):
            pol = Policy()
            pol.set_parameters(lpi, 1)
            pol.add_state(self.init, action, 0) #is it really 0 ? I think so... 
            lpi = self.add_policy(pol, lb, ub, lpi)

            d = self.delta/(d_star*self.generator.bf(self.init))
             
            #s_u is a couple (state, action)
            self.sample_eff(pol, self.init, action, self.m(1,d))

        while True:
            candidate_policies = []
            for action in self.generator.get_actions(self.init):
                value_tr(self.init, action) #fait je sais pas trop quoi...
                #ici il faut sortir la meilleure policy pour cette action
            #ici il faut sortir les deux meilleures actions et policies associees
            p1,p2,a1,a2
            
            if p1.lb + self.epsilon >= p2.ub:
                return [p1, a1]

            if p2.depth >= p1.depth:
                a = a1
                p = p1
            else:
                a = a2
                p = p2

            #calculation of K:
            K = 1
            for i in range(0, p.depth): #meriterait d'etre verifie en termes d'indices
                K *= self.generator.pessimistic_action_number(self.init, i) ** self.generator.pessimistic_children_number(self.init, i)

            #multiplication du branching factor...
            d = self.delta/(d_star*K)#???
            

    def sample_eff(self, policy, state, action, m):
        if policy.position(state) == policy.depth:
            return
        #could be great to do it with a try catch and catch the error of missing key
        if policy.depth not in action.m.keys():
            action.m[policy.depth] = 0

        while action.m[policy.depth] < m:
            action.m[policy.depth] += 1
            next_state = self.generator.sample_transition(action)

            #idem: could be great with a try/catch
            if next_state.value not in self.state_list.keys():
                self.state_list[next_state.value] = next_state
            next_state = self.state_list[next_state.value]

            if policy.depth not in next_state.r.keys():
                next_state.r[policy.depth] = 0
            if policy.depth not in next_state.m.keys():
                next_state.m[policy.depth] = 0

            next_state.r[policy.depth] = (next_state.r[policy.depth]*next_state.m[policy.depth] + self.generator.sample_reward(next_state))/(1+next_state.m[policy.depth])
            next_state.m[policy.depth] += 1

            for item in self.generator.get_children_nodes(action):
                v = item.value
                if v not in self.state_list.keys():
                    self.state_list[v] = item
                if policy.depth not in state_list[v].m.keys():
                    self.state_list[v].m[policy.depth] = 0
                self.sample_eff(policy, self.state_list[v], self.state_list[v].m[policy.depth])