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
    #processed_data = processed_data.reset_index()
    processed_data.to_csv('data/epl_processed.csv')
    return processed_data

def generate_prior_data(stats,epl_clubs,prior):
    d = []
    for clubA in epl_clubs:
        for clubB in epl_clubs:
            if clubA == clubB: continue
            try:
                xA = np.mean(map(float, prior[(prior['home_team'] == clubA) & (prior['away_team'] == clubB)]['home_score'].to_string(index = False).split('\n')) + map(float, prior[(prior['home_team'] == clubB) & (prior['away_team'] == clubA)]['away_score'].to_string(index = False).split('\n'))).round(2)
                xB = np.mean(map(float, prior[(prior['home_team'] == clubB) & (prior['away_team'] == clubA)]['home_score'].to_string(index = False).split('\n')) + map(float, prior[(prior['home_team'] == clubA) & (prior['away_team'] == clubB)]['away_score'].to_string(index = False).split('\n'))).round(2)
            except:
                xA = float(stats[stats.index == clubB]['Tier'].get_values())
                xB = float(stats[stats.index == clubA]['Tier'].get_values())
            d.append({'ClubA': clubA, 'ClubB': clubB, 'meanScoreA': xA, 'meanScoreB': xB})
    processed_data = pd.DataFrame(d).reindex_axis(['ClubA', 'meanScoreA', 'ClubB', 'meanScoreB'], axis = 1).set_index(['ClubA', 'ClubB'])
    processed_data.to_csv('data/epl_prior.tsv',sep='\t')
    return processed_data

def get_competition_stats(epl_clubs, prdata, pdata):
    teams = []
    seen = []
    for clubA in epl_clubs:
        for clubB in epl_clubs:
            if (clubA == clubB) | ((clubB, clubA) in seen): continue
            seen.append((clubA, clubB))
            attA = float(pdata[pdata['Club'] == clubA].Attack.get_values())
            defA = float(pdata[pdata['Club'] == clubA].Defence.get_values())
            midA = float(pdata[pdata['Club'] == clubA].Midfield.get_values())
            ratA = float(pdata[pdata['Club'] == clubA].Rating.get_values())
            tierA = float(pdata[pdata['Club'] == clubA].Tier.get_values())
            attB = float(pdata[pdata['Club'] == clubB].Attack.get_values())
            defB = float(pdata[pdata['Club'] == clubB].Defence.get_values())
            midB = float(pdata[pdata['Club'] == clubB].Midfield.get_values())
            ratB = float(pdata[pdata['Club'] == clubB].Rating.get_values())
            tierB = float(pdata[pdata['Club'] == clubB].Tier.get_values())
            winA = float(np.sign((prdata[(prdata['ClubA'] == clubA) & (prdata['ClubB'] == clubB)].meanScoreA - prdata[(prdata['ClubA'] == clubA) & (prdata['ClubB'] == clubB)].meanScoreB)))
            teams.append({'attA': attA, 'defA': defA, 'midA': midA, 'ratA':ratA, 'tierA': tierA, 'attB': attB, 'defB': defB, 'midB': midB, 'ratB':ratB, 'tierB': tierB, 'winA': winA })
    competition_stats = pd.DataFrame(teams)
    return competition_stats
