from common import *

# sum over probability matrix to get the expectation of {# of winning}
prob_matrix = np.array(get_probs())
expect_num_win = np.sum(prob_matrix, axis=1)





