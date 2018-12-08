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
    #processed_data.to_csv('data/WC18_processed.csv')
    return processed_data
