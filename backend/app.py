import pandas as pd
import csv
from wmd import WMD
#Get the idea
idea = "Tweetsourcing"

#TODO: OM's Task
descriptions = {}
ceo_description = ''
cmo_description = ''
cto_description = ''
descriptions['CEO'] = ceo_description
descriptions['CMO'] = cmo_description
descriptions['CTO'] = cto_description



profiles_directory = 'Profiles'


#TODO: Bhushan's Task
# community_data = pd.read_csv('communtiy_data.csv')

wmd = WMD(re, profiles_directory)
top_5_profiles = wmd.wmd()
results = {}
for i, (profile_path, similarity_score) in enumerate(top_5_profiles, 1):
    print(f"Top {i} Profile (Similarity Score: {similarity_score}): {profile_path}")
    results[profile_path] = similarity_score

results_csv = "results.csv"
fields = ["Name", "Score"]
with open(results_csv, "w", encoding="utf-8") as f:
    csvwriter = csv.writer(f)
    csvwriter.writerow(fields)
    for name, value in results.items():
        csvwriter.writerow([name, value])

# community_results = {}
# for role,desc in descriptions.items():
#     community_results[role] = community_data.apply(lambda row: apply_WMD(row,desc), axis = 1).tolist()
#
# total_score = 0
# people_score = 0
# for name, value in results.items():
#     people_score += value
#
# community_score = 0
# # for name,value in community_results.items():
# #     community_score += value
#
# total_score = 0.7 * people_score + 0.3 * community_score
#
# print(total_score)

# #  Closest community
# max_community = max(community_results, key=lambda x: community_results[x])

#TODO: Display the community
    