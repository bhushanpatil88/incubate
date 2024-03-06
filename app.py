import pandas as pd 

#Get the idea
idea = input()

#TODO: OM's Task
descriptions = {}
ceo_description = ''
cto_description = ''
cmo_description = ''

descriptions['CEO'] = ceo_description
descriptions['CTO'] = cto_description
descriptions['CMO'] = cmo_description

#TODO: Mehak's Task
people_data = pd.read_csv('people_data.csv')

#TODO: Bhushan's Task
community_data = pd.read_csv('communtiy_data.csv')


#TODO: Ruchi's Task
def WMD(str1:str,str2:str) -> int:
    pass

def apply_WMD(row,desc) -> dict:
    value = WMD(row['Tags'],desc)
    return {row['name'],value}

results = {}
for role,desc in descriptions.items():
    results[role] = people_data.apply(lambda row: apply_WMD(row,desc), axis = 1).tolist()

community_results = {}
for role,desc in descriptions.items():
    community_results[role] = community_data.apply(lambda row: apply_WMD(row,desc), axis = 1).tolist()

total_score = 0
people_score = 0
for name,value in results.items():
    people_score += value

community_score = 0
for name,value in community_results.items():
    community_score += value

total_score = 0.7 * people_score + 0.3 * community_score

#  Closest community
max_community = max(community_results, key=lambda x: community_results[x])

#TODO: Display the community
    