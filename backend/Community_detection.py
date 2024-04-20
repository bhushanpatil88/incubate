from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import igraph as ig
import os

def build_text_network(texts):

    vectorizer = TfidfVectorizer(stop_words='english')
    tfidf_matrix = vectorizer.fit_transform(texts)
    

    cosine_similarities = cosine_similarity(tfidf_matrix, tfidf_matrix)

    num_texts = len(texts)
    edges = [(i, j, cosine_similarities[i][j]) for i in range(num_texts) for j in range(num_texts) if cosine_similarities[i][j] > 0.2 and i != j]
    
    G = ig.Graph.TupleList(edges, weights=True)
    return G

def detect_communities(G):
    partition = G.community_multilevel(weights='weight')
    return partition

ceo_data = []
cmo_data = []
cto_data = []

for role in ["ceo","cto","cmo"]:
    profiles = f'./Profile/{role}'
    for filename in os.listdir(profiles):
            profile_path = os.path.join(profiles, filename)
            with open(profile_path, 'r', encoding="utf-8") as f:
                profile = f.read()
                if role == "ceo":
                    ceo_data.append(profile)
                elif role == "cto":
                    cto_data.append(profile)
                elif role == "cmo":
                    cmo_data.append(profile)
                
                


ceo_G = build_text_network(ceo_data)
cmo_G = build_text_network(cmo_data)
cto_G = build_text_network(cto_data)



ceo_communities = detect_communities(ceo_G)
cmo_communities = detect_communities(cmo_G)
cto_communities = detect_communities(cto_G)

community_ceo_folder = './Community/ceo'
community_cto_folder = './Community/cto'
community_cmo_folder = './Community/cmo'

profile_ceo = './Profile/ceo'
profile_cto = './Profile/cto'
profile_cmo = './Profile/cmo'


for i, community in enumerate(ceo_communities):
    print(f"Community {i+1}: {community}")
    profiles = ''
    for filename in os.listdir(profile_ceo):
        for j in community:
            if str(j)==filename[:-4]: 
                profile_path = os.path.join(profile_ceo, filename)
                with open(profile_path, 'r', encoding="utf-8") as f:
                    profile = f.read()
                    profiles += profile

    with open(f'{community_ceo_folder}/community_{i+1}',"w",encoding="utf-8") as f:
        f.write(profiles)


print("Communities:")
for i, community in enumerate(cmo_communities):
    print(f"Community {i+1}: {community}")
    profiles = ''
    for filename in os.listdir(profile_cmo):
        for j in community:
            if str(j)==filename[:-4]: 
                profile_path = os.path.join(profile_cmo, filename)
                with open(profile_path, 'r', encoding="utf-8") as f:
                    profile = f.read()
                    profiles += profile

    with open(f'{community_cmo_folder}/community_{i+1}',"w",encoding="utf-8") as f:
        f.write(profiles)

print("Communities:")
for i, community in enumerate(cto_communities):
    print(f"Community {i+1}: {community}")
    profiles = ''
    for filename in os.listdir(profile_cto):
        for j in community:
            if str(j)==filename[:-4]: 
                profile_path = os.path.join(profile_cto, filename)
                with open(profile_path, 'r', encoding="utf-8") as f:
                    profile = f.read()
                    profiles += profile

    with open(f'{community_cto_folder}/community_{i+1}',"w",encoding="utf-8") as f:
        f.write(profiles)
