from common import *
from sklearn.naive_bayes import GaussianNB

# This method is modified from a github repository: https://github.com/puchiha/fifa-wc-2018-bayesian
def get_probs():
    # This function will generate a winning probability matrix
    matchData = pd.read_csv('../data/epl_competition_stats.tsv',sep='\t')
    data = matchData.iloc[:, :-1]
    targets = matchData.iloc[:, -1]

    gnb = GaussianNB()
    gnb.fit(data, targets)

    clubData = pd.read_csv('../data/epl_processed.csv')
    numClubs = len(clubData)
    prob_matrix = np.zeros((numClubs, numClubs))

    #For each pair of teams, find predicted label, convert to probability.
    for i in range(numClubs):
        for j in range(i+1,numClubs):
            clubA = clubData.iloc[i, :]
            clubB = clubData.iloc[j, :]

            point = [clubA.Attack, clubB.Attack, clubA.Defence, clubB.Defence, clubA.Midfield, clubB.Midfield, clubA.Rating, clubB.Rating, clubA.Tier, clubB.Tier]
            df = pd.DataFrame(np.array(point).reshape((1,10)), columns=data.columns)
            # winner = gnb.predict(df)
            probs = gnb.predict_proba(df)

            prob_matrix[i,j] = .5 * probs[0,1] + probs[0,2]
            prob_matrix[j,i] = .5 * probs[0,1] + probs[0,0]

    return prob_matrix


if __name__ == '__main__':
    print(get_probs())