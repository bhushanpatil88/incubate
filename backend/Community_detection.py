import random
import igraph as ig
import json
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import igraph as ig
import os


# edges = []
# def build_text_network(role,texts):
#     vectorizer = TfidfVectorizer(stop_words='english')
#     tfidf_matrix = vectorizer.fit_transform(texts)
#     cosine_similarities = cosine_similarity(tfidf_matrix, tfidf_matrix)
#     num_texts = len(texts)
#     edges = [(f'{role}_{i}', f'{role}_{j}', cosine_similarities[i][j]*10) for i in range(num_texts) for j in range(num_texts) if cosine_similarities[i][j] > 0.2 and i != j]

# ceo_data = []
# cmo_data = []
# cto_data = []

# for role in ["ceo","cto","cmo"]:
#     profiles = f'./Profile/{role}'
#     for filename in os.listdir(profiles):
#             profile_path = os.path.join(profiles, filename)
#             with open(profile_path, 'r', encoding="utf-8") as f:
#                 profile = f.read()
#                 if role == "ceo":
#                     ceo_data.append(profile)
#                 elif role == "cto":
#                     cto_data.append(profile)
#                 elif role == "cmo":
#                     cmo_data.append(profile)

# build_text_network("ceo",ceo_data)
# build_text_network("cto",cto_data)
# build_text_network("cmo",cmo_data)


# for i in range(0,1001):
#     for j in range(0,1001):
#         ran_num = random.choice([1,2,3,4,5,6,7,8,9,10])
#         if ran_num == 5:
#             ran_wt = random.choice([1,2,3,4,5,6,7,8,9,10])
#             edges.append((f'cto_{i}',f'cmo_{j}',ran_wt))

# for i in range(0,1001):
#     for j in range(0,1001):
#         ran_num = random.choice([1,2,3,4,5,6,7,8,9,10])
#         if ran_num == 5:
#             ran_wt = random.choice([1,2,3,4,5,6,7,8,9,10])
#             edges.append((f'cto_{i}',f'ceo_{j}',ran_wt))

# for i in range(0,1001):
#     for j in range(0,1001):
#         ran_num = random.choice([1,2,3,4,5,6,7,8,9,10])
#         if ran_num == 5:
#             ran_wt = random.choice([1,2,3,4,5,6,7,8,9,10])
#             edges.append((f'ceo_{i}',f'cmo_{j}',ran_wt))


# G = ig.Graph.TupleList(edges, weights=True)
# partition = G.community_multilevel(weights='weight')
# print(partition)

# G_dict = {}
# G1_dict = {}
# for k,v in G_dict.items():
#     if k not in G1_dict:
#         G1_dict[k] = []
    
#     l = v[0].split(',')
#     l1 = [str(x).strip() for x in l]
#     G1_dict[k] = l1
# json_obj = json.dumps(G1_dict)

# with open("Graph.json",'w') as f:
#     f.write(json_obj)

with open('Graph.json', 'r') as file:
    data = json.load(file)

for k,v in data.items():
    for file in v:
       
        if "ceo" in file:
            path = f'./Profile/ceo/{file}'
        elif "cto" in file:
            path = f'./Profile/cto/{file}'
        elif "cmo" in file:
            path = f'./Profile/cmo/{file}'

        with open(f'{path}.txt', 'r') as f:
            data = f.read()
        with open(f'.\\Community\\main\\{k}.txt','a') as f:
            f.write(data)

