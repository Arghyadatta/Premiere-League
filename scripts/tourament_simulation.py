from common import *
from itertools import product, combinations, permutations
import heapq
import random

random.seed(1010101)

def rr_outcomes(n):
    '''Get all possible outcomes of a round robin tournament with n teams.
    Result will be an nxn matrix where outcome(i,j) = i beats j.
    Diagonals will be 0.'''
    num_games = (n*(n-1))/2
    outcomes_first_leg = []
    outcomes_second_leg = []
    for result in product([0,1], repeat=num_games):
        #result is 1-0 vector representing wins, losses for a set of games
        new_outcome = np.zeros((n,n))
        new_outcome[np.triu_indices(n, k=1)] = result
        new_outcome[np.tril_indices(n, k=-1)] = (1-new_outcome.T)[np.tril_indices(n, k=-1)]
        outcomes_first_leg.append(new_outcome)

    for result in product([0,1], repeat=num_games):
        #result is 1-0 vector representing wins, losses for a set of games
        new_outcome = np.zeros((n,n))
        new_outcome[np.triu_indices(n, k=1)] = result
        new_outcome[np.tril_indices(n, k=-1)] = (1-new_outcome.T)[np.tril_indices(n, k=-1)]
        outcomes_second_leg.append(new_outcome)

    # return outcomes_first_leg
    return outcomes_first_leg, outcomes_second_leg

def _mapper(ids):
    epl_clubs = ['Manchester City', 'Liverpool', 'Tottenham Hotspur', 'Chelsea', 'Arsenal', 'Everton', 'Bournemouth',
                 'Manchester United', 'Leicester City', 'Brighton & Hove Albion', 'Watford', 'Wolverhampton Wanderers',
                 'West Ham United', 'Newcastle United', 'Crystal Palace', 'Cardiff City', 'Huddersfield Town',
                 'Southampton', 'Burnley', 'Fulham']
    return [epl_clubs[i] for i in ids]

def to_wl_ids(outcome, group):
    '''Where outcome is an nxn 1-0 matrix for the outcome of a game,
    and ids is a list of n player ids, return two lists in the form winners,
    losers. Use this to index the probability array.'''
    loser_mat, winner_mat = np.meshgrid(group, group)
    return (winner_mat[outcome==1], loser_mat[outcome==1])


table = list(np.linspace(0,19,num=20,dtype=int))

#group results is nxn where group_result[i,j] -> i winner, j runner up
table_results = np.zeros((20,20))

import get_probs
wl = get_probs.get_probs()


f_o, s_o = rr_outcomes(len(table))

print np.shape(f_o)

