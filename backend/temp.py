import random
import igraph as ig
import json

profile_ceo = './Profile/ceo'
profile_cto = './Profile/cto'
profile_cmo = './Profile/cmo'




edges = []
for i in range(0,1001):
    for j in range(0,1001):
        ran_num = random.choice([1,2,3,4,5,6,7,8,9,10])
        if ran_num == 5:
            ran_wt = random.choice([1,2,3,4,5,6,7,8,9,10])
            edges.append((f'cto_{i}',f'cmo_{j}',ran_wt))

for i in range(0,1001):
    for j in range(0,1001):
        ran_num = random.choice([1,2,3,4,5,6,7,8,9,10])
        if ran_num == 5:
            ran_wt = random.choice([1,2,3,4,5,6,7,8,9,10])
            edges.append((f'cto_{i}',f'ceo_{j}',ran_wt))

for i in range(0,1001):
    for j in range(0,1001):
        ran_num = random.choice([1,2,3,4,5,6,7,8,9,10])
        if ran_num == 5:
            ran_wt = random.choice([1,2,3,4,5,6,7,8,9,10])
            edges.append((f'ceo_{i}',f'cmo_{j}',ran_wt))


G = ig.Graph.TupleList(edges, weights=True)
partition = G.community_multilevel(weights='weight')
print(partition)
communities = {}

# Iterate over each vertex and its corresponding community
# for vertex, community_id in enumerate(partition.membership):
#     if community_id not in communities:
#         # If the community is not yet in the dictionary, add it
#         communities[community_id] = [vertex]
#     else:
#         # If the community is already in the dictionary, append the vertex to its list
#         communities[community_id].append(vertex)



# json_obj = json.dumps(G_dict)

# with open("Graph.json",'w') as f:
#     f.write(json_obj)



