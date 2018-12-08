from common import *

def generate_team_stats(clubs_dict, squad_list,squad_name,midfield,defense,attack):
    d = []
    for key in clubs_dict:
        best_rating, best_squad, best_formation, squad_stats = clubs_dict[key].get_best_formation_all(squad_list,squad_name)
        mid_rating, def_rating, att_rating = clubs_dict[key].get_team_stats(squad_stats,midfield,defense,attack)
        if best_rating > 84.0: tier = 1
        elif best_rating > 77.0: tier = 2
        else: tier = 3
        d.append({'Club': key, 'Rating': best_rating, 'Squad': best_squad, 'Defence': def_rating, 'Midfield': mid_rating, 'Attack': att_rating, 'Formation': best_formation,'Tier': tier})
    processed_data = pd.DataFrame(d).reindex_axis(['Club', 'Squad', 'Formation', 'Tier', 'Rating', 'Attack', 'Midfield', 'Defence'], axis = 1).set_index('Club')
    processed_data.to_csv('data/epl_processed.csv')
    return processed_data

def generate_prior_data(stats,epl_clubs):
    d = []
    for cA in qualified_countries:
        for countryB in qualified_countries:
            if countryA == countryB: continue
            try:
                xA = np.mean(map(float, prior[(prior['home_team'] == countryA) & (prior['away_team'] == countryB)]['home_score'].to_string(index = False).split('\n')) + map(float, prior[(prior['home_team'] == countryB) & (prior['away_team'] == countryA)]['away_score'].to_string(index = False).split('\n'))).round(2)
                xB = np.mean(map(float, prior[(prior['home_team'] == countryB) & (prior['away_team'] == countryA)]['home_score'].to_string(index = False).split('\n')) + map(float, prior[(prior['home_team'] == countryA) & (prior['away_team'] == countryB)]['away_score'].to_string(index = False).split('\n'))).round(2)
            except:
                xA = int(stats[stats.index == countryB]['Tier'].get_values())
                xB = int(stats[stats.index == countryA]['Tier'].get_values())
            d.append({'CountryA': countryA, 'CountryB': countryB, 'meanScoreA': xA, 'meanScoreB': xB})
    processed_data = pd.DataFrame(d).reindex_axis(['CountryA', 'meanScoreA', 'CountryB', 'meanScoreB'], axis = 1).set_index(['CountryA', 'CountryB'])
    processed_data.to_csv('data/WC18_prior.csv')

