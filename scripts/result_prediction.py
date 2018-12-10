from common import *


if __name__ == '__main__':
    # sum over probability matrix to get the expectation of {# of winning}
    prob_matrix = np.array(get_probs())
    expect_num_win = np.sum(prob_matrix, axis=1)

    data = pd.read_csv('../data/epl_processed.csv')
    clubs = np.array(list(data.iloc[:, 0]))

    idx = np.argsort(expect_num_win)[::-1]
    result = np.transpose([clubs[idx],expect_num_win[idx]])

    print('Generating result...\n')
    print(result)

