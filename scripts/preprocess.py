from common import *


class Club(object):
    def __init__(self,name,data):
        self.name=name.lower()
        self.data=data
        self.process()

    def process(self):
        # include all internal function calls here
        self.get_club_roster()

    def get_club_roster(self):
        self.data = self.data[self.data['Club']==self.name]

    def get_best_squad_n(self,formation,measurement = 'Potential'):
    # finds the best 11 players given formation
    # returns overall_squad_rating, squad_list, squad_stats (i.e. positions and ratings)
        store = []
        team = []
        df_copy=self.data.copy()
        for i in formation:
            store.append([df_copy.loc[[df_copy[df_copy['Preferred Position'].str.contains(i)][measurement].idxmax()]]['Preferred Position'].to_string(index = False),df_copy[df_copy['Preferred Position'].str.contains(i)][measurement].max()])
            team.append(df_copy.loc[[df_copy[df_copy['Preferred Position'].str.contains(i)][measurement].idxmax()]]['Name'].to_string(index = False))
            df_copy.drop(df_copy[df_copy['Preferred Position'].str.contains(i)][measurement].idxmax(), inplace = True)
        return np.mean([x[1] for x in store]).round(2), np.array(team), pd.DataFrame(np.array(store).reshape(11,2), columns = ['Position', measurement]).to_string(index = False)

    def get_best_formation_all(self,squad_list,squad_name):
        # finds the best formation for the given team
        # returns the best_rating, best_squad_list, best_formation, and squad_stats (i.e. positions   and ratings)
        best_rating = 0
        best_squad, best_formation = [], []
        for i, formation in enumerate(squad_list):
            print formation
            potRating, pot_squad, squad_info = self.get_best_squad_n(formation,'Potential')
            if potRating > best_rating:
                best_rating = potRating
                best_squad = pot_squad
                best_formation = squad_name[i]
        return best_rating, best_squad, best_formation, squad_info

    def get_team_stats(self,squad_stats,midfield,defense,attack):
    # gets the stats for attack, defence and midfield for a team
        midRating, defRating, attRating  = [], [], []
        for player in squad_stats.split('\n'):
            pos, rating = player.split()[0], player.split()[-1]
            if pos in midfield: midRating.append(float(rating))
            if pos in defense: defRating.append(float(rating))
            if pos in attack: attRating.append(float(rating))
        return np.mean(midRating).round(2), np.mean(defRating).round(2), np.mean(attRating).round(2)

"""
def generate_team_stats():
    d = []
    for club in qualified_clubs:best_rating, best_squad, best_formation, squad_stats =get_best_formation_all(squad_list_adj, club)
        mid_rating, def_rating, att_rating = get_team_stats(squad_stats)
        if best_rating > 84.0: tier = 1
        elif best_rating > 77.0: tier = 2
        else: tier = 3
        d.append({'Country': country, 'Rating': best_rating, 'Squad': best_squad,'Defence': def_rating,'Midfield': mid_rating, 'Attack': att_rating, 'Formation':best_formation,'Tier': tier})
     processed_data = pd.DataFrame(d).reindex_axis(['Country', 'Squad', 'Formation', 'Tier',   'Rating', 'Attack', 'Midfield', 'Defence'], axis = 1).set_index('Club')
     processed_data.to_csv('data/')
     return processed_data

 def generate_prior_data(stats):
     d = []
     for countryA in qualified_countries:
         for countryB in qualified_countries:
             if countryA == countryB: continue
             try:
                 xA = np.mean(map(float, prior[(prior['home_team'] == countryA) & (prior['away_team'] == countryB)]['home_score'].to_string(index = False).split('\n')) + map(float,           prior[(prior['home_team'] == countryB) & (prior['away_team'] == countryA)]['away_score'].to_string(index = False).split('\n'))).round(2)
                 xB = np.mean(map(float, prior[(prior['home_team'] == countryB) & (prior['away_team'] == countryA)]['home_score'].to_string(index = False).split('\n')) + map(float,           prior[(prior['home_team'] == countryA) & (prior['away_team'] == countryB)]['away_score'].to_string(index = False).split('\n'))).round(2)
             except:
                 # use a uniform prior
                 xA = int(stats[stats.index == countryB]['Tier'].get_values())
                 xB = int(stats[stats.index == countryA]['Tier'].get_values())
             d.append({'CountryA': countryA, 'CountryB': countryB, 'meanScoreA': xA, 'meanScoreB': xB})
     processed_data = pd.DataFrame(d).reindex_axis(['CountryA', 'meanScoreA', 'CountryB', 'meanScoreB'], axis = 1).set_index(['CountryA', 'CountryB'])
     processed_data.to_csv('data/WC18_prior.csv')
"""
