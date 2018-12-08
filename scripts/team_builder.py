from common import *


if __name__=='__main__':

    data_path='data/'

    prior=pd.read_csv(data_path+'prior_fixtures.tsv',sep='\t')

    squad_352_strict = ['GK', 'LB|LWB', 'CB', 'RB|RWB', 'LM|W$', 'RM|W$', 'CM', 'CM|CAM|CDM', 'CM|CAM|CDM', 'W$|T$', 'W$|T$']
    squad_442_strict = ['GK', 'LB|LWB', 'CB', 'CB', 'RB|RWB', 'LM|W$', 'RM|W$', 'CM', 'CM|CAM|CDM', 'W$|T$', 'W$|T$']
    squad_433_strict = ['GK', 'LB|LWB', 'CB', 'CB', 'RB|RWB', 'CM|LM|W$', 'CM|RM|W$', 'CM|CAM|CDM', 'W$|T$', 'W$|T$', 'W$|T$']
    squad_343_strict = ['GK', 'LB|LWB', 'CB', 'RB|RWB', 'LM|W$', 'RM|W$', 'CM|CAM|CDM', 'CM|CAM|CDM', 'W$|T$', 'W$|T$', 'W$|T$']
    squad_532_strict = ['GK', 'LB|LWB', 'CB|LWB|RWB', 'CB|LWB|RWB', 'CB|LWB|RWB', 'RB|RWB', 'M$|W$', 'M$|W$', 'M$|W$', 'W$|T$', 'W$|T$']

    squad_352_adj = ['GK', 'B$', 'B$', 'B$', 'M$|W$|T$', 'M$|W$|T$', 'M$|W$|T$', 'M$|W$|T$', 'M$|W$|T$', 'W$|T$|M$', 'W$|T$|M$']
    squad_442_adj = ['GK', 'B$', 'B$', 'B$', 'B$', 'M$|W$|T$', 'M$|W$|T$', 'M$|W$|T$', 'M$|W$|T$', 'W$|T$|M$', 'W$|T$|M$']
    squad_433_adj = ['GK', 'B$', 'B$', 'B$', 'B$', 'M$|W$|T$', 'M$|W$|T$', 'M$|W$|T$', 'W$|T$|M$', 'W$|T$|M$', 'W$|T$|M$']
    squad_343_adj = ['GK', 'B$', 'B$', 'B$', 'M$|W$|T$', 'M$|W$|T$', 'M$|W$|T$', 'M$|W$|T$', 'W$|T$|M$', 'W$|T$|M$', 'W$|T$|M$']
    squad_532_adj = ['GK', 'B$', 'B$', 'B$', 'B$', 'B$', 'M$|W$|T$', 'M$|W$|T$', 'M$|W$|T$', 'W$|T$|M$', 'W$|T$|M$']

    midfield = ['CDM', 'CM', 'RM', 'LM','CAM']
    defense = ['GK', 'LB', 'CB', 'RB', 'LWB', 'RWB']
    attack = ['LW', 'RW', 'ST','CAM']

    squad_list_strict = [squad_352_strict, squad_442_strict, squad_433_strict, squad_343_strict, squad_532_strict]
    squad_list_adj = [squad_352_adj, squad_442_adj, squad_433_adj, squad_343_adj, squad_532_adj]
    squad_name = ['3-5-2', '4-4-2', '4-3-3', '3-4-3', '5-3-2']

    epl_clubs=['Manchester City', 'Liverpool', 'Tottenham Hotspur', 'Chelsea', 'Arsenal', 'Everton','Bournemouth', 'Manchester United', 'Leicester City','Brighton & Hove Albion', 'Watford', 'Wolverhampton Wanderers', 'West Ham United', 'Newcastle United', 'Crystal Palace','Cardiff City', 'Huddersfield Town', 'Southampton', 'Burnley', 'Fulham']
    player_data = pd.read_csv('data/fifa_dataset_processed.tsv',sep='\t')

    # dict of clubs, each key is a club name and the value is a club object

    clubs_dict={}
    for key in epl_clubs: clubs_dict[key]=Club(key,player_data)


    df = generate_team_stats(clubs_dict,squad_list_adj,squad_name,midfield,defense,attack)
    df1 = generate_prior_data(df,epl_clubs,prior)
    df=df.reset_index()
    df1=df1.reset_index()
    df2 = get_competition_stats(epl_clubs,df1,df)

