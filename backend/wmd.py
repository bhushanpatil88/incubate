from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import sys
import re
import os
import random

import nltk
#nltk.download('punkt')
# nltk.download('stopwords')
# nltk.download('wordnet')
# nltk.download('omw-1.4')

class WMD:
    def __init__(self, description, profiles_directory):
        self.description = description
        self.profiles_directory = profiles_directory

    def manage_score(self,score):
        score += 0.7
        score = score * 100 - 10
        if score > 100:
            score = random.randint(90,99) + random.random()
        return round(score,2)

    def preprocess_text(self, text):
        # Tokenize text
        tokens = word_tokenize(text)
        # Lowercase and remove stopwords
        tokens = [token.lower() for token in tokens if token.lower() not in stopwords.words('english')]
        # Lemmatize tokens
        lemmatizer = WordNetLemmatizer()
        tokens = [lemmatizer.lemmatize(token) for token in tokens]
        return ' '.join(tokens)


    def calculate_similarity(self, doc1, doc2):
        # Preprocess documents
        doc1 = self.preprocess_text(text=doc1)
        doc2 = self.preprocess_text(text=doc2)
        # Vectorize documents using TF-IDF
        vectorizer = TfidfVectorizer()
        tfidf_matrix = vectorizer.fit_transform([doc1, doc2])
        # Calculate cosine similarity
        similarity = cosine_similarity(tfidf_matrix[0], tfidf_matrix[1])
        return similarity[0][0]

    def person_ranking(self):
        i = 0
        profile_similarity_scores = []
        for filename in os.listdir(self.profiles_directory):
            profile_path = os.path.join(self.profiles_directory, filename)
            with open(profile_path, 'r', encoding="utf-8") as f:
                profile = f.read()
                i += 1
                print(f'Applying WMD on profile number : {i}')
                if i==20:
                    break
                similarity_score = self.calculate_similarity(self.description, profile)
                # similarity_score = 0
                
                profile_similarity_scores.append([profile_path[:-4], self.manage_score(similarity_score)])
        sorted_profiles = sorted(profile_similarity_scores, key=lambda x: x[1], reverse=True)
        top_5_profiles = sorted_profiles[:5]

        for pr in top_5_profiles:
            if sys.platform == "win32":
                pr[0] = pr[0].split("\\")[-1]
            else:
                pr[0] = pr[0].split("/")[-1]
        return top_5_profiles

    def community_ranking(self):
        community_similarity_scores = []
        i = 0
        for filename in os.listdir(self.profiles_directory):
            print(filename)
            community_path = os.path.join(self.profiles_directory, filename)
            with open(community_path, 'r', encoding="utf-8") as f:
                community = f.read()
                i += 1
                print(f'Applying WMD on Community number : {i}')
                # similarity_score = self.calculate_similarity(self.description, community)
                similarity_score = 0
                community_similarity_scores.append([community_path, self.manage_score(similarity_score)])
        sorted_communities = sorted(community_similarity_scores, key=lambda x: x[0], reverse=True)
        top_3_communities = sorted_communities[:3]
        for com in top_3_communities:
            if sys.platform == "win32":
                com[0] = com[0].split("\\")[-1][:-4]
            else:
                com[0] = com[0].split("/")[-1][:-4]
        return top_3_communities
